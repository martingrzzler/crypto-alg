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

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a


def gen_e(n, phi_n):
	for e in range(2, phi_n):
		if gcd(e, n) == 1 and gcd(e, phi_n) == 1:
			return e

def gen_d(e, phi_n):
	for d in range(2, phi_n):
		if d*e % phi_n == 1:
			return d

# depending on n this function may take many year
def phi(n):
	res = 1
	for i in range(2, n):
		if (gcd(i, n) == 1):
			res+=1
	return res

# General formula
# encryption -> m^e mod n = c
# decryption -> c^d mod n = m
# (m^e)^d mod N = m; m^(e*d) mod N = m
# How to solve for D?
# Use Euler's Theorem -> m^phi(n) congruent 1 (mod n)
# 1^k=1 hence m^(k*phi(n)) congruent 1 (mod n)
# 1*m = m hence m*m^(k*phi(n)) congruent m (mod n) -> m^(k*phi(n)+1) congruent m (mod n)
# So m^(k*phi(n)+1) congruent m (mod n)
#    m^(e*d)        congruent m (mod n)
# So d = (k*phi(n)+1)/e 
# How to get k? Well k can take on infinite values such that d is an integer
# There is another relationship d*e=(k*phi(n)+1) is really just: d*e mod phi(i) = 1



# Generate two distinct primes
p = rand_prime(1000)
q = rand_prime(1000)

print(f"Primes p={p}, q={q}")

# compute n
n = p * q
print(f"n={n}")

# compute phi(n) - totient function
# phi(p)=p-1 for every prime number p 
phi_n = (p - 1) * (q - 1)
print(f"phi(n)={phi_n}")

# generate e which must be { 1 < e < phi(n) } and coprime (gcd(a, b) == 1) to n and phi(n)
e = gen_e(n, phi_n)
print(f"e={e}")

# generate d; see explanation above
#  d can be computed efficiently by using the extended Euclidean algorithm
d = gen_d(e, phi_n)
print(f"d={d}")

# Alice and Bob
print(f"Alice Public Key: ({e},{n})")
print(f"Alice Private Key: ({d})")

# Bob 
m = 123
c = m**e % n
print(f"Bob's message: {m}")
print(f"Bob's cipher: {c}")

# Alice
dm = c**d % n
print(f"Alice decrypts cipher to: {dm}")

# Eve Attack
# If you encrypt a message byte by byte you may reveal the key through frequency analasys, so randomness is required
# Eve has the cipher and the public key
bf_phi_n = phi(n)
print(f"Eve calculates phi(n)={phi(n)}")
# hack d
hacked_d = gen_d(e, bf_phi_n)
print(f"Eve has the private key: d={hacked_d}")

# Signing test
document = 444
signature = (document ** d) % n

verified_document = (signature ** e) % n
print(f"Alice's document: {document}")
print(f"The signature: {signature}")
print(f"Bob verifies signature with public key: {verified_document}")


