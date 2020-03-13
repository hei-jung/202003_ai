"""16. 1부터 50 까지의 숫자 중에서 3의 배수를 공백으로 구분하여 출력하시오."""
for num in range(1, 51):
    if num % 3 == 0:
        print(num)
