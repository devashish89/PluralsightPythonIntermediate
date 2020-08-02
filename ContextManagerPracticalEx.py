import sys
import contextlib
import time

class Transaction:
    def __init__(self,txid):
        self.txid = txid

    def commit(self):
        print(f"Transaction: {self.txid} is committed")

    def rollback(self):
        print(f"Transaction: {self.txid} is rolled back")


class DatabaseEntry:

    def __init__(self,conn, txn):
        self.conn = conn
        self.txn = txn

    def dbconnection(self):
        return True if self.conn == "Oracle" else False

    def __enter__(self):
        if self.dbconnection() == True:
            print("Database connection successful")
        else:
            raise ConnectionError("Database connection failed")
        return self


    def processTransaction(self):
        if  isinstance(self.txn.txid, int):
            print("Transaction is successful")
        else:
            raise ValueError(f"Transaction Id: {self.txn.txid} has to be numeric")

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is None:
            self.txn.commit()

        else:
            self.txn.rollback()

print("."*20)

txn1 = Transaction(1)
with DatabaseEntry("Oracle", txn1) as f:
    f.processTransaction()

print("."*20)
time.sleep(2)

txn1 = Transaction("h")
with DatabaseEntry("Oracle", txn1) as f:
    try:
        f.processTransaction()
    except Exception:
        print("Error: {}".format(sys.exc_info()))

print("."*20)
time.sleep(2)

with DatabaseEntry("SQL", txn1) as f:
    f.processTransaction()




