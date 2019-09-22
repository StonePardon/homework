class List:
    def __init__(self, num, next, prev):
        self.num = num
        self.next = next
        self.prev = prev

    def add(self, num):
        t = self
        while t.next != None:
            t = t.next
        t.next = List(num, None, t)

    def serch_num(self, num):
        t = self
        i = 0
        while t.next != None:
            if t.num == num:
                print("Element number " + str(i) + " is equal to " + str(num))
            t = t.next
            i = i + 1
        print("Search complete!")

    def serch_elem(self, num):
        t = self
        i = 0
        while i != num and t != None:
            t = t.next
            i += 1
        if i == num:
            print("Element number " + str(i) + " is equal to " + str(t.num))
            print("Search complete!")
        else:
            print("Search fail")

    def print(self):
         t = self
         print(t.num, end=" <-> ")
         while t.next != None:
             t = t.next
             print(t.num, end=" <-> ")
         print()


def deletion_elem(x, num):
    if num == 0:
        tmp = x.next
        tmp.prev = None
        del x
        return tmp
    t = x
    i = 0
    while i != num and t != None:
        i += 1
        t = t.next
    t.prev.next = t.next
    if t.next != None:
        t.next.prev = t.prev
    del t
    return x


def trans_list(number):
    s = str(number)
    print(s[0], s[1])
    i = 1
    tmp = List(s[0], None, None)
    while i < len(s):
        tmp.add(s[i])
        i += 1
    return tmp

