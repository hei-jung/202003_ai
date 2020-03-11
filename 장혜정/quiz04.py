"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""
def area_triangle():
    base = int(input('가로의 숫자를 입력하시오 : '))
    height = int(input('높이의 숫자를 입력하시오 : '))
    area = base * height / 2
    print('삼각형의 넓이는 {} 입니다.'.format(area))

# area_triangle()
