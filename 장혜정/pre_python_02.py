""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""
num1 = float(input('첫번째 수를 입력하시오 : '))
num2 = float(input('두번째 수를 입력하시오 : '))
op = input('연산기호를 입력하시오(+, -, *, /) : ')

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
