# N体のモンスター, K回まで必殺技が使える
N, K = map(int, input().split())

# モンスターの体力 高い順
H_list = list(map(int, input().split()))
H_list = sorted(H_list, reverse=True)

# K番目のモンスターまでは必殺技で殺す
H_list = H_list[K:]

# 残りのモンスターのHP数を合計する
HP_sum = sum(H_list)

print(HP_sum)