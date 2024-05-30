# Review 1
def add_to_list(value, my_list=[]):
    # Should check if value is none
    if value is not None:
        my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # Wrong formating syntax, should use .format()
    # Using empty placeholder to reduce code length
    return "Hello, my name is {} and I am {} years old.".format(name, age)

# Review 3
class Counter:
    # No need to declare value as it will be created in __init__

    def __init__(self):
        # Should not do increment in init method
        # Should declare initial value (0) in __init__
        self.count = 0

    # Should create dedicated increment method for counter to function
    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


# Review 4
import threading

class SafeCounter:
    # Implementation is not safe for threads as the same counter object will be shared with all threads
    def __init__(self):
        self.count = 0
        # Need to use lock to eliminate race conditions
        self.lock = threading.Lock()

    def increment(self):
        # Need to acquire lock for increments
        with self.lock:
            self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

# Should have name guard for executable codes
if __name__ == "__main__":
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
    counts = {}
    for item in lst:
        # List items could have mixed types, safe to parse to string for dict indexing
        index = str(item)
        if index in counts:
            # Wrong syntax for increment with =+ 1
            counts[index] += 1
        else:
            counts[index] = 1
    return counts
