while True:
    num = input()
    if num == '-1': break
    
    try:
        if num[1] == 'x': print(int(num, base=16))
        else: print('0x' + hex(int(num))[2:].upper())
    except IndexError:
        print('0x' + num)