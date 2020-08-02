import sys
import os

class Reader:
    def __init__(self, filename):
        self._filename = filename
        self.f = open(self._filename, "rt")

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()


if __name__ == "__main__":
    print("executing Module TextFileReader")
    obj = Reader("test.txt")
    print(obj.read())
    obj.close()
