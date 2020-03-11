"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
N = int(input('N의 값을 입력하시오 : '))

for i in range(9):
    print('{} X {} = {}'.format(N, i+1, N*(i+1)))
