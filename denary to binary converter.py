num = input("please input a number that you would like to convert to binary: ") 
num = int(num)
double = 1
counter = 0

while double < num:
    counter = counter + 1
    double = double * 2

counter = counter + 1
print(counter)

bi = 1
for i in range(counter - 1):
    bi = bi * 2


print(bi)

for i in range(counter):
    if num > bi or num == bi:
        print("1")
        num = num - bi
        bi = bi / 2
    else:
        print("0")
        bi = bi / 2
