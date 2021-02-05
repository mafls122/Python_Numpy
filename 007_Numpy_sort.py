import numpy as np
'''
numpy.sort() : 정렬 후 ndarray로 리턴
ndarray.sort() : ndarray 자체 정렬
numpy.argsort() : 정렬된 인덱스의 배열을 ndarray로 리턴
'''

# 1. 일차원 배열 : np.sort()
a = np.array([3,4,5,6,2])
print(a)

# 1-1. 일차원 배열 정렬
a_sort = np.sort(a)
print("a_sort : ", a_sort)
print("a : ", a)  # a는 변경 안됨

# 1-1. 정렬 후 역순으로 슬라이싱
a_sort_reverse = np.sort(a)[::-1]
print(a_sort_reverse)

# 2. 다차원 배열 : np.sort()
a_2d = np.array([ [300,2,5],[5,10,43], [55,99,100] ])
print(a_2d)

# 2-1. 다차원 배열 열 정렬
a_2d_sort = np.sort(a_2d, axis =0)  # axis=0 : 열 , axis=1 : 행
print(a_2d_sort)

# 2-2. 다차원 배열 행 정렬
a_2d_sort = np.sort(a_2d, axis =1)  # axis=0 : 열 , axis=1 : 행
print(a_2d_sort)

# 2-3. 다차원 axis = -1 기준 정렬
a_2d_sort = np.sort(a_2d, axis =-1)  # axis=-1 : 마지막 축에 따라 정렬 (3차원은 면에 따라 정렬)
print(a_2d_sort)

# 2-4. 다차원 내림차순 정렬
a_2d_sort = np.sort(a_2d, axis =0)[::-1]
print(a_2d_sort)

a_2d_sort = np.sort(a_2d, axis =1)[:,::-1]
print(a_2d_sort)

# 3. ndarray.sort() 사용하여 ndarray 자체 정렬
# 3-1. 일차원 정렬
a = np.array([3,4,5,6,2])
a.sort()
print(a)

# 3-1. 다차원 정렬, 역정렬
a_2d.sort(axis=0)
print(a_2d)
print(a_2d[::-1])

# 4. numpy.argsort() 사용하여 정렬
a_2d = np.array([ [300,2,5],[5,10,43], [55,99,100] ])
print(a_2d)

# 4-1. 특정 열을 기준으로 정렬
col_num = 1
print(a_2d[:, col_num])  # 1열 출력
print(np.argsort(a_2d[:, col_num]))  # 1열을 기준으로 정렬

res = a_2d[np.argsort(a_2d[:, col_num])]  # 1열을 기준으로 정렬한 인덱스를 바탕으로 행을 정렬
print(res)

# 4-2. 특정 열을 기준으로 내림차순
print(np.argsort(a_2d[:, col_num][::-1]))  # 1열을 기준으로 역순 정렬한 인덱스
res = a_2d[np.argsort(a_2d[:, col_num][::-1])]  # 1열을 기준으로 정렬한 인덱스를 바탕으로 행을 역순 정렬
print(res)