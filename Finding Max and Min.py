smallest = None
biggest = None

while True:
    prompt = input('Enter a number: ')
    if prompt == 'done' :
        break
    try:
        digit = float(prompt)
    except:
        print('Invalid input')
        continue

    if biggest is None :
        biggest = digit
    elif biggest < digit :
        biggest = digit

    if smallest is None :
        smallest = digit
    elif smallest > digit :
        smallest = digit

print('Maximum is', int(biggest))
print('Minimum is', int(smallest))
