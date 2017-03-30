#Find the prime factors of a given number
# By Aden Huen

def prime(number):
    i = 2
    primes = [i]
    
    divisible = True
    while divisible == True:  
        #find next divisible number
        while int(number % i) != 0:
            i += 1
            
        #check if divisible number is prime
        divisible = True
        while divisible == True:    
            divisible = False
            for j in range(0, len(primes)):
                if int(i % primes[j]) == 0:
                    divisible = True
            
            if divisible == False:
                primes.append(i)
            else:
                divisible = True
                i += 1
    return i
            
def pfact(number):
    i = prime(number)
    factor = i
    
    while int(number / factor) != 1:
        mod = number / factor
        j = prime(mod)
        factor *= j
        print(j)

    return i