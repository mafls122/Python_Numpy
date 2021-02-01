import numpy as np

# 1-1. linspace (start, end, 분할 갯수, retstep, dtype)
# 1에서 10까지 5등분 하기
print(np.linspace(1, 10, 5))

# 1-2. start > stop 관계 (역순)
print(np.linspace(10, 0, 5, dtype = int))

# 1-3. endpoint = False : 0(end)을 포함하지 않고 5등분 하기, retstep 튜플로 반환
print(np.linspace(10, 0, 5, endpoint=False, dtype=int, retstep=True))

# 2. arange([start,] stop[, step,], dtype=None)
print(np.arange(3, 10, 2))
print(np.arange(10, 3, -2))

# 3. 역순으로 변환 arange(), [::-1], flip()
print(np.arange(3, 10, 2)[::-1])
print('flip 사용하여 역순으로 변경 : ')
print(np.flip(np.arange(3, 10, 2)))  # flip 괄호 안에는 무조건 배열값이 들어가야함

# 4. 다차원으로 변환 채우기
# 2d 3d = 다차원 배열로 등차 수열을 생성한다. reshape()
print(np.arange(12).reshape(3, 4))  # 1씩 증가값을 3행 4열로 다차원 변환
print(np.linspace(0, 10, 12, dtype=int).reshape(3, 4))  # 균등 분할값을 3행 4열로 다차원 변환

'''
 값 채우기
 
1. 요소 수를 지정해서 채우기
    linspace(start, end)
    
2. 주어진 숫자를 간격으로 채우기 (파이썬의 range()는 정수만, Numpy의 arange()는 정수+실수 가능)
    
    arange(end dtype) : 0 <= n < end (간격 1) , dtype도 명시 가능
    arange(start, end) : start <= n < end (간격 1)
    arange(start, end, step : start <= n < end (간격 step)
    
3. 역순으로 변환

4. 다차원으로 변환 채우기
'''