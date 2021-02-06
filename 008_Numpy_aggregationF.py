import numpy as np

# 행과 열의 집계 함수 : 합계 sum, 평균 mean, 최대 max, 최소 min, clip, 표준편차 std, 분산 var
a = np.arange(1, 11).reshape(2, 5)
print(a)

# 1. np.sum()
print(np.sum(a))
print(np.sum(a, axis=0))  # 열의 합계
print(np.sum(a, axis=1))  # 행의 합계
print('\n')

# 2. np.clip() / ndarrau.clip() : 배열 요소의 값을 임의의 간격에 맞추어 처리
# 인수로 최소값, 최대값을 지정하게 되면 해당 범위에서 벗어나면 최소값, 최대값으로 대체된다.
# 0.0 ~ 1.0 / 0 ~ 255
print( np.clip(a, 2, 7) )  # 최소2, 최대7
print( np.clip(a,None,7))  # 최소 없음 최대 7 -> 매개인수가 필수로 3개 지정

print(a.clip(2))  # 최소 2로 자동 입력
print(a.clip(min=2)) # 키워드로 지정 가능 min, max
print(a.clip(max=8))
print('\n')

# 3. np.argmax(), np.argmin() : ndarray의 최대, 최소 '인덱스'를 리턴
print(a)
print(np.argmax(a))
print(np.argmin(a))

# 4. np.max() : 최대값, np.min() : 최소값, np.mean() : 평균값 출력
print(np.max(a))
print(np.min(a))
print(np.mean(a))




