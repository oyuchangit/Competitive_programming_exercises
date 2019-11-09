###############################################
#### zip
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18




###############################################
#### set
#### sortedでソート可能
l = [1, 2, 2, 3, 1, 4]

print(l)
print(type(l))
# [1, 2, 2, 3, 1, 4]
# <class 'list'>

s_l = set(l)

print(s_l)
print(type(s_l))
# {1, 2, 3, 4}
# <class 'set'>




###############################################
#### sorted
#### 新規でリストを作成して返却する
#### 辞書(dict)のキーのソートやsetのソートにも使える
d = {'c': 10, 'b':1, 'a':30}
# sorted(d)   #ソートされたキーのリストを返す
# ['a', 'b', 'c']

d = set([3,1,2])

# d
# set([1, 2, 3])

# sorted(d)
# [1, 2, 3]
