'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

For Examples​:
Input 1:
4
Output 1:
2 + 2 = 4


Solution:

# Generates all prime numbers less than n.         
'''

def gen_prime(num, isPrime): 
    # Initialize all entries of boolean array as True. A value in isPrime[i] 
    # will finally be False if i is Not a prime, else True bool isPrime[n+1] 
    isPrime[0] = isPrime[1] = False
    for i in range(2, num+1): 
        isPrime[i] = True

    j = 2
    while(j*j <= num): 

        # If isPrime[j] is not changed,then it is a prime 
        if (isPrime[j] == True):
            # Update all multiples of j 
            i = j*j 
            while(i <= num): 
                isPrime[i] = False
                i += j 
        j += 1


def findaPrimePair(n):
    if n%2 == 0 and n>2: #Checking the value of “n”, if its an Even number
        isPrime = [0] * (n+1)  
        gen_prime(n, isPrime)     
        for i in range(0, n): 
            if (isPrime[i] and isPrime[n - i]): 
                print("Output:\n{} + {} = {}".format(i,(n-i),n))
                return
    else:
        return print("Please enter valid Even number greater than 2 to find its prime pair")


##Program execution starts from here
if __name__ == '__main__':
    num = int(input("Input:\n"))
    findaPrimePair(num)
