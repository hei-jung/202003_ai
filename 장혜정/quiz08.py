"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오"""
integer = int(input('정수를 입력하시오 : '))

if integer == 0:
    print('0입니다.')
elif integer%2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')
