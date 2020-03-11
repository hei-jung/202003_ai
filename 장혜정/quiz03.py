"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
import random

def dice():
    diceNum = random.randint(1,6)
    print('{}입니다.'.format(diceNum))
    return diceNum

input('[user1] Enter 키를 누르면 주사위가 실행됩니다... ')
user1 = dice()

input('[user2] Enter 키를 누르면 주사위가 실행됩니다... ')
user2 = dice()

if user1 > user2:
    result = 'user1이 이겼습니다'
elif user1 < user2:
    result = 'user2가 이겼습니다'
else:
    result = '비겼습니다'


print('''user1: {}, user2: {}
{}.'''.format(user1, user2, result))
