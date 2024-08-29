with open('test.csv', 'w+') as file:
    pass

with open('test.csv', 'ab') as f:       # ab Append as Bytes siehe: f.write
    for i in range(10):
        f.write(bytes(f"{i + 1}, a, b, c\n", 'utf-8'))

with open('test.csv', 'r') as f:
    print(f.read())

(lambda: print("This is an anonymous function"))()      # funky code where the function that was just created gets called immediately...
# a lambda function cant be called like a normal function, it would defeat the purpose of the lambda function
'''
The UGLY way, would also have to do a try-finally (sagt linus)

f = open('test.csv', 'w')
f.write(f"{datetime.datetime.date(today()).isoformat()}\n")
f.close()
f = open("test.csv", 'a')
for i in range(10):
    f.write(f"{i + 1}, a,b ,c \n")
f.close()

f = open("test.csv", 'r')
print(f.read())
'''