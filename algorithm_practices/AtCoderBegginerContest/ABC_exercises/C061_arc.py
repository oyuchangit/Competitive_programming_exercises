# https://atcoder.jp/contests/arc061/tasks/arc061_a

S = input()
def dfs(i, formula, ans_formula):
    # ベースケース
    if i == len(formula):
        ans_formula.append(formula)
        return 

    # +を入れる場合
    dfs(i+2, formula[:i] + '+' + formula[i:], ans_formula)
    
    # +を入れない場合
    dfs(i+1, formula, ans_formula)

ans_formula = []
dfs(1, S, ans_formula)

ans = 0
for i in range(len(ans_formula)):
    ans += sum(list(map(int, ans_formula[i].split('+'))))

print(ans)