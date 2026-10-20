# @author Jakub Kijek
# @date 2026.10.20

def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a: int, b: int):
    return a * b // gcd(a, b)

print("gcd(36, 48):", gcd(36, 48))
print("lcm(12, 8): ", lcm(12, 8))

