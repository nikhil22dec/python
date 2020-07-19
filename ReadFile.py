dict={}
with open(r"C:\Users\jainnikh\Desktop\ListOfNames.txt", 'r') as open_file:
    line = open_file.readline()
    while line:
            line = line.strip() #rid of all whitespaces
            if line in dict:
                dict[line]+=1
            else:
                dict[line]=1
            line = open_file.readline()
print(dict)