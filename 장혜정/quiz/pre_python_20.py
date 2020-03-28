"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고,
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""
for num in range(1,101):
    myNum = num
    if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
        myNum = '짝'
    elif num // 10 == 3 or num // 10 == 6 or num // 10 == 9:
        myNum = '짝'
    elif num % 5 == 0:
        myNum = '아자'
    print(myNum)
