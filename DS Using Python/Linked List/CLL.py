class Node:
    def __init__(self, data = None, next = None):
        self.item = data
        self.next = next
    
class CLL:
    def __init__(self, last = None):
        self.last = last

    def is_empty(self):
        return self.last == None
    
    def insert_at_first(self, data):
        node = Node(data)
        if self.is_empty():
            node.next = node
            self.last = node
            print(f"{data} successfully inserted at first")
        else:
            node.next = self.last.next
            self.last.next = node
            print(f"{data} successfully inserted at first")

    def insert_at_last(self, data):
        node = Node(data)
        if self.is_empty():
            node.next = node
            self.last = node
            print(f"{data} successfully inserted at last")
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node
            print(f"{data} successfully inserted at last")

    def insert_after_a_value(self,data,val):
        node = Node(data)
        if self.is_empty():
            print(f"{val} is not present")
        else:
            temp = self.last.next
            if temp == self.last and temp.item == val:
                node.next = self.last
                self.last.next = node
                print(f"{data} successfully inserted after {val}")
            
            else:
                while temp is not self.last:
                    if temp.item == val:
                        node.next = temp.next
                        temp.next = node
                        print(f"{data} successfully inserted after {val}")
                        return
                    temp = temp.next

                if self.last.item == val:
                    node.next = self.last.next
                    self.last.next = node
                    print(f"{data} successfully inserted after {val}")
                    return
                print(f"{val} is not present")

    def print_list(self):
        if self.last == None:
            print("List is empty")
        else:
            temp = self.last.next
            while temp is not self.last:
                print(temp.item, " ->", end = ' ')
                temp = temp.next
            print(temp.item)

    def search(self, val):
        if self.last == None:
            print("List is empty")
        else:
            temp = self.last.next
            count = 0
            while temp is not self.last:
                if temp.item == val:
                    print(f"{val} is present at {count} index")
                    return
                count += 1
                temp = temp.next
            
            if temp.item == val:
                print(f"{val} is present at {count} index")
                return
            print(f"{val} is not present in the list")

    def delete_first(self):
        if self.is_empty():
            print("List is already empty")
        temp = self.last.next
        if self.last == temp:
            print(f"{self.last.item} had been deleted successfully")
            self.last = None
        else:
            print(f"{self.last.next.item} had been deleted successfully")
            self.last.next = self.last.next.next

    def delete_last(self):
        if self.is_empty():
            print("List is already empty")
        temp = self.last.next
        if self.last == temp:
            print(f"{self.last.item} had been deleted successfully")
            self.last = None
        else:
            while temp.next is not self.last:
                temp = temp.next
            print(f"{self.last.item} had been deleted successfully")
            temp.next = self.last.next
            self.last = temp

    def delete_a_value(self, val):
        if self.is_empty():
            print("List is already empty")
        temp = self.last.next
        if self.last == temp:
            if self.last.item == val:
                print(f"{self.last.item} had been deleted successfully")
                self.last = None
        else:
            while temp is not self.last:
                if temp.next.item == val:
                    if temp.next == self.last:
                        self.last = self.last.next
                        temp.next = temp.next.next
                        print(f"{val} had been deleted successfully")
                    else:
                        temp.next = temp.next.next
                        print(f"{val} had been deleted successfully")
                temp = temp.next
            if temp.next.item == val:
                self.delete_first()
                return

            print(f"{val} is not present in the list")
                    
                    

if __name__ == "__main__":        

    li = CLL()
    li.insert_at_first(4)
    li.insert_at_first(3)
    li.insert_at_last(5)
    li.insert_at_last(7)
    li.insert_after_a_value(6,5)
    li.print_list()
    li.search(6)
    li.delete_first()
    li.print_list()
    li.delete_last()
    li.print_list()
    li.delete_a_value(5)
    li.delete_a_value(4)
    li.delete_a_value(6)
    li.print_list()

'''
4 successfully inserted at first
3 successfully inserted at first
5 successfully inserted at last
7 successfully inserted at last
6 successfully inserted after 5
3  -> 4  -> 5  -> 6  -> 7
6 is present at 3 index
3 had been deleted successfully
4  -> 5  -> 6  -> 7
7 had been deleted successfully
4  -> 5  -> 6
5 had been deleted successfully
5 is not present in the list
4 had been deleted successfully
6 had been deleted successfully
List is empty
'''
