from LinkedList import Node, Linkedlis

if __name__ == "__main__":
    list = Linkedlis()
    list.head = Node(1)
    kedua = Node(2)
    ketiga = Node(3)
    keempat = Node("Hllo")

    # menyambungkan dengan node
    list.head.next = kedua
    kedua.next = ketiga
    ketiga.next = keempat
    # tampilkan lis
    list.printList()
    # tampilkan jumlah list
    print(list.sumList())
    list.cariData(3)
    print(list.hapusData(2))
    list.printList()

    list.tambahDataAwal(40)
    list.tambahDataAwal(41)
    list.tambahDataAwal(42)
    list.printList()
    print("Pogram Berhasil Dijalankan")