import numpy as np

# 1-1. 대각선 diag() 추출 : 다차원 배열을 대각선으로 추출해서 일차원으로 리턴
ar = np.arange(9).reshape(3, 3)
print(ar)

print('ar의 대각선 값 : ')
res = np.diag(ar)
print(res)

# 1-2. 정수는 오른쪽 위쪽, 음수는 왼쪽 아래
print(np.diag(ar, k=1))
print(np.diag(ar, k=2))

print(np.diag(ar, k=-1))
print(np.diag(ar, k=-3))  # 값이 없음

# 2. np.diag 를 이용해서 대각선으로 객체 생성
a = np.array([10,20,30,40,50,60])
print(np.diag(a))
print(np.diag((10,20,30,40,50,60))) #튜플
print(np.diag([10,20,30,40,50,60])) #배열

# 3. 대각선 생성 전용 함수 : np.identity(크기, 형식) 사용 / 비교
print(np.identity(5, int))  # 대각선의 크기 지정, 값은 1로 채운다

# 4. 대각선 생성 전용 함수2 : np.eye(행 크기, 열 크기, 시작 위치)
# k = 1는 시작 위치, M 은 열의 크기
print(np.eye(5, k=1, M=3))


