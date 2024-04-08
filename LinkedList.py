class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlis:
    def __init__(self):
        self.head = None

    # tampilkan list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next
        print(None)

    # jumlahkan semua nilai list
    def sumList(self):
        temp = self.head
        total = 0
        while(temp):
            if type(temp.data) == int:
                total += temp.data
            temp = temp.next
        return  total

