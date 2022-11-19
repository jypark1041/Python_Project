#문제> 시각: 00시00분00초 부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
# 3이 있는지 없는지 확인, 배열..?

#N 입력 받기
n = int(input())

count = 0
for i in range(n+1):  #시
    for j in range(60):   #분
        for k in range(60):    #초
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


