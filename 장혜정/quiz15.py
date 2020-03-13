"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오.
(리스트 split 과 슬라이싱 활용) """
id = input('주민등록번호를 입력하시오 > ')
num_id = id[6:]
if num_id[0] == '1' or num_id[0] == '3':
    gender = '남자'
elif num_id[0] == '2' or num_id[0] == '4':
    gender = '여자'
print('성별은 {}입니다.'.format(gender))
