class FistOne():
    def __init__(self, my_iter):
        self.lst = list(my_iter) # Минус: чем длинее список, тем дольше будет выполяться операция по смене индексов оставшихся элементов

    def fifo(self, item):
        return self.lst.append(item), self.lst.pop(0)


class SecondOne():
    def __init__(self, my_iter):
        self.lst = list(my_iter)
        self.dic = dict(zip((x for x in range(len(self.lst))), self.lst))
        self.count = 0

    def fifo(self, item):
        self.dic.update({int(len(self.lst) + self.count): item})
        self.dic.pop(self.count)
        self.count += 1
# Много лишних переменных, аналогчная проблема как и при работе со списком

lst = SecondOne(input())
while True:
    lst.fifo(input())
    print(list(lst.dic.values()))
