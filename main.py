### NumCruncher
from mpmath import mp
def gcd(x, y, d):
 mp.dps = d
 r = mp.mpf(x % y)
 x = mp.mpf(y)
 y = mp.mpf(r)
 r = mp.mpf(x % y)
 x = mp.mpf(y)
 y = mp.mpf(r)
 return mp.mpf(y)
def sqrt(x, d, g=1.0):
 mp.dps = d
 for i in range(0, 10):
  g = mp.mpf(g + x / g) / 2
 return str(mp.mpf(g))
def prime(x):
 is_prime = [True] * (x + 1)
 is_prime[0] = is_prime[1] = False
 for i in range(2, int(x**0.5) + 1):
  if is_prime[i]:
   for j in range(i * i, x + 1, i):
    is_prime[j] = False
 return [i for i in range(2, x + 1) if is_prime[i]]
print("Welcome to Num-Cruncher!")
choice = input("Enter choice: ")
if choice == "gcd":
    n = int(input("Enter a number: "))
    n1 = int(input("Enter a 2nd number: "))
    n2 = int(input("Enter digits: "))
    print(f"GCD = {gcd(n, n1, n2)}")
if choice == "sqrt":
 n = int(input("Enter number: "))
 d = int(input("Enter digits: "))
 print(f"sqrt = {sqrt(n, d)}")
if choice == "primes":
 n = int(input("Enter limit: "))
 print(f"primes = {prime(n)}") 