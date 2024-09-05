from Experiments.FileIO import FileIO as fio
import math

file = 'test.txt'

data = f"{math.sqrt(1*2*3*4*5)}, a, b, c \n"

fio.clear_file(file)

fio.append_to_file(file, data, 6)

fio.read_file(file)

data = [15, 35, 56, 24, 100, 34, 64]

#fio.clear_file(file)

fio.append_to_file(file, data, 6)

print(fio.read_file(file))


#(lambda: print("This is an anonymous function"))()      # funky code where the function that was just created gets called immediately...
# a lambda function cant be called like a normal function, it would defeat the purpose of the lambda function
