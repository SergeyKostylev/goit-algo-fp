from random import randint


class SumResult:

    def __init__(self, sum_value):
        self.sum_value = sum_value
        self.amount = 0
        self.percent = 0

    def __str__(self):
        return f"{self.sum_value:>2}  {self.amount:>7}  {self.percent:>7.3f} %"


def throws(throw_amount: int):
    result = {key: SumResult(key) for key in range(2, 13)}

    for _ in range(throw_amount):
        value1 = randint(1, 6)
        value2 = randint(1, 6)
        loop_sum = value1 + value2

        result[loop_sum].amount += 1

    for sum_value, data in result.items():
        result[sum_value].percent = data.amount / throw_amount

    return result


res = throws(50000)
print("Sum   Amount   Percent")
for key, item in res.items():
    print(item)
