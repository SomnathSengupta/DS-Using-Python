class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self, data):
        node = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = node
        self.start = node
        print(f"{data} successfully inserted at first")

    def insert_at_last(self, data):
        if self.start is None:
            self.start = Node(None, data, None)
            print(f"{data} successfully inserted at last")
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            node = Node(temp, data, None)
            temp.next = node
            print(f"{data} successfully inserted at last")

    def insert_after_a_value(self, data, val):
        if self.start is None:
            print(f"{val} not present in the list")
        else:
            temp = self.start
            while temp is not None:
                if temp.data == val:
                    node = Node(temp, data, temp.next)
                    if temp.next is not None:
                        temp.next.prev = node
                    temp.next = node
                    print(f"{data} successfully inserted after {val}")
                    return
                temp = temp.next
            print(f"{val} is not present in the list")

    def print_list(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, " -> ", end='')
                temp = temp.next
            print("null")

    def print_reverse(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            
            while temp is not None:
                print(temp.data, " -> ", end='')
                temp = temp.prev
            print("null")


    def search(self, val):
        if self.start is None:
            print("List is empty")
        else:
            count = 0
            temp = self.start
            while temp is not None:
                if temp.data == val:
                    print(f"{val} present at {count} index")
                    return
                count+=1
                temp = temp.next
            
    def delete_first(self):
        if self.start is None:
            print("List is already empty")
        else:
            print(f"{self.start.data} had deleted successfully")
            self.start = self.start.next
            self.start.prev = None

    def delete_last(self):
        if self.start is None:
            print("List is already empty")
        elif self.start.next is None:
            print(f"{self.start.data} had deleted successfully")
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            print(f"{temp.data} had deleted successfully")
            temp.prev.next = None

    def delete_a_value(self, val):
        if self.start is None:
            print("List is already empty")

        elif self.start.data == val:
            self.delete_first()

        else:
            temp = self.start
            while temp is not None:
                if temp.data == val:
                    if temp.next == None:
                        self.delete_last()
                    else:
                        print(f"{val} had deleted successfully")
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        return
                temp = temp.next
            print(f"{val} is not present in the list")

if __name__ == "__main__":

    li = DLL()
    li.insert_at_first(2)
    li.insert_at_first(1)
    li.insert_at_last(3)
    li.insert_at_last(4)
    li.insert_after_a_value(6, 3)
    li.print_list()
    li.print_reverse()
    li.search(6)
    li.delete_first()
    li.print_list()
    li.delete_last()
    li.print_list()
    li.delete_a_value(3)
    li.print_list()

'''
2 successfully inserted at first
1 successfully inserted at first
3 successfully inserted at last
4 successfully inserted at last
6 successfully inserted after 3
1  -> 2  -> 3  -> 6  -> 4  -> null
4  -> 6  -> 3  -> 2  -> 1  -> null
6 present at 3 index
1 had deleted successfully
2  -> 3  -> 6  -> 4  -> null
4 had deleted successfully
2  -> 3  -> 6  -> null
3 had deleted successfully
2  -> 6  -> null
'''