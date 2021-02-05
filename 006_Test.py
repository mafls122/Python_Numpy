import numpy as np

''' sample.csv --
1,2,3,4
11,12,100,120
21,,13,24
31,23,,34
'''

# 코드의 실행 결과를 생각해보자.

# 1.
a = np.genfromtxt('sample.csv', delimiter=',')
print(a)

# 2.
print(np.isnan(a))
print(~np.isnan(a))

# 3.
print( a[~np.isnan(a)] )  # 결손치가 아닌 값을 일차원으로 리턴
print( a[np.isnan(a)] )  # 결손치 값만 일차원으로 리턴

# 4.
print(np.nanmax(a))
r = np.nan_to_num(a, nan = np.nanmax(a))
print(r)

# 5.
r2 = np.nan_to_num(a, nan = (a - 119))
print(r2)