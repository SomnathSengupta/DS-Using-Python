class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
class SLL:
    def __init__(self, start = None):
        self.start = start

    def isempty(self):
        return self.start == None
    
    def insert_at_first(self, data):
        node = Node(data)
        if self.start == None:
            self.start = node
            print(data," successfully inserted at first")
        else:
            node.next = self.start
            self.start = node
            print(data," successfully inserted at first")

    def insert_at_last(self, data):
        node = Node(data)
        if self.start == None:
            self.start = node
            print(data," successfully inserted at last")
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            node.next = None
            temp.next = node
            print(data," successfully inserted at last")

    def print_list(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, " -> ", end = ' ')
                temp = temp.next
            print("null")

    def insert_after_a_value(self, val, data):
        if self.start == None:
            print("List is empty")
        else:
            node = Node(data)
            temp = self.start
            while temp is not None:
                if temp.item == val:
                    node.next = temp.next
                    temp.next = node
                    print(data," successfully inserted after", val)
                    return
                temp = temp.next
            print(val," not present in the list")

    def search(self, val):
        if self.start == None:
            print("List is empty")
        else:
            count = 0
            temp = self.start
            while temp is not None:
                if temp.item == val:
                    print(val, " present at ", count, " index")
                    return
                count += 1
                temp = temp.next
            print("Value not present")

    def delete_first(self):
        if self.start == None:
            print("List is empty")
        else:
            print(self.start.item, " deleted successfully")
            self.start = self.start.next

    def delete_last(self):
        if self.start == None:
            print("List is empty")
        elif self.start.next is None:
            print(self.start.item, " deleted successfully")
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            print(temp.next.item, " deleted successfully")
            temp.next = None

    def delete_a_value(self, val):
        if self.start == None:
            print("List is empty")
        elif self.start.next is None:
            if self.start.item == val:
                print(self.start.item, " deleted successfully")
                self.start = None
            else:
                print(val, " not present in the list")
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == val:
                    print(val, " deleted suxxessfully")
                    temp.next = temp.next.next
                    return
                temp = temp.next
            print(val, " not present in the list")

if __name__ == "__main__":

    li = SLL()
    li.insert_at_first(2)
    li.insert_at_first(3)
    li.insert_at_last(5)
    li.print_list()
    li.insert_after_a_value(5, 20)
    li.insert_after_a_value(2, 4)
    li.print_list()
    li.search(4)
    li.delete_first()
    li.print_list()
    li.delete_last()
    li.delete_last()
    li.print_list()
    li.delete_a_value(4)
    li.print_list()

'''
2  successfully inserted at first
3  successfully inserted at first
5  successfully inserted at last
3  ->  2  ->  5  ->  null
20  successfully inserted after 5
4  successfully inserted after 2
3  ->  2  ->  4  ->  5  ->  20  ->  null
4  present at  2  index
3  deleted successfully
2  ->  4  ->  5  ->  20  ->  null
20  deleted successfully
5  deleted successfully
2  ->  4  ->  null
4  deleted suxxessfully
2  ->  null

'''

