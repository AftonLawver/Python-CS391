
try:
    # create the file
    f = open("test3.txt", "x")
    print("file created.")
    # open the file for writing
    f = open("test3.txt", "w")

    # write the first three lines
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")
    f.close()

    # read the first two lines of the file
    file = open("test3.txt", "r")
    print(file.readline())
    print(file.readline())
    file.close()

    # append a fourth line to the file 
    file = open("test3.txt", "a")
    file.write("This is the fourth line")  
    file.close()

    # read the rest of the lines in the file
    file = open("test3.txt", "r")
    for line in file.readlines()[2:]:
        print(line)

except FileExistsError:
    print("File already exists.")
    f = open("test.txt", "w")

    # write the first three lines
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")
    f.close()

    # read the first two lines of the file
    file = open("test.txt", "r")
    print(file.readline())
    print(file.readline())
    file.close()

    # append a fourth line to the file 
    file = open("test.txt", "a")
    file.write("This is the fourth line")  
    file.close()

    # read the rest of the lines in the file
    file = open("test.txt", "r")
    for line in file.readlines()[2:]:
        print(line)


