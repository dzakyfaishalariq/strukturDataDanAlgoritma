class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlis:
    def __init__(self):
        self.head = None

    # tambah data awal
    def tambahDataAwal(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
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
        return total

    def cariData(self, value):
        temp = self.head
        value = int(value)
        while(temp):
            if temp.data == value:
                print("Nilai Ditemukan dengan nilai : {}".format(temp.data))
                break
            temp = temp.next
        return
    def hapusData(self, value):
        # menghapus head
        temp = self.head
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        # mencari nilai value di list
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        # jika value tidak ada di list
        if temp == None:
            return
        # ubah link node dari linkedlist
        prev.next = temp.next

        temp = None





