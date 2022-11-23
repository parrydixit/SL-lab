tlist = []


def ctof(cel):  # function for converting celsius to farhenite
    far = (9 / 5 * cel) + 32
    return far


def ftoc(cel):  # funtion for converting farhenite to celsius
    cel = (far - 32) * 5 / 9
    return cel


while 1:
    print("Main Menu")  # providing options for the user
    print("1. Celcius to Farhenite")
    print("2. Farhenite to Celcius")
    print("3. Print Tuple")
    print("4. Exit")

    n = int(input("Enter the desired the choice"))

    if (n == 1):
        cel = int(input("enter temperature in celsius:"))
        print("The temperature in farhenite is:" + str(ctof(cel)))  # calling function for farhenite conversion
        tlist.append(str(cel) + " C", str(ctof(cel)) + " F")  # appending to list

    if (n == 2):
        far = int(input("enter temperature in farhenite:"))
        print("The temperature in farhenite is:" + str(ftoc(far)))  # calling function for celsius conversion
        tlist.append(str(far) + " F", str(ftoc(far)) + " C")  # appending to list

    if n == 3:
        print(tuple(tlist))  # converting list to tuple

    if n == 4:
        break  # coming out of the infinite loop
