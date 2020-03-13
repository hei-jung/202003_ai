"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']
"""
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
for i, item in enumerate(file):
    if '.' in file[i]:
        file_name = file[i].split('.')
        file_name.pop()
        # print(file_name)
        file[i] = ''.join(file_name)
print('file = {}'.format(file))
