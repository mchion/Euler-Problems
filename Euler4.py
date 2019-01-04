# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#Discussion: We don't need to loop through 

i = 999
j = 999
result = 0
product = 0

while i >= 100: 
    while j >= 100: 
        product = i * j
        if str(product) == str(product)[::-1]:
            if result < product:
                result = product
        j = j-1
    j=999
    i = i-1

print(result)

