import sys

list = sys.argv
list.pop(0)
for num in list:
    curent = int(num)

    if(curent % 3 == 0):
        if((curent % 5) == 0):
            print("fizzbuzz")
            continue
    if(curent % 3 == 0):
        print("fizz")
        continue
    if(curent % 5 == 0):
        print("buzz")
        continue
    print(curent)