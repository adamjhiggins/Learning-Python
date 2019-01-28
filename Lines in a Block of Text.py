fname = input("Enter file name: ")
fo = open(fname)
count = 0
for line in fo :
    if line.startswith('From ') :
        #From can be changed to match your block of text
        count = count + 1
        line = line.strip()
        address = line.split()
        print(address[1])
print('There were', count, 'lines in the file with From as the first word')
