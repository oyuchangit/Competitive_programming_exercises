import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
a_list = list(map(int, input().split()))

count = 1
break_count = 0

for i in range(N):
    if a_list[i] == count:
        count += 1
    else:
        break_count += 1
    
if break_count == N:
    print(-1)
else:
    print(break_count)











# 以下コンテスト中のダメ回答

'''
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
a_list = list(map(int, input().split()))



isBreak_list = [False] * N
# 全探索i番目のレンガを壊すか壊さないかで再帰
def dfs(i, isBreak_list, a_list):
    # リストの長さまで決め終わったら判定する

    if i == N:
            
        dellist_index = []

        for x in range(N):
            if isBreak_list[x]:

                dellist_index.append(x)
        
        tmp_a_list = copy.copy(a_list)

        # for i in dellist_index:
        #     tmp_a_list[i] = ''
        # tmp_a_list = list(filter(lambda s:s != '', tmp_a_list))

        # dellist(tmp_a_list, dellist_index)


        for y in len(tmp_a_list):
            if y in dellist_index:
                tmp_a_list[y] = -2
                
        new = [i for i in tmp_a_list if i == -2]

        tmp_a_list_len = len(new)
        if tmp_a_list == range(1, tmp_a_list_len + 1):
            print(N - tmp_a_list_len)
            exit()
        
        return

    # i番目のレンガを壊す場合
    isBreak_list[i] = True
    dfs(i + 1, isBreak_list, a_list)

    # i番目のレンガを壊さない場合
    isBreak_list[i] = False
    dfs(i + 1, isBreak_list, a_list)

dfs(0, isBreak_list, a_list)
print(-1)
'''