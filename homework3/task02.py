import time
import struct
import random
import hashlib
from multiprocessing import Pool

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

def calculate_total_sum():
    # Define the number of processes to use
    num_processes = 4

    # Create a Pool of processes
    pool = Pool(processes=num_processes)

    # Generate a list of numbers from 0 to 500
    numbers = list(range(501))

    # Use multiprocessing to calculate the sums in parallel
    results = pool.map(slow_calculate, numbers)

    # Calculate the total sum
    total_sum = sum(results)

    # Close the pool of processes
    pool.close()
    pool.join()

    return total_sum

# Calculate the total sum using multiprocessing
total_sum = calculate_total_sum()
print(total_sum)