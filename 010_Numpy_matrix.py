import numpy as np

# 1. numpy.matrix() : 행렬 객체 생성
mat = np.matrix([1,2,3,4,5,6])
print(type(mat))  # <class 'numpy.matrix'>
mat.shape

# 2. 전치 행렬 : .T
ar = np.arange(6).reshape(2,3)
print(ar)
print(ar.T)  # 행과 열이 바뀜

# 3. 행렬의 합, 차, 곱 : + - *
ar02 = np.arange(0,12,2).reshape(2,3)
print('\n',ar)
print('\n',ar02)

print('합-----')
print(ar + ar02)
print('차-----')
print(ar - ar02)

m01 = np.matrix(ar)
m02 = np.matrix(ar02)
print(m01 + m02)   # ndarray와 같이 연산 가능

# 4. 행렬의 곱 : numpy.dot(), numpy.matmul(), @연산자, *연산자  python ver 3.5이상 가능
ar01 = np.arange(4).reshape(2, 2)
print(ar01)
ar02 = np.arange(6).reshape(2, 3)
print(ar02, '\n')

# 4-1. np.multiply()
print(np.multiply(m01, m02))  # 곱, shape가 맞아야함

# 4-2. np.dot() : 행렬 곱셈
print(np.dot(ar01, ar02))  # 0 * 0 + 1 * 3  = 3  /  2 * 0 + 3 *3 = 9

a = np.array([1, 2])
# [ 1,2 ]
b = np.arange(4).reshape(2, 2)
# [[0 1]
#  [2 3]]
# -> 1 * 0 + 2 * 2 = 4  /  1 * 1 + 2 * 3 = 7
print('행렬곱셈 np.dot() : \n', np.dot(a,b))  # [ 4, 7 ]

# 4-3. @ 연산 사용 : 행렬 곱셈
print('@연산 : \n', ar01 @ ar02)

# 4-4. 거듭제곱 : **
print('거듭제곱 : \n', a ** b)