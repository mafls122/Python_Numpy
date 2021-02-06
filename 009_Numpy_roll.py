import numpy as np

# ndarray 이동 작업 : roll(a, shift, axis=None)
a = np.arange(1, 11)
print(a)

# 1. np.roll()을 사용하여 배열 이동시키기
a_roll = np.roll(a, 3)  # 3칸 오른쪽으로 이동
print(a_roll)

# 2-1. 다차원 배열 행 이동
a_2d = np.arange(12).reshape(3, 4)
print(a_2d)

print(np.roll(a_2d, 2))

# 2-2. 열을 하나 오른쪽으로 이동
print(np.roll(a_2d, 1, axis=0))

# 2-3. 행과 열 동시에 이동, 축도 지정할 수 있음
print(np.roll(a_2d, (1, 2), axis=(0, 1)))