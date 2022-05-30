def compact(src):
    if src == '':
        return ''
    tmp = src[0]
    cnt = 1
    result = ''
    for i in src[1:]:
        if tmp == i:
            cnt += 1
        else:
            result += tmp + str(cnt)
            tmp = i
            cnt = 1
    result += tmp + str(cnt)
    return result

src = 'aaaabbb'
print("src = '{}'".format(src))
print("output = '{}'".format(compact(src)))

src = 'aaaabccccaaaaacccfg'
print("src = '{}'".format(src))
print("output = '{}'".format(compact(src)))

src = ''
print("src = '{}'".format(src))
print("output = '{}'".format(compact(src)))

src = 'a'
print("src = '{}'".format(src))
print("output = '{}'".format(compact(src)))