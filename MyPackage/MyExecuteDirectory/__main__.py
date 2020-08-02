import sys
sys.path.append("MyExecuteDirectory")
import TextFileReader.TextFileReader as txtReader

print("executing __main__.py under MyExecuteDirectory")

r = txtReader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()


# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage>python MyExecuteDirectory "C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage\MyExecuteDirectory\Te
# xtFileReader\test.txt"
# executing __main__.py under MyExecuteDirectory
# Hello reading using text file reader ...
#
# (base) C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage>
