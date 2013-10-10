

def main():
    ll = LinkedList()

    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(5)
    ll.add(7)
    ll.add(8)
    print ll
    print ll.length()


class LinkedList(object):

    def __init__(self):
        self.start = Node(None)
        self.last = self.start
        self.size = 0

    def add(self, d):
        n = Node(d)
        self.last.next = n
        self.last = n
        self.size += 1

    def length(self):
        return self.size

    def remove(self, d):
        pass

    def to_list(self):
        n = self.start
        l = []
        while n.next:
            l.append(n.next.data)
            n = n.next
        return l

    def __str__(self):
        s_list = [str(x) for x in self.to_list()]
        return " --> ".join(s_list)


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == '__main__':
    main()
