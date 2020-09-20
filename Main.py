from numpy import random
import Service
import time

# input = [-9, -2, 0, 2, 3]
# input = [-11, -10, -9, -2, 0, 2, 3, 66, 88]
input = [random.randint(-1000,1000) for _ in range(1_000)]

output1 = []
output2 = []

tic1 = time.perf_counter()
output1 = Service.run(input)
toc1 = time.perf_counter()

tic2 = time.perf_counter()
output2 = Service.runInOnePass(input)
toc2 = time.perf_counter()

print(f"Elapsed time 1 tic/toc {toc1 - tic1:0.4f} seconds")
print(f"Elapsed time 2 tic/toc {toc2 - tic2:0.4f} seconds")

# print ("Input = ", input)
# print ("Output 1 = ", output1)
# print ("Output 2 = ", output2)