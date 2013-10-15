
import linkedlist


def main():
    hm = HashMap(n=10)
    hm.add('firstname', 'Mattias')
    hm.add('lastname', 'Appelgren')
    hm.add('age', 23)
    print hm.get('age')
    print hm.get('lastname')
    print hm.get('firstname')
    print hm.hashlist
    for i, e in enumerate(hm.hashlist):
        print i, e


class HashMap(object):

    def __init__(self, n=100):
        self.n = n
        self.hashlist = self.n * [None]

    def add(self, key, value):
        hashed_key = hash(key) % self.n
        if not self.hashlist[hashed_key]:
            self.hashlist[hashed_key] = linkedlist.LinkedList()
        self.hashlist[hashed_key].add((key, value))

    def get(self, key):
        hashed_key = hash(key) % self.n
        ll = self.hashlist[hashed_key]
        if ll:
            li = ll.to_list()
            for k, v in li:
                if k == key:
                    return v
        return None


if __name__ == '__main__':
    main()
