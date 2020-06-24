# https://atcoder.jp/contests/abc068/tasks/abc068_b
input = int(input())

# １～受け取った数字までの連番のリストを作成
# range(start, stop) -> start <= x < stopまでの連番作成であることに注意
input_list = list(range(1, input + 1))

# input_listのそれぞれの要素と2で割れる回数をセットで格納するリスト
count_list = []

# input_listのそれぞれの要素が2で何回割れるか -> count_listに結果を格納
for e in input_list:
    count = 0
    e_tmp = e
    while True:
        if e_tmp % 2 == 0:
            e_tmp = e_tmp/2
            count += 1
        else:
            break
    count_list.append([e, count])

# 2で割れる回数の最大値
max_value = 0

# 2で割れる回数が最大である要素
max_key = 0

for i in range(input):    
    curr_value = int(count_list[i][1])
    if curr_value >= max_value:
        max_value = curr_value
        max_key = count_list[i][0]
    
print(max_key)


#print(max(count_list))