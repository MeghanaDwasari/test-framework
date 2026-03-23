import random

def generate_email():
    return f"user{random.randint(1000,9999)}@test.com"

def generate_name():
    return f"user{random.randint(100,999)}"