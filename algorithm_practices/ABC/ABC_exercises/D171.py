# https://atcoder.jp/contests/abc171/tasks/abc171_d


N = int(input())

A_list = list(map(int, input().split()))    #整数列
Q = int(input())                            #操作の回数

B_list = []                                 #値がBである要素を
C_list = []                                 #全てCに置き換える

for i in range(Q):
    B, C = map(int, input().split())
    B_list.append(B)
    C_list.append(C)


curr_sum = 0
elements_num_dict = {}

for A in A_list:
    curr_sum += A

    if A in elements_num_dict:
        elements_num_dict[A] += 1
    else:
        elements_num_dict[A] = 1


for i, (B, C) in enumerate(zip(B_list, C_list)):

    if B in elements_num_dict:
        
        count = elements_num_dict[B]
        diff = C*count - B*count
        curr_sum += diff


        # 辞書配列を修正
        elements_num_dict[B] -= count

        if C in elements_num_dict:
            elements_num_dict[C] += count
        else:
            elements_num_dict[C] = count

    
    print(curr_sum)
