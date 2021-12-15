# init, add, value, del, isEmpty
from random import randint
import time


class Queue:

    def __init__(self, size=0):
        self.queue = [0] * size

    def add_el(self, val):  # добавление элемента в конец очереди
        self.queue.insert(0, val)

    def del_el(self):  # удаление элемента из начала очереди (FIFO)
        if len(self.queue) > 0:
            return self.queue.pop()
            # N_op += 4

    def is_empty(self):  # проверка на наличие элементов в очереди
        if len(self.queue) == 0:
            # N_op += 3
            return True
        else:
            # N_op += 1
            return False

    def size(self):
        a = 0
        for el in self.queue:
            a += 1
        return a

    def set(self, pos, value):  # замена элемента очереди по позиции
        self.queue[pos] = value
        return self.queue
        # N_op += 3

    def get(self, pos):  # получение элемента очереди по позиции
        # N_op += 2
        return self.queue[pos]

    def print_queue(self):
        for que in self.queue:
            print(que, end=' ')
            # self.N_op += 1

    def maximum(self):
        return max(self.queue)

    def counting_sort(self):
        max_el = max(self.queue)
        count = [0] * (max_el + 1)
        for que in self.queue:
            count[que] += 1

        for u in range(1, max_el + 1):
            count[u] += count[u - 1]

        result = Queue(len(self.queue))

        for k in self.queue:
            result.set(count[k] - 1, k)
            count[k] -= 1

        return result


N_op = 0

new_queue = Queue()
N_op += 1

for i in range(1, 11):
    for j in range(1000 * i):
        new_queue.add_el(randint(0, 100000))
        N_op += 1

    length = new_queue.size()
    max_ = new_queue.maximum()
    start = time.time()
    new_queue = new_queue.counting_sort()
    end = time.time()
    N_op += length + max_ + 1 + 3 * length + 4 * max_ + length + 1 + 5 * length
    timer = (end - start)
    print(
        f"Номер сортировки: {i}. Количество отсортированных элементов: {1000 * i}. Время сортировки (s): {timer:0.4f}. Количество операций (N_op): {N_op}")
    new_queue = Queue()
