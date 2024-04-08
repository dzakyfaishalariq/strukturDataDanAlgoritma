myList = [1,2,3,4,5,"hallo"]


if __name__ == "__main__":
    # menampilkan List
    print(myList)
    myList.append("Dzaky")
    myList.append(20)
    myList.pop(0)

    # myList.clear() # sebagai menghapus list
    # menampilkan lis dari belakang
    print(myList[::-1])
    for i in myList:
        if type(i) == int:
             print(f'ini adalah type {"int"} : {i}')
        else:
            print(f'ini adalah type {"str"} : {i}')