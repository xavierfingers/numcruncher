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
