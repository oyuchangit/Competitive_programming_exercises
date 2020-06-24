# https://atcoder.jp/contests/arc061/tasks/arc061_a

S = input()
def dfs(i, formula, ans_formula_list):
    # ベースケース
    if i == len(formula):
        ans_formula_list.append(formula)
        return 

    # +を入れる場合
    dfs(i+2, formula[:i] + '+' + formula[i:], ans_formula_list)
    
    # +を入れない場合
    dfs(i+1, formula, ans_formula_list)

ans_formula_list = []
dfs(1, S, ans_formula_list)

ans = 0
for i in range(len(ans_formula_list)):
    ans += sum(list(map(int, ans_formula_list[i].split('+'))))

print(ans)