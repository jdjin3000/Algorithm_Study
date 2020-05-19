def solution(N):
    third = ""
    
    while N >= 3:
        third += str(N%3)
        N = N//3
    
    third += str(N)

    third = list(map(int, list(third[::-1])))
    print(third)

    while 0 in third:
        for i in range(len(third) - 1):
            if third[i+1] == 0:
                third[i] -= 1
                third[i+1] = 3
    
    print(third)
    # third = str(int("".join(map(str, third))))
    # third = third.replace('2', '4')
    # third = third.replace('1', '2')
    # third = third.replace('0', '1')

    # answer = third
    # return answer

solution(21)