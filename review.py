# Review 1
def add_to_list(value, my_list=[]):
    # Should de-reference the returned list from input
    # Should check if value is none
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # Wrong formating, should use .format()
    return "Hello, my name is {name} and I am {age} years old."

# Review 3
class Counter:
    count = 0

    def __init__(self):
        # Init method does not increase count
        # Will always return 1 for Counter instances
        # Should create dedicated count method for increment
        self.count += 1

    def get_count(self):
        return self.count


# Review 4
import threading

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Review 5
def count_occurrences(lst):
    # Input type is unknown, safe to parse to string when indexing
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1 # += 1
        else:
            counts[item] = 1
    return counts
