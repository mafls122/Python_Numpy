import numpy as np

# 기본 list (데이터 형식)
ar = [1,2,3,4,5]
print(ar, type(ar))  # [1, 2, 3, 4, 5] <class 'list'>

# ndarray는 데이터형식 dtype, np.array()를 통해서 ndarray 객체를 생성
a = np.array([1,2,3], dtype=np.int64)  # dtype 으로 지정 (== dtype='int64')
print(a)   # [1 2 3]
print(a.dtype)  # int64
print(type(a))  # <class 'numpy.ndarray'>

# 1. 행과 열의 수를 지정해서 생성

print(np.zeros([2, 2, 3], dtype=np.int))  #정수 타입으로 지정, 배열 값을 모두 0으로 지정
print(np.ones([2, 2, 3], dtype='float'))  #실수 타입으로 지정, 배열 값을 모두 1으로 지정

# 2. 임의로 값으로 데이터 채우기  numpy.full(shape, fill_value)

print(np.full(3, 100))   # 배열 갯수 3개, 값 100으로 지정
print(np.full((2,3), np.pi)) # 2,3 배열 생성, 값 : pi
print(np.full((2,3), np.pi, dtype=np.int)) # dtype을 int로 변경, 기본 dtype값은 float

# 3. 기존의 배열 형식으로 값을 대입하여 생성
a = np.arange(4).reshape((2, 2))
print(a)

b = np.zeros_like(a)  # 기존 배열 값을 0으로 대입 후 생성, dtype도 변경가능, np.ones_like(), np.full_like() 도 있다.
print(b)


# test) 지정된 배열값을 변경해 보자

a = np.arange(6).reshape(2,3)
print(a)

b = np.zeros_like(a)
print(b)

# 슬라이스를 이용해서 값을 변경해 보자
a[ : , : ] = 0 #앞에는 행 뒤에는 열
print(a)

a = a.astype(np.float)  #dtype float로 변경, int,str도 가능
a[:] = 1.0
print(a)   #원래 a의 dtype이 정수여서 정수로 나옴 dtype값을 바꿔줘야함!



