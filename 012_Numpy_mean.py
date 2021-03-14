import numpy as np

jua = [1, 2, 3, 4, 5]

print("평균 : ", np.mean(jua))

# 분산 : 통계에서 평균으로부터 떨어져 있는 정도를 말하며 평균을 뺀 후 제곱하고 전체의 갯수로 나눈 값
print("분산 : ", np.var(jua))

# 표준편차 : 분산을 제곱근으로 계산한 값으로 클수록 평균에서 많이 떨어진 값이다.
print("표준편차 : ", np.std(jua))