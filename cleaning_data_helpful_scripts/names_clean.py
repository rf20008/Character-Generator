data = "data.rtf"
file = open(data)
Names = {}
for line in file:
    c = 0
    Name = ""
    print(c, line)
    while line[c] != " ":
        Name += line[c]
        c +=1
    c+=1
    Population = float(line[c] + line[c+1] + line[c+2] + line[c+3])
    Names[Name] = Population

print(Names)
file.close()
