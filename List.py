l1 = []

while 1:
    print("enter choice\n1.insert\t2.getMin\t3.getMax\t4.delete\t5.search\t6.Display\t-1.Exit")
    choice = int(input())
    if choice == 1:
        item = int(input("enter item to add"))
        l1.append(item)
    elif choice == 2:
        print(min(l1))
    elif choice == 3:
        print(max(l1))
    elif choice == 4:
        ele = int(input("enter item to be deleted"))
        a = l1.count(ele)
        if a > 0:
            l1.remove(ele)
        else:
            print("item not present")
    elif choice == 5:
        x = int(input("enter item to be searched"))
        b = l1.count(x)
        if b > 0:
            print("element is present")
        else:
            print("element not present")
    elif choice == 6:
        # for item in l1:
        #     print(item, end=" ")
        print(l1)
        print()
    elif choice < -1 or choice > 6:
        print("invalid choice")
    else:
        break
