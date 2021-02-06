import numpy as np

# 1. csv 파일 로드 : np.loadtxt()
a = np.loadtxt('sample.csv', delimiter=',', dtype=str)  # ndarray로 반환, 기본 float의 dtype
print(a, '\n', type(a))
print(a.dtype, a.shape)

# 2. csv 파일 로드 : skoprows, usecols
# sample.csv 파일을 로드하고 1행 건너띄고 1,2,3,4 열을 로드한다.
b = np.loadtxt('sample.csv', delimiter=',', skiprows=1, usecols=[1,2,3,4])
print(b, '\n', type(b))
print(b.dtype, b.shape)

# 3. csv 파일 저장 : np.savetxt()
c = np.arange(1, 11).reshape(2, 5)
np.savetxt('sample_save.csv', c, fmt='%3d', delimiter=',')  # %.2f , %.5e 등등.. 포맷형식
