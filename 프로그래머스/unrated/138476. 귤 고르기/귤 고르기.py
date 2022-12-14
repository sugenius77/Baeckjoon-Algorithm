from collections import Counter
def solution(k, tangerine):
    answer = 0
    type = 0
    count = Counter(tangerine)
    new_list = sorted(list(count.items()), key = lambda x:x[1], reverse = True)
    
    for i in new_list:
        k -= i[1]
        if k == 0:
            type += 1
            break
        if k < 0:
            type += 1
            break
        else:
            type += 1
    return type