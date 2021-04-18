print("Months Dictionary Script by Alex Bourg \n")
monthConversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


def monthf():
    month = input("Enter month number: ")
    month = float(month)
    while month not in (int(1), int(2), int(3), int(4), int(5), int(6), int(7), int(8), int(9), int(10), int(11), int(12)):
        print("Invalid month!")
        month = input("Enter month number: ")
        month = float(month)

    print(str(month) + " is " + monthConversions.get(month, "Not a valid month") + "\n")
    monthf()

monthf()
