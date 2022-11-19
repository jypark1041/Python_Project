#문제> 곱하기 혹은 더하기
#큰 수를 곱하면 큰 값이 나옴 단, 0과 1 제외(이땐 +가 효율적)

S = input()

result = int(S[0])


for i in range(1, len(S)):
    num = int(S[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num


print(result)


