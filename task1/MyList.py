class List:
    def __init__(self, num, next = None, prev = None):
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


def num_to_list(number):
    s = str(number)
    i = 1
    tmp = List(int(s[0]), None, None)
    while i < len(s):
        tmp.add(int(s[i]))
        i += 1
    return tmp

def list_to_num(x):
    num = 0
    while x != None:
        num = 10*num + x.num
        x = x.next
    return num

def add_list(l1, l2):
    x1 = list_to_num(l1)
    x2 = list_to_num(l2)
    return trans_list(x1 + x2)


