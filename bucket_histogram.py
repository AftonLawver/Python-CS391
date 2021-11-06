import random

def in_bucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count += 1
    return count

# This function creates a list of 1000 float values that are between 0 and 1.
def random_list(n):
    s = [0] * n  # creates the list with n number of zeros in it
    for i in range(n):
        s[i] = random.random()
    return s

t = random_list(10000)
num_buckets = 8
buckets = [0] * num_buckets
bucket_width = 1.0 / num_buckets
for i in range(num_buckets):
    low = i * bucket_width
    high = low + bucket_width
    buckets[i] = in_bucket(t, low, high)
print(buckets)
