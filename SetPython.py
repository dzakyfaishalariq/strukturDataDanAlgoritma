Set = {1,2,3,4,"HALLO",4,5,6}
stringSet = "Hallo"
if __name__ == "__main__":
    print(type(Set), Set)
    print(set(stringSet))
    for i in list(set(stringSet))[::-1]:
        print(i, end=" ")