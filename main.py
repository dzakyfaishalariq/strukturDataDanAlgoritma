from LinkedList import Node, Linkedlis

if __name__ == "__main__":
    list = Linkedlis()
    list.head = Node(1)
    kedua = Node(2)
    ketiga = Node(3)

    # menyambungkan dengan node
    list.head.next = kedua
    kedua.next = ketiga
    # tampilkan lis
    list.printList()
    # tampilkan jumlah list
    print(list.sumList())
    print("Pogram Berhasil Dijalankan")