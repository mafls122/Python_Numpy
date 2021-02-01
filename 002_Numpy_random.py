import numpy as np

# 1-1. 일차원 3개의 난수
m_rand = np.random.rand(3)
print(m_rand)

# 1-2. 이차원 2,3개의 난수
m_rand = np.random.rand(2,3)
print(m_rand)

# 2-1. 일차원 3개의 난수
m_rand = np.random.sample(3)
print(m_rand)

# 2-2. 이차원 2,3개의 난수
m_rand = np.random.sample((2,3))
print(m_rand)

# 3. randint(최소값, 최대값, 형식, dtype) 을 사용하여 4 이상 10 이하의 3*3 배열의 객체 생성
ar = np.random.randint(4, 10, (3, 3))
print(ar)

# 4. 정규 분포 random.normal ( loc = 0.0, scale = 1.0, size = None)
# loc = 평균, scale = 정규 분포에 따른 난수
arr = np.random.normal(-2, 0.5, (3, 3))
print(arr)

'''
1. 균일 분포 난수 생성
    numpy.random.rand() : 0.0 이상 1.0 미만
    numpy.random.rand_sample() : 0.0 이상 1.0 미만
    numpy.random.randint() : 정수 난수

2. 정규 분포 난수 생성
    randn() : 평균 0, 분산 1 (표준편차 1)
    normal() : 임의의 평균, 표준편차
    *표준표차, 상관계수가 같아도 꼭 데이터의 분포가 같은 것은 아님

3. 이항 분포 난수 생성
    binomial()  X ~ B(n,p) = 확률변수
    사건이 발생했을때 일어날 확률이 p이고 n번 반복한 것

4. 배타 분포 난수 생성
    beta()

5. 감마 분포 난수 생성
    gama()

6. 카이제곱 분포 난수 생성
    chisquare()
'''