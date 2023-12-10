def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("File", file_name, "wasn't opened!")

        return None

    else:

        print("File", file_name, "was opened!")

        return file

file1_name = "TF9_1.txt"

file2_name = "TF9_2.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):
    file_1_w.write("Short line\n")
    file_1_w.write("This is a longer line that needs to be truncated\n")
    file_1_w.write("Another short line\n")
    file_1_w.write("This line is very long and will be cut off\n")
    file_1_w.write("Short line again\n")
    print("Information was successfully added to TF9_1.txt!")
    file_1_w.close()

file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r != None or file_2_w != None:
    for line in file_1_r:
        if len(line) < 20:
            line = line.rstrip('\n') + ' ' * (20 - len(line))
        else:
            line = line[:20]
        file_2_w.write(line + '\n')
file_1_r.close()
file_2_w.close()

file_2_r = Open(file2_name, "r")


with open('TF9_2.txt', 'r') as file:
    for line in file:
        print(line)