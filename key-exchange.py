from distutils.log import error
import math
import random

def is_prime(p):
	for i in range(2, math.isqrt(p) + 1):
		if p % i == 0:
			return False
	return True

def rand_prime(start: int):

	while True:
		p = random.randrange(start, 2*start)
		if is_prime(p):
			return p

def is_generator(g, p):
	for i in range(2, p - 1):
		if (g**i) % p == 1:
			return False
	return True

def get_generator(p):
	for g in range(2, p):
		if is_generator(g, p):
			return g

def make_generator(p):
	for g in range(2, p):
		s = set()
		is_gen = True
		for i in range(2, p):
			val = (g**i) % p
			if val in s:
				is_gen = False
				break
			s.add(val)
		if is_gen:
			return g


# Public
p = rand_prime(10000)
g = make_generator(p)
if g == None:
	raise error("No generator found")


print(f"p={p}, g={g}")

# Alice
a = random.randrange(0, p)
g_a = (g**a) % p

# Bob
b = random.randrange(0, p)
g_b = (g**b) % p

# Alice
alice_key = (g_b**a) % p

# Bob
bob_key = (g_a**b) % p

print(f"Alice's key: {alice_key}, Bob's key: {bob_key}")

# if p is big enough (more than 2000 bits) tham Eve than it's just infeasable for Eve to get either a or b
# it would take to much time to brute force







