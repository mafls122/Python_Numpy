import numpy as np

# unravel_index(indices, shape, order='C')

a_2d = np.array([[20,50,30],[60,40,10]])
print(a_2d)
print(np.argmax(a_2d))  # 일차원으로 나열해서 해당 인덱스 번호를 리턴

idx = np.unravel_index(np.argmax(a_2d), a_2d.shape)  # 2차원의 인덱스 번호 리턴
print(idx)
print(a_2d[idx])  # 최고(max) 인덱스 값

# np.where()로 리턴 받아보기
print(np.where(a_2d == np.max(a_2d)))

print(list(zip( *np.where(a_2d == np.max(a_2d)) )))  # *은 오픈, zip으로 묶어서 가져온다
print(list(zip( *np.where(a_2d == np.min(a_2d)) )))
