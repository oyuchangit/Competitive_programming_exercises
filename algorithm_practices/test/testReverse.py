N = 10000


def convert_reversenum(num):

    if num < 0:
        return False

    if num % 10 == 0:
        return False

    errs = set()
    errs = {'3', '4', '7'}
    num_txt = str(num)
    num_txt_list = list(num_txt)
    num_len = len(num_txt)

    for i in range(num_len):

        if num_txt_list[i] in errs:
            return False

        if num_txt_list[i] == '6':
            num_txt_list[i] = '9'

        elif num_txt_list[i] == '9':
            num_txt_list[i] = '6'

    return_num_txt_list = reversed(num_txt_list)
    return int(''.join(return_num_txt_list))

rev_pair = []

for i in range(N):
    for j in range(i, N):

        ans = i + j

        rev_i = convert_reversenum(i)
        if rev_i == False:
            continue

        rev_j = convert_reversenum(j)
        if rev_j == False:
            continue

        rev_ans = convert_reversenum(ans)
        if rev_ans == False:
            continue

        if rev_j + rev_i == rev_ans:
            rev_pair.append([i, j])
        
print(rev_pair)


