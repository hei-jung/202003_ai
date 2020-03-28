def hanoi(n, f, t):
    if n==1:    return print(f"{f}번 기둥의 1번 원판을 {t}번 기둥에 옮긴다.")  # f에서 t로 1번 원판을 옮긴다.
    hanoi(n-1, f, 6-f-t)
    print(f"{f}번 기둥의 {n}번 원판을 {t}번 기둥에 옮긴다.")    # f에 있는 한개의 원판을 t로 옮긴다.
    hanoi(n-1, 6-f-t, t)

hanoi(3,1,3)