import gzip
import sys

opener = gzip.open

if __name__ =="__main__":
    """create the compression files"""
    f = gzip.open(sys.argv[1], "wt")
    f.write(" ".join(sys.argv[2:]))
    f.close()