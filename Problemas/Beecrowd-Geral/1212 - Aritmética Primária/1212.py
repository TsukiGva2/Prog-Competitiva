while True:
    num1, num2 = input().split()
    if num1 == '0' and num2 == '0': break
    
    lenght  = len(num1) - len(num2)
    carries = 0

    if lenght > 0:
        num2 = '0'*lenght + num2
    else:
        num1 = '0'*(lenght * -1) + num1
    
    result = ''
    carry = 0

    for i in range(len(num1)-1, -1, -1):
        if int(num1[i]) + int(num2[i]) + carry > 9:
            carries += 1
            carry = 1
        else:
            carry = 0

        result = str((int(num1[i]) + int(num2[i])) % 10) + result
    
    if carries == 0:
        print("No carry operation.")
    elif carries == 1: 
        print("1 carry operation.")
    else:
        print(f"{carries} carry operations.")