evtot = 0
nuev = 0
odtot = 0
nuod = 0
list = []
inp = input('Enter number OR \'quit\':\n')
while inp != 'quit':
    list.append(inp)
    inp = input('Enter number OR \'quit\':\n')

for i in range(len(list)):
    if int(list[i]) % 2 == 0:
        evtot = int(evtot) + int(list[i])
        nuev = nuev + 1
    else:
        odtot = int(odtot) + int(list[i])
        nuod = nuod + 1

print('Even total =', str(evtot) + '\nNumbers used =', nuev)
print('Odd mean =', str(odtot / nuod) + '\nNumbers used =', nuod)
