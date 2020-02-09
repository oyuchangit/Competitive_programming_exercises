# A の末尾の桁が B の先頭の桁に等しく、 
# A の先頭の桁が B の末尾の桁に等しい

N = int(input())

count_handstand = 0
for A in range(1, N + 1):
    str_A = str(A)

    # Aの先頭の桁
    A_first = str_A[0]

    # Aの末尾の桁
    A_last = str_A[len(str_A)-1]

    # 生成したBがあり得るかどうか判定
    B_list = []
    if A_first == A_last:
        count_handstand += 1
    for i in range(2, len(str(N))+1):
        middle_len = i-2
        middle_str = '0' * middle_len
        B = int(A_first + middle_str + A_last)
        if B <= N and middle_len == 0:
            count_handstand += 1
        elif B <= N and middle_len != 0:
            count_handstand += middle_len * 10


print(count_handstand)