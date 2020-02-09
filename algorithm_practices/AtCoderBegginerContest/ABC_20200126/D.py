H = int(input())

count = 0
while True:
    if H != 1:
        H = H // 2
        count += 1
    else:
        break

final_monster_num = 2 ** count
ans = final_monster_num * 2 - 1 

print(ans)