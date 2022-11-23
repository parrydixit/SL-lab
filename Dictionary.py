# from q6 import *
#
# AtomicDictionary()

dict = {'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Na': 'Sodium',
        'K': 'Potassium', 'Rb': 'Rubidium', 'F': 'Fluorine', 'O': 'Oxygen'}


def AtomicDictionary():
    while 1:
        print("enter choice\n1.Add\t2.Display\t3.Search\t4.Exit")
        choice = int(input())

        if choice == 1:
            k = (input("enter the key"))
            v = input("enter the value for the key")
            if k in dict:
                print("key is already PRESENT in the dictionary!!!")
            else:
                dict[k] = v

        elif choice == 2:
            print(dict)
            count =0
            for key,value in dict.items():
                if len(key) == 1:
                    count= count+1
            print(count)

        elif choice == 3:
            key = input("enter the key to be searched for:")
            if key in dict:
                print("key is PRESENT in the dictionary!!!")
                print("value of that key is:" + dict[key])
            else:
                print("key is NOT PRESENT in the dictionary!!!")
            print()

        else:
            exit()