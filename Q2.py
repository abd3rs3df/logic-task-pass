def solution(num):
    prim = []
    pri = True
    for i in range(2,num):
        for j in prim :
            if i%j == 0 :
                pri = False
                break
            else:
                pri = True
        if pri :
            prim.append(i)

    return prim

print(solution(100))