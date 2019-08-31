from module import rishi_math as rm
import time

start_time = time.time()
print(rm.factorial_rec(500))
end_time_rec = time.time() - start_time
print(f'Factorial Recursion runtime = {end_time_rec}')

start_time = time.time()
print(rm.factorial(500))
end_time = time.time() - start_time
print(f'Factorial Recursion runtime = {end_time}')

print((end_time_rec - end_time) / end_time_rec * 100)