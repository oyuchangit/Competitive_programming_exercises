# K = int(input())

# lun_n = 0
# lun_t = '0'

# def meke_next_lun(n):
#     n_t = str(n)
#     len_n = len(n_t)

#     if len(set(n_t)) == 1:
#         return n + 1


#     for i in reversed(range(1, n_t)):
        
#         right = int(n_t[i])
#         left = int(n_t[i-1])

#         if right <= left:
#             n_t[i] = (right + 1)

#             return int(n_t)

#     n_t[0] = int(n_t[0]) + 1
    
#     if len_n >= 2:
#         for i in range(1, n_t):
#             n_t[i] = n_t[0] + 1

#     return int(n_t)



# for _ in range(K):
#     lun_n = meke_next_lun(lun_n)
    




# 未完