#Binary to Number converter
# By Aden Huen

def bin2num(number):
    invalid = False
    l_num = list(str(number))
    
    for i in range(0,len(l_num)):
        if l_num[i] != '1' and l_num[i] != '0':
            invalid = True
        else:
            pass
            
    if invalid == False:
        count = 0
        sum = 0
        for i in range(len(l_num)-1, -1, -1):
            sum = sum + (int(l_num[i]) * (2 ** count))
            count+=1
        return sum
    else:
        print("Please enter a valid binary number")
        