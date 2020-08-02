import bz2
import sys

opener = bz2.open

if __name__ == "__main__":
    """create the compression files"""
    f = bz2.open(sys.argv[1], "wt")
    f.write(" ".join(sys.argv[2:]))
    f.close()

# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate>cd MyPackage
#
# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage>cd compressed
#
# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage\compressed>python bzipped.py test.bz2 data compression using bz2
#
# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage\compressed>python gzipped.py test.gz data compression using gz
