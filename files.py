from os import write

f = open("pic.png", "rb")

f1 = open("newpic.JPG", "wb")
for i in f:
    f1.write(i)



# f = open("MyData.txt", "r")

# f1 = open("abc", "w")
 
# for data in f:
#     f1.write(data)

# w = write
# a  = append
# r = read

# print(f.readline())
# print(f.readline())
# f1.write("Laptop")