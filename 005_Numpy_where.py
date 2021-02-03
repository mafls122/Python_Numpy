import numpy as np

# 조건 처리 : numpy.where(condition, [x,y])  & |

ar = np.arange(9).reshape(3,3)
print(ar)

# 1. ar이 5보다 작으면 0, 그렇지 않으면 999 값으로 채우자
ar = np.where(ar < 5, 0, 999)
print(ar)

# 2-1. 6개의 순차 배열값을 만들고 3보다 작은 값들을 추출해서 튜플로 리턴
ar2 = np.arange(6)
print(ar2)

print(np.where(ar2 < 3))
print(list(zip(*np.where(ar2 < 3))))

# 2-2. 리스트로 리턴
print(np.where(ar2 < 3)[0])
print(np.where(ar2 < 3)[0].tolist())
