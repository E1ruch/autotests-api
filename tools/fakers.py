import time

def get_random_email() -> str:
    return f"test.{time.time()}@qa.com"

print(get_random_email())