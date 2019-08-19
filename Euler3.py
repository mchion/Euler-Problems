# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

n = 600851475143
i = 2

while i*i <=n:   #a prime factor is always less than or equal to the square root of the number
    if n%i != 0:
        i+=1
    else:
        n//=i

print(n)
