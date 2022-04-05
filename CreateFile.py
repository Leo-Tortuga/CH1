def read_file():
    """
    returns the content of the file
    """
    txt = input("Enter File Name: ")
    file = open(txt)
    for i in file:
        print(i)


def create_file():
    """
    Ask the user to name a file and add text to it
    """
    try:
        file = input("Create a New File: " )
        name = open(file, "w")
    except:
        print("Not A Valid File Name.")
    print("Insert text")
    add = True
    while add == True:
        str = input("- ")
        if str == "Quit":
           add = False
        else:
            name.write(str)
            name.write("\n")
    name.close()
    return name