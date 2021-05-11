# a function for getting a list of all primes in the range given, n+1 to get the full range up to n itself.
def getPrimes(n):
    primes = [2]
    for i in range(3,n+1,2):
        flag = True
        for prime in primes:
            if i%prime == 0:
                flag = False
        if flag:
            primes.append(i)
    return primes

# for getting the list of prime numbers between 2 and the num received
num = int(input("Enter requested range: "))

# the list of primes in the given range
primes = getPrimes(num)

# calculate the multiplication of all primes in the primes list so for later use.
primesMul = 1
for i in primes:
    primesMul *= i


# getting the square of the num (which is the biggest number we have to divide by)
# int function used for getting a natural value.
sqrtNum = int(num**0.5)

# we want to calculate for all primes in the list that are smaller than the square
# root of n the number of times that we need to increae them by a certain power "x"
# for it not to be larger than n . That way, we can know all of the combinations of
# multiples that we need in order to get the minimum number to multiply primesMul by
# to get the smallest number thats divided by all numbers in range.
# This works because when doing so, you can get all numbers and their powers below the
# range, meaning the devisible number we find at the end is divisible by all numbers in the range.
for prime in primes:
    if prime<=sqrtNum:
        temp = prime
        while temp<=num:
            # we want to keep multiplying until we pass num
            temp*=prime
        # we divide twice, one time because of the while passing
        # num and only checking after, the second time because in primesMul
        # we already have one of the primes to achieve that number,
        # so we need one power less.
        temp = int(temp /(prime*prime))
    # no need to check for more numbers in primes, we reached the
    # numbers which if we take to the power of 2 will pass num.
    else:
        break
    primesMul *= temp

print(primesMul)

