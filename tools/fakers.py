import time

counter = 0

def get_random_email() -> str:
    return f"test.{time.time()}@qa.com"

def get_random_name() -> str:
    global counter
    counter += 1
    return f"user{counter}"

print(get_random_email())
print(get_random_name())