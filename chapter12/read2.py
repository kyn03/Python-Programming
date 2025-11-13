infile = open("C:/python/chapter12/phones.txt", "r", encoding="utf-8")
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()
