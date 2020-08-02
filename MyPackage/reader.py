from .compressed import bzipped, gzipped # relative import works with modules inside a particular packege (MyPackage)
#. - current directory
#.. - parent directory

#from MyPackage.compressed import bzipped, gzipped #Absolute import
import os
extension_map={
    "gz":gzipped.opener,
    "bz2":bzipped.opener,
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1] # extension
        opener = extension_map.get(extension, open) # if extension matches .gz | .bz2 respective opener else return open
        self._filename = filename
        self.f = opener(self._filename, "rt", errors="ignore")

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()

