def hanoi(x):
    if x == 1:
        return 1
    else:
        return 2*hanoi(x-1) + 1
x = int(input("ENTER THE NUMBER OF DISKS: "))
print('NUMBER OF STEPS: ', hanoi(x))
