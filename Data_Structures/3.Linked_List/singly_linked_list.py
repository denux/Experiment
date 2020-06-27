class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.sn = None

    def traverse_list(self):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        while n is not None:
            print(n.item)
            n = n.ref

    def insert_at_start(self, data):
        nn = Node(data)
        if self.sn is None:
            self.sn = nn
        else:
            nn.ref = self.sn
            self.sn = nn

    def insert_at_end(self, data):
        if self.sn is None:
            print("No List found")
            return

        nn = Node(data)
        n = self.sn
        while n.ref is not None:
            n = n.ref
        n.ref = nn

    def insert_after_item(self, x, data):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item not found")
        else:
            nn = Node(data)
            nn.ref = n.ref.ref
            n.ref.ref = nn

    def insert_before_item(self, x, data):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item not found")
        else:
            nn = Node(data)
            nn.ref = n.ref
            n.ref = nn

    def insert_at_index(self, index, data):
        if index == 0:
            if self.sn is None:
                self.sn = Node(data)
            else:
                nn = Node(data)
                nn.ref = self.sn
                self.sn = nn
        else:
            count = 0
            n = self.sn
            while count != index - 1:
                n = n.ref
                count += 1
            nn = Node(data)
            nn.ref = n.ref
            n.ref = nn

    def get_count(self):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        count = 0
        while n is not None:
            n = n.ref
            count += 1
        print("count is :", count)

    def search_item(self, x):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        while n.ref is not None:
            if n.ref.item == x:
                print("Found")
                return
            n = n.ref
        print("Not Found")

    def delete_at_start(self):
        if self.sn is None:
            print("No List found")
            return
        self.sn = self.sn.ref

    def delete_at_end(self):
        if self.sn is None:
            print("No List found")
            return
        n = self.sn
        if n.ref is None:
            self.sn = None
        else:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_element_by_value(self, x):
        if self.sn is None:
            print("No List found")
            return

        if self.sn.item == x:
            self.sn = self.sn.ref
            return

        n = self.sn
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.sn
        while n:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.sn = prev
