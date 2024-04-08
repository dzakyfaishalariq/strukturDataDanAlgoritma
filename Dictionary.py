# area Dictionary
Dict = {
    "nama" : "Dzaky",
    1 : [20,30,40],
    "umur" : 22,
}

Dict2 = {x : x**2+3 for x in range(20)}

if __name__ == "__main__":
    print(Dict["nama"])
    print(Dict.get("umur"))
    # menambahkan Dictionary
    Dict[2] = {
        "main" : "ini mermainan",
        "version" : "0.0.1"
    }
    print(Dict)
    print(Dict[2])
    print(Dict2)