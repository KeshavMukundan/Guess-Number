def lunh_algorithm(credit) -> int:
    temp = " ".join(str(credit))    
    temp = list(map(int,temp.split()))
    temp1 = []
    temp2 = []
    for i in range(len(temp) - 2, -1, -2):
        u = temp[i]*2
        if len(str(u)) != 2:
            temp1.append(u)
        else:
            for i in str(u):
                temp1.append(int(i))
    sum_temp1 = sum(temp1)
        
    for index in range(len(temp) - 1, -1 , -1):
        if index % 2 != 0:
            temp2.append(temp[index])
    
    sum_temp2 = sum(temp2)
    
    sum_temp = sum_temp1 + sum_temp2
    
    if sum_temp % 10 == 0:
        return 1
    else:
        return -1
        
    
                
    
        
        
credit = input("Please enter your credit card: ")

if (lunh_algorithm(credit) == -1):
    print("That is not a valid credit card")
else:
    print("That is a valid credit card")
