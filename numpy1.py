import numpy as np

# numpy는 다차원. 엑셀의 수치 계산
# 선형대수...연산에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수 제공

# 3차원에서 z축을 0번, x축을 1번, y축을 2번으로 본다. 

# 1. 넘파이 배열
# 파이썬 리스트와 비슷해 보이지만 계산 속도가 훨씬 빠르다

a_valuse=np.array([12500,45000,32000,0,56000])
#array: 배열 만들어주는 명령어 메서드

print(a_valuse) # [12500 45000 32000     0 56000]'

# pandas는 엑셀의 역할, numpy는 그 셀 안에 있는 데이터 연산을 한다고 보면 된다. 

b_valuse=np.array([
    [1000,2000,3000,4000],
    [5000,6000,7000,8000],
    [9000,10000,11000,12000],
]) # > 3행 4열의 형태이다(2차원)
print(b_valuse)


# 3차원
c_values = np.array([
    # 지역이 아시아
    [
        [100,200,300],
        [200,300,400],
        [500,600,700]
    ],
    [
        # 유럽
        [90,80,50],
        [80,80,40],
        [100,80,50],
    ],
     [
        # 북유럽
        [60,60,40],
        [70,60,50],
        [100,50,40],
    ],  
])
print(c_values)
# 엑셀과 달리 한번에 쓸 수 있는게 numpy...?

print(a_valuse.shape)
print(b_valuse.shape)
print(c_values.shape)
# sahpe:내가 갖고 있는 데이ㅌ의 모양, 몇행 몇열?인지 찍는 것
'''
(5,) 튜플은 하나일 때 , 찍는다. 1차원 배열이므로 ,까지 5개의 1차원 배열
(3, 4) 3행 4열
(3, 3, 3) x,y,z축이 다 3,3,3 
'''

print(a_valuse.itemsize) #8
print(b_valuse.itemsize) #8
print(c_values.itemsize) #8 
# 8바이트, 각 정보가 숫자라는 뜻(?)
# items는 자료 구조 보는 것. byte

print(a_valuse.size) #5 (1행 5개 값 데이터 있음)
print(b_valuse.size) #12 : 3*4
print(c_values.size) #27 : 3*3*3
# size > 셀 개수와 마찬가지

# np.zeros : 0으로 구성된 n차원 배열 생성
# np.one : 1로 구성된 n차원 배열 생성
# np.empty : 초기화 되지 않은(비어있는?) n차원 배열 생성SS

print(np.zeros((4,6))) # 4*6의 행렬을 만들고 0으로 채워라
print(np.ones((2,3,4) , dtype=np.int64))
print(np.empty((2,3)))   # n차원 배열 만들기

print(np.arange(10,30,5)) # [10,15,20,25]
print(np.arange(0,2,0.3)) # [0.  0.3 0.6 0.9 1.2 1.5 1.8] float의 형태로도 가져올 수 있다. 

print(np.linspace(0,99,100)) # 0부터 99까지를 100등분
print(np.arange(0,1+0.25,0.25)) # 1.25

print(np.linspace(0,1,5))

a=np.arange(6)
print(a)
# [0 1 2 3 4 5]

b=np.arange(12).reshape(4,3)
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

c=np.arange(24).reshape(2,3,4)
print(c)


a=np.array([20,30,40,50])
b=np.arange(4)#[0,1,2,3]
c=a-b
print(c) # [20 29 38 47]

print(b*10) # 0 10 20 30
print(b**10) # [    0     1  1024 59049]

print(a < 35) # [ True  True False False]
# numpy는 셀 데이터를 하나하나 긁어오지 않고, 연산기호만으로 계산할 수 있다. 

A = np.array([
    [1,1],
    [0,1],
])

B = np.array([
    [2,0],
    [3,4],
])

print(A*B)
'''
[[2 0]
 [0 4]]  같은 위치에 있는 데이터들끼리(행렬끼리) 곱한 값이 나온다.
'''

print(A@B) # 행렬 곱셈

int < float # 정수보다 소수가 더 강하다. 둘이 같이 묶이면 float 형태로 나온다. 