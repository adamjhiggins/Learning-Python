import re
hand = open('data.txt')
lst = list()
for line in hand :
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) <=0 : continue
    for digit in num :
        x = int(digit)
        lst.append(x)
final = sum(lst)
print(final)
