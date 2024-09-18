def main():
    
    myFruit1 = input("myFruit1: ")
    myFruit2 = input("myFruit2: ")
    myFruit3 = input("myFruit3: ")

    yourFruit1 = input("yourFruit1: ")
    yourFruit2 = input("yourFruit2: ")

    theirFruit = input("theirFruit1: ")

    fruits = {myFruit1, myFruit2, myFruit3}
    print(sorted(fruits))

    fruits.add(theirFruit)
    print(sorted(fruits))

    fruitsInter = fruits & {yourFruit1, yourFruit2}
    print(sorted(fruitsInter))

    fruits.remove(myFruit1)
    print(sorted(fruits))


if __name__ == "__main__":
    
    main()