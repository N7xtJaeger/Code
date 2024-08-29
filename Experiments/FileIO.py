import os

#TODO: Ask Linus what @staticmethod does

class FileIO:
    def __init__(self):


     def __str__(self):
        return "You called the FileHandler class"

    @staticmethod
    def clearfile(filepath):
        """
        A function to clear the contents of a file specified by the input argument 'filepath'
        :param filepath: the path of the file that should be cleared
        :return None: No returns
        """
        with open(filepath, 'w+') as file:
            pass

    @staticmethod
    def appendtofile(filepath, data, repetitions):
        """
        A function to append data to a file specified by the input argument 'filepath' as well as the number of
        repetitions to print the data N times to the file. It also automatically adjust do the type of the data.
        Currently, the types int, str and list are supported.
        :param filepath:
        :param data:
        :param repetitions:
        :return:
        """
        if isinstance(data, str):
            data = bytes(data.encode('utf-8'))

        elif isinstance(data, list):
            data = bytes((','.join(str(x) for x in data) + '\n').encode('utf-8'))

        elif isinstance(data, int):
            data = f"{data}{os.linesep}".encode('utf-8')

        with open(filepath, 'ab') as f:
            for i in range(repetitions):
                f.write(data)


    @staticmethod
    def readfile(filepath):
        """
        A simple function to read the contents of a file specified by the input argument 'filepath'
        :param filepath:
        :return None:
        """
        with open(filepath, 'r') as f:
            print(f.read())


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