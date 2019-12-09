# https://atcoder.jp/contests/abc104/tasks/abc104_c

D, G = map(int, input().split())

p = []
c = []

for d in range(D):
    p_i, c_i = map(int, input().split())
    p.append(p_i)
    c.append(c_i)

def dfs(i, total_score, completed_amount, total_completed):
    if total_score >= G:
        total_completed.append(completed_amount)
        return
    
    if i == 1:
        return

    # 完全に解く(100i 点の問題を pi 問解く)場合
    dfs(i-1, total_score + 100*(i) * p[i] + c[i], completed_amount+p[i], total_completed)

    # 1問も解かない場合
    dfs(i-1, total_score, completed_amount, total_completed)

    '''
    # 中途半端に解く(100i 点の問題を 1 問以上 pi − 1 問以下解く)場合
    for j in range(p[i]-1):
        dfs(i, total_score + 100*(i+1), completed_amount + 1, total_completed)
    '''


total_completed = []
dfs(D, 0, 0, total_completed)
ans = min(total_completed)

