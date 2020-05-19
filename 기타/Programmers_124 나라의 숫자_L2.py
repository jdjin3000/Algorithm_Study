def solution(N):
    third = ""
    
    while N >= 3:
        q, r = divmod(N, 3)
        third += str(r)
        N = q
    
    third += str(N)

    third = list(map(int, list(third[::-1])))

    while 0 in third:
        for i in range(len(third) - 1):
            if third[i+1] == 0:
                third[i] -= 1
                third[i+1] = 3
        
        for i in range(len(third)):
            if third[0] != 0:
                break
            del third[0]

    third = str(int("".join(map(str, third))))
    third = third.replace('3', '4')

    answer = third
    return answer