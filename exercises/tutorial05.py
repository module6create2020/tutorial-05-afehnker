from exercises.mate import Mate

import bisect


def explore_stack():
    stack = list()
    stack.append(Mate("Alice", 1))
    stack.append(Mate("Bob", 3))
    stack.append(Mate("Cara", 6))
    stack.append(Mate("Dan", 5))
    stack.append(Mate("Emile", 2))

    print(stack)


def explore_queue():
    queue = list()
    queue.append(Mate("Alice", 1))
    queue.append(Mate("Bob", 3))
    queue.append(Mate("Cara", 6))
    queue.append(Mate("Dan", 5))
    queue.append(Mate("Emile", 2))

    print(queue)


def explore_sort():
    l = list()
    l.append(Mate("Alice", 1))
    l.append(Mate("Bob", 3))
    l.append(Mate("Cara", 6))
    l.append(Mate("Dan", 5))
    l.append(Mate("Emile", 2))

    l.sort()
    print(l)


def explore_priority_queue():
    sorted_list = list()
    bisect.insort(sorted_list, Mate("Alice", 1))
    bisect.insort(sorted_list, Mate("Bob", 3))
    bisect.insort(sorted_list, Mate("Cara", 6))
    bisect.insort(sorted_list, Mate("Dan", 5))
    bisect.insort(sorted_list, Mate("Emile", 2))

    print(sorted_list)


def update_element(a_list, an_element):
    if an_element in a_list:
        a_list.remove(an_element)
        bisect.insort(a_list, an_element)


def update_element_left(a_list, an_element):
    if an_element in a_list:
        a_list.remove(an_element)
        bisect.insort_left(a_list, an_element)


if __name__ == "__main__":
    print("\nExplore Stack")
    explore_stack()
    print("\nExplore Queue")
    explore_queue()
    print("\nExplore Sort")
    explore_sort()
    print("\nExplore Priority Queue")
    explore_priority_queue()

