class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        list_to_print = []
        while current:
            # print(current.data)
            list_to_print.append(str(current.data))
            current = current.next

        print(" -> ".join(list_to_print))

    def sort_recursive(self):
        if self.head is None:
            return
        cur = self.head

        while cur:
            next_el = cur.next
            is_last = next_el.next is None
            cur.next = None if is_last else cur.next.next
            next_el.next = self.head
            self.head = next_el

            if is_last:
                break

    def sort_list(self):
        if self.head is None:
            return
        sorted_list = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = None
            if sorted_list is None:
                sorted_list = cur
            else:
                sorted_cur = sorted_list
                if cur.data < sorted_list.data:
                    cur.next = sorted_list
                    sorted_list = cur
                else:
                    while sorted_cur.next is not None and sorted_cur.next.data < cur.data:
                        sorted_cur = sorted_cur.next
                    cur.next = sorted_cur.next
                    sorted_cur.next = cur
            cur = next_node

        self.head = sorted_list

        return self


def merge_to_sorted_lists(list1: LinkedList, list2: LinkedList):
    res = LinkedList()
    el1 = list1.head
    el2 = list2.head

    while el1 is not None or el2 is not None:
        if el1 is None:
            res.insert_at_end(el2.data)
            el2 = el2.next
        elif el2 is None:
            res.insert_at_end(el1.data)
            el1 = el1.next
        elif el1 == el2:
            res.insert_at_end(el1.data)
            res.insert_at_end(el2.data)
            el1 = el1.next
            el2 = el2.next
        elif el1 < el2:
            res.insert_at_end(el1.data)
            el1 = el1.next
        elif el1 > el2:
            res.insert_at_end(el2.data)
            el2 = el2.next

    return res


llist1 = LinkedList()

llist1.insert_at_end(100)
llist1.insert_at_end(29)
llist1.insert_at_end(3)
llist1.insert_at_end(9)
llist1.insert_at_end(19)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(1000)
llist2.insert_at_end(101)
llist2.insert_at_end(100)
llist2.insert_at_end(1)

print("Raw list 1: ")
llist1.print_list()
print("Raw list 2: ")
llist2.print_list()

llist1.sort_recursive()
print("Recursive list 1: ")
llist1.print_list()
llist1.sort_list()
print("Sorted list 1: ")
llist1.print_list()
print("Merged list: ")
llist3 = merge_to_sorted_lists(llist1.sort_list(), llist2.sort_list())
llist3.print_list()
