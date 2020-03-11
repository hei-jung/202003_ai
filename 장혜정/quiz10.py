"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""
def factorial(num):
    n = 1
    for i in range(num):
        n = n * (num-i)
    print(n)

num = int(input('숫자를 입력하시오 : '))
factorial(num)
