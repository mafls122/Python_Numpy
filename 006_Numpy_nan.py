import numpy as np

# 1. 결측값(NaN) 처리
# 1-1. np.nan
print(type(np.nan))  # <class 'float'>
print(np.nan == np.nan)  # 결손값끼리 == 비교연산시 -> False

# 1-2. np.isnan()
print(np.isnan(np.nan))  # isnan() 사용하여 비교 -> True
print(float('nan'), np.math.nan, np.math.isnan(np.nan))

# 2. np.genfromtxt -> 복잡한 서식이 있는 파일을 로드 및 결측값 처리
a = np.genfromtxt('sample.csv', delimiter=',')
print(a)  # 결측값 nan 표시됨
b = np.genfromtxt('sample.csv', delimiter=',', filling_values = 0)  # 인지하지 못하는 것들을 0으로 채움 : filling_values
print(b)

# 3-1. np.nan_to_num() : 결측값을 숫자로 변경
r = np.nan_to_num(a, nan = 10)  # 결측값이 있을 경우 10으로 대체
print(r)

# 3-2. np.nan_to_num() + 연산
print(np.nanmean(a))  # a의 평균값 계산
r2 = np.nan_to_num(a, nan = np.nanmean(a))  # 결측값을 np.nanmean(a)값으로 대체
print(r2)
# r2 = np.nan_to_num(a,nan = (a*10))  # 이 연산은 안됨! 주의
