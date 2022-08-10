def solution(str,char):
    strList=''.join(list(set(list(str))))
    return len(str)-len(strList)+1

print(solution('aaaaaaab','a'))