# https://atcoder.jp/contests/abc079/tasks/abc079_c

A_B_C_D = input()
plus = '+'
minus = '-'
right_side = '=7'
ans = ''

def dfs(i, formula, sum):
    # ベースケース
    if i == 7:
        if sum == 7:
            # global変数を使うなんてイケてないのでは？
            global ans 
            ans = formula + right_side        
        return
    
    # +を入れる場合
    dfs(i+2, formula[:i] + plus + formula[i:], sum + int(formula[i]))

    # -を入れる場合
    dfs(i+2, formula[:i] + minus + formula[i:], sum - int(formula[i]))

dfs(1, A_B_C_D, int(A_B_C_D[0]))

print(ans)