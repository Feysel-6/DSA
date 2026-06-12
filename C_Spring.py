import math

def get_lcm(x, y):
    if x == 0 or y == 0: return 0
    return abs(x * y) // math.gcd(x, y)

t = int(input())
for _ in range(t):
    a, b, c, m = map(int, input().split())
    na = m // a
    nb = m // b
    nc = m // c
    
    nab = m // get_lcm(a, b)
    nbc = m // get_lcm(b, c)
    nac = m // get_lcm(a, c)
    
    nabc = m // get_lcm(a, get_lcm(b, c))
    
    alice = 6*(na - nab - nac + nabc) + 3*(nab - nabc) + 3*(nac - nabc) + 2*(nabc)
    bob   = 6*(nb - nab - nbc + nabc) + 3*(nab - nabc) + 3*(nbc - nabc) + 2*(nabc)
    carlo = 6*(nc - nac - nbc + nabc) + 3*(nac - nabc) + 3*(nbc - nabc) + 2*(nabc)

    print(int(alice), int(bob), int(carlo))