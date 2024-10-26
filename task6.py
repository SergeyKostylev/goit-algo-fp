class FoodItem:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories

    def get_valuation(self):
        return self.calories / self.cost

    def __repr__(self):
        return f'{self.name} cost:{self.cost} calories:{self.calories} {self.get_valuation():.2f}\n'


def create_items_from_raw_data(data):
    res = []
    for name, item_data in data.items():
        res.append(FoodItem(name, item_data["cost"], item_data["calories"]))
    return res


def greedy_algorithm(items: list[FoodItem], budget: int):
    sorted_items = sorted(items, key=lambda x: x.get_valuation(), reverse=True)

    total_cost = 0
    total_calories = 0
    selected_food_items = []

    for item in sorted_items:
        if total_cost + item.cost <= budget:
            selected_food_items.append(item.name)
            total_cost += item.cost
            total_calories += item.calories

    return selected_food_items, total_calories


def dynamic_programming(items: list[FoodItem], budget: int):
    dp = [0] * (budget + 1)
    selected_food_items = [[] for _ in range(budget + 1)]

    for item in items:
        for current_budget in range(budget, item.cost - 1, -1):
            if dp[current_budget - item.cost] + item.calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - item.cost] + item.calories
                selected_food_items[current_budget] = selected_food_items[
                                                          current_budget - item.cost
                                                          ] + [item.name]

    optimal_items = selected_food_items[budget]
    total_calories = dp[budget]

    return optimal_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

item_list = create_items_from_raw_data(items)
functions = {
    "Greedy Algorithm": greedy_algorithm,
    "Dynamic Programming": dynamic_programming
}

budget = 100
for name, function in functions.items():
    selected_items, total_calories = function(item_list, budget)
    print(name)
    print(f"Selected Food: {", ".join(selected_items)}")
    print(f"Total Calories: {total_calories}\n")
