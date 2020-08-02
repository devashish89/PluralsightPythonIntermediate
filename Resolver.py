import socket
class Resolver:
    def __init__(self):
        self._cache = dict()


    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
            return self._cache[host]

    def clearCache(self):
        self._cache.clear()

    def has_host(self, host):
        if host in self._cache.keys():
            return True
        else:
            return False



