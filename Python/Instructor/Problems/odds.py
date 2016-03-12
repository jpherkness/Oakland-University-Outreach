# Write a definition that prints all odd numbers between 'a' and 'b'
# Hint: Could you use modulus(%)?
def odds(a, b):
    for i in range(a, b):
        if(i % 2 == 1):
            print(i)
            
odds(0, 10)
