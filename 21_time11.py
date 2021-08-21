"""
perf_counter:
-------------
    to finding the performance of executing time
    """
from time import perf_counter,sleep
start=perf_counter()
for i in range(8):
    print("hey")
    sleep(2)
end=perf_counter()
print("%.2f" %(end-start))
