# モンスターの体力H, トキの魔法N種類
H, N = map(int, input().split())

A_B_list= []
efficiency_list = []
for i in range(N):
    A, B = map(int, input().split())
    A_B_list.append([A, B])
    efficiency_list.append(A / B)



best_magic_index = efficiency_list.index(max(efficiency_list))
best_magic = A_B_list[best_magic_index]

at_least_attack_num = H // best_magic[0]
H = H - (at_least_attack_num * best_magic[0])


B_list = []

def dfs(H, i, B_sum):
    if H <= 0:
        B_list.append(B_sum)
        
    else:
        for A_B in A_B_list:
            dfs(H - A_B[0], i + 1, B_sum + A_B[1])

B_ = best_magic[1] * at_least_attack_num

dfs(H, 0, 0)
print(min(B_list) + B_)