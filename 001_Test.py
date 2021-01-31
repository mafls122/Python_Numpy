import numpy as np

# test) 지정된 배열값을 변경해 보자
a = np.arange(6).reshape(2,3)
print(a)

b = np.zeros_like(a)
print(b)

# 슬라이스를 이용해서 값 변경 -> [ : , : ] 앞에는 행, 뒤에는 열
a[ : , : ] = 10
print(a)