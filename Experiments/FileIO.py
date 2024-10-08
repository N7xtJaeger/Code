"""
File IO class, V0.1
Written by Lennart Golumbeck, 04.09.2024

History:

"""

import os


class FileIO:
    def __init__(self):
        pass

    def __str__(self):
        return "You called the FileHandler class"

    @staticmethod
    def clear_file(filepath: str):
        """
        A function to clear the contents of a file specified by the input argument 'filepath'
        :param filepath: the path of the file that should be cleared
        :return None: No returns
        """
        with open(filepath, 'w+'):      # as file not needed as we just pass anyway
            pass

    @staticmethod
    def append_to_file(filepath: str, data: [str, list]):
        """
        A function to append data to a file specified by the input argument 'filepath'.
        It also automatically adjusts to the type of the data.
        Currently, the types int, str and list are supported.
        :param filepath:
        :param data:
        :return:
        """
        if isinstance(data, str):
            data = bytes(data.encode('utf-8'))

        elif isinstance(data, list):
            data = bytes((','.join(str(x) for x in data) + '\n').encode('utf-8'))

        elif isinstance(data, int):
            data = f"{data}{os.linesep}".encode('utf-8')

        else:
            raise Exception("append_to_file, unsupported data type")

        with open(filepath, 'ab') as f:
            f.write(data)


    @staticmethod
    def read_file(filepath: str) -> str:     # type annotation to specify the return, python doesn't enforce this tho
        """
        A simple function to read the contents of a file specified by the input argument 'filepath'
        :param filepath:
        :return None:
        """
        with open(filepath, 'r') as f:
            return f.read()


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