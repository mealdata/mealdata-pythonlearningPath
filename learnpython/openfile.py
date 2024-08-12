Countries_file = open("file.txt")

#print(Countries_file.readlines()) this will print ['Ethiopia\n', 'Kenya\n', 'France\n', 'Moroca\n', 'Uganda\n', 'Djiabout\n']

for lines in Countries_file.readlines():
    print(lines)

Countries_file.close()

