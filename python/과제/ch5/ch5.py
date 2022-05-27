def compact(src):
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

a = 'acddbcceeffffaaegg'
print(compact(a))