# Prime number checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Worker function for threads
def prime_worker(start, end, result):
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []
    step = (end - start + 1) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step - 1 if i < num_threads - 1 else end
        thread = threading.Thread(target=prime_worker, args=(sub_start, sub_end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted(result)

# Example usage
import threading

# Oddiy tub son tekshirish funksiyasi
def __name__(n):
    if __name__ == "__main__":
        primes = threaded_prime_checker(1, 100, num_threads=4)
    print("Prime numbers:", primes)
import threading
from collections import Counter

# Worker function to count words
def word_count_worker(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)

def threaded_word_count(filename, num_threads=4):
    # Read file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

# Split lines between threads
step = len(lines) // num_threads
threads = []
counters = []

for i in range(num_threads):
        sub_lines = lines[i*step : (i+1)*step] if i < num_threads - 1 else lines[i*step:]
        thread = threading.Thread(target=word_count_worker, args=(sub_lines, counters))
        threads.append(thread)
        thread.start()

for thread in threads:
        thread.join()

# Merge results
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    return total_counter

# Example usage
if __name__ == "__main__":
    filename = "sample.txt"  # o‘zing fayl nomini yoz
    result = threaded_word_count(filename, num_threads=4)
    print("Word occurrences:\n", result.most_common(10))

