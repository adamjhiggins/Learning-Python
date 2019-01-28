start = input('Enter file: ')
file = open(start)
end = dict()
for line in file :
    if line.startswith('From:') :
    # can use any variable instead of From depending on your block of text
        words = line.split()
        for word in words :
            sender = words[1]
            # sender can be changed to something related to your block of text
            # used words position 1 due to file format
        end[sender] = end.get(sender, 0) + 1

bigcount = None
bigword = None
for x,v in end.items():
    if bigcount is None or v > bigcount :
        bigword = x
        bigcount = v

print(bigword, bigcount)
