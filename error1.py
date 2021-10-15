a = 5
b = 1
try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number ::"))
    print(k)
    
except Exception as e:
    print('You cannot divide a number by zero::', e)

finally:
    print("resource closed")
    print("Bye")

