"""11. 최대공약수를 구하는 함수를 구현하시오"""
def gcd():
    a = int(input('a : '))
    b = int(input('b : '))
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
        if r == 0:
            return b

my_gcd = gcd()
print(my_gcd)
