import pandas as pd 
import numpy as np

dict_data={
    "a":1,
    "b":2,
    "c":3,
}

series_data = pd.Series(dict_data) 
print(type(series_data))
print(series_data)   # dtype: int64 > 64bit = 8 bytes (8bit=1byte) 


list_data = [
    "2026-1-19",
    3.14,
    "abc",
    100,
    True
    ]
series_data=pd.Series(list_data)
print(type(series_data))
print(series_data)   
"""
0    2026-1-19
1         3.14
2          abc
3          100
4         True
dtype: object  # 개체 생성(클래스 관련) > dtype: object (문자열 포함 모든 자료형 가능)??
"""

dict_data={"c0":[1,2,3],
           "C1":[4,5,6],
           "c2":[7,8,9],
           "c3":[10,11,12],
           "c4":[13,14,15],
           }
# DataFrame 생성 
df=pd.DataFrame(dict_data)
print(type(df))
print(df)

# co~c4: column names
# 0~2: index names (row names)

# 엑셀처럼 행열구조로 만들어주는 게 pandas > 연산도 가능하다. 

# numpy는 수치계산에 특화된 라이브러리 
# pandas는 데이터 분석에 특화된 라이브러리

# pandas 데이터 내용 확인하는 방법
# .colums : 컬럼명 확인
# .head(): 데이터 상단의 5개 행 출력 ()안에 숫자채우면 그 개수만큼 본다
# .tail(): 데이터 하단의 5개 행 출력 ()안에 숫자채우면 그 개수만큼 본다
# .shape: (행, 열) 크기 확인, 셀 개수 확인
# .info(): 데이터에 대한 전반적인 정보 제공 (행열 크기, 컬럼명, 컬럼별 결측치>데이터가 비어있는 부분 확인, 컬럼별 데이터 타입) +info는 다 갖고 오는 것
# .type(): 데이터 타입 확인

# 파일 불러오기 
'''
형식      읽기          쓰기
csv      read_csv     to_csv
excel   read_excel   to_excel
JSON    read_json    to_json
html    read_html    to_html
./ 내가 있는 기준으로 하위 폴더 이동 ./폴더명/tesditanic=pd.read_csv(".")
../ 내가 있는 기준으로 상위 폴더 이동 ../../../  > 상위폴더/상위폴더/상위폴더/폴더명/데이터명
'''

# 제일먼저 변수를 받아서 읽는다
titanic = pd.read_csv("Titanic-Dataset.csv") # csv 파일 불러오기
print(titanic) # 전체 데이터 출력
print(titanic.columns)
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')
print(titanic.head()) # 상단 5개 행 출력
print(titanic.tail(10))
print(titanic.shape) # (891,12)
print(titanic.info())
#object: 문자열(숫자가 섞여있을수도 있음. 모든 개체), int64: 정수, float64: 실수, bool: 참거짓
#non-null: 결측치가 아닌 값 (데이터가 들어있는 값)??

print(type(titanic)) # <class 'pandas.core.frame.DataFrame'>

# 판다스에서 특정 열 선택 방법 # 

# 1개의 열 선택 pandas에서 열은 series로 반환 = Series 객체 반환
# 데이터 프레임의 열 데이터 1개 선택할 때 2가지 방식
# 1) 대괄호 [] 안에 열 이름을 따옴표("")로 함께 입력
# 2) 점(.)=도트 다음에 열 이름 입력

# 열 n개 선택 = DataFrame 객체 반환
# 데이터 프레임의 열 데이터 n개를 선택할 땐ㄴ 1가지 방식
# 이중 대괄호 [[]] 안에 열 이름을 따옴표("")로 함께 입력

# ***만약에 열 1개를 데이터 프레임 객체로 추출하려면 [[]] 사용가능

# 방법 1
names = titanic ["Name"]  
print(names.head())
# 방법 2
names=titanic.Name #대문자인 이유는 column name이기 때문
print(names.head())
print(type(names))
print(names.shape) # (891,)

# 열 n개 선택 해보기 (Sex, Age) / (Pclass, Age)로 해도 됨
double_columns = titanic[["Sex", "Age"]]
print(double_columns.head())
print(type(double_columns))  # <class 'pandas.core.frame.DataFrame'>
print(double_columns.shape)  # (891, 2)

# pandas에서 데이터 필터링

# 1. boolean 인텍싱 True값을 가진 행만 추출하기 
# 2. .isin() 각각의 요소가 데이터프레임 또는 시리즈에 존재하는지 파악한 후 True/False 반환 (둘이 섞어써도 가능하다)
# 3. .isna() 결측치 확인 (결측치: 비어있는 값) > 반대는 .notna() # 없으면 False 있으면 True / isin 결측값은 True, 그 외는 False(비어있으면 T, 채워져있으면 F)
# 4. .notna() 결측값은 False, 그 외는 True
# 5. between() 범위 내에 있는지 확인 (숫자형 데이터에만 사용 가능)
# 1. boolean 인덱싱


print(double_columns["Age"]>=35) #이게 boolean indexing

# True인것만 보고싶다면?
above35 = double_columns[double_columns["Age"]>=35] # 조건을 변수로 치환
print(above35.head()) #True 값만 추출 기본 위에서 5개 행 출력

# 성별 - 남자만 추출
gender_male=double_columns[double_columns["Sex"]=="male"]
print(gender_male.head())

# isin() 메서드 사용법
print(titanic.head())
class_1 = titanic[titanic["Pclass"].isin([1])]
print(class_1.head()) # 1등석 승객들만 추출

print(double_columns.head())
age2040 = double_columns[double_columns["Age"].isin(np.arange(20,41))]  #isin을 거는 이유: 나이에 있다 없다를 걸어주는 것
# >> 20~40까지의 숫자가 있으면 뽑아라
print(age2040.head(10))


# 결측치 
print(double_columns.head(7))
class_2=double_columns["Age"].isna()  # 결측치 확인 # 비어있는 cell을 True로 반환
print(class_2.head(7))  # True: 결측치, False: 결측치 아님


class_3=double_columns["Age"].notna()  # 비어있는 cell을 False로 반환
print(class_3.head(7))  # True: 결측치 아님, False: 결측치

# 결측 값을 제거한 누락되지 않는 값을 확인
# 행 제거
print(double_columns.head(10))
# 결측치가 있는 행 제거 / 제거되더라도 다음 행의 인덱스 번호는 유지된다. 

age5=double_columns[double_columns["Age"].notna()]
print(age5.head(10)) # 5번째 행이 사라짐. 인덱스번호는 4다음 6으로 유지

# 결측치 제거 
# .dropna(axis=0) == .dropna() : 결측 값들이 들어 있는 "행(0)" 전체를 삭제
# .dropna(axis=1) == : 결측값이 들어 있는 "열(1)" 전체 삭제

print(titanic.head())
print(titanic.dropna()) # 0번행, 2번행, ... 삭제됨 (결측치가 하나라도 있으면 행 전체 삭제)

titanic.dropna(axis=1) # 열 기준
print(titanic.dropna(axis=1).head()) # Age, Cabin 열 전체 삭제됨 (결측치가 하나라도 있으면 열 전체 삭제)

# 엑셀을 굳이 안쓰고도 판다스로 처리 가능
# pandas > 이름과 인덱스로 특정 행과 열 선택 가능
# .loc[]: 이름 기반 인덱싱 > 행 이름과 열 이름 사용 DataFrame객체.loc[행이름, 열이름]
# .iloc[]: 정수 기반 인덱싱 > 행 번호와 열 번호 사용 DataFrame객체.loc[행번호, 열번호]

name35=titanic.loc[titanic["Age"]>=35,["Name","Age"]]
print(name35.head()) 

name35.iloc[[1,2,3],0] = "No name" # 1,2,3번째 행의 0번째 열 (Name열)
print(name35.head())
'''
                                                Name   Age
1   Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0  > 1행
3                                             No name  35.0
4                                             No name  35.0
6                                             No name  54.0
11                           Bonnell, Miss. Elizabeth  58.0

'''

# 판다스 데이터 통계 (numpy가 아닌 padnas에서 제공하는 통계 메서드)
# .mean(): 평균값 계산
# .median(): 중앙값 계산
# .describe(): 다양한 통계량 요약 출력 > mean, std min, max, 25%, 50%, 75% 범위 내 구하기 등등
# .mode(): 최빈값 계산
# .std(): 표준편차 계산 
# .min(): 최소값 계산
# .max(): 최대값 계산
# .count(): 데이터 개수 계산
# .sum(): 합계 계산
# .agg(): 여러 개의 열에 다양한 함수 적용
# 모든 열에 여러 함수를 매핑 : group.객체.agg([함수1, 함수2,...])
# 각 열마다 다른 함수를 매핑 : group.객체.agg({"열1":함수1, "열2":함수2,...})
# .groupby(): 그룹별 집계 (집단별로 나눠서 통계 계산할 때 사용)
# .value_counts(): 값의 개수 세기 (범주형 데이터에 주로 사용?)

print("---- 평균 나이 ----")
print(titanic["Age"].mean()) # 수치가 있는 열만 계산된다(?)
print("---- 중앙값 나이 ----")
print(titanic["Age"].median())
print("---- 나이에 대한 다양한 통계량 요약 ----")
print(titanic.describe())

print("---- 나이와 요금의 평균 및 표준편차 ----")
print(titanic[["Age","Fare"]].agg(["mean","std"])) # 여러 열에 여러 함수 적용

print("---- 열별 사용자 집계 ----")
agg_dict={
    "Age":["min","max","mean"],
    "Fare":["median","sum"]
}
print(titanic.agg(agg_dict)) # 각 열마다 다른 함수 적용

print("---- 성별 기준으로 평균 나이 및 요금 ----")
print(titanic.groupby("Sex")[["Age","Fare"]].mean())

print("---- 객실 등급(Pclass)별 인원수")
print(titanic["Pclass"].value_counts())

print("---- 성별 인원수 ----")
print(titanic["Sex"].value_counts())

print("---- 새로운 열 country 열 생성 USA----")
titanic["Country"]="USA"
print(titanic)

print(" ---- 기존의 열을 계산해서 새로운 열을 추가 ----")
titanic["NewAge"]=titanic["Age"]+10
print(titanic)

# 28세 미만이면 child, 아니면 adult
print(" ---- 20세 미만이면 child, 아니면 adult----")
titanic["Age_group"]="Adult"
print(titanic)
titanic.loc[titanic["Age"]<20, "Age_group"] = "Child" #loc...?
print(titanic)

# 데이터 프레임의 가장 마지막 인덱스 확인 후 행 추가
new_index = len(titanic)
print(new_index) 
# [891 rows x 15 columns]
# 891

print(titanic.head())
titanic.loc[new_index] =[992,1,1,"shin","female",53,3,1,"Pc123",20.0,"C77","S","USA",63,"Adult"]

new_data = pd.DataFrame({
    "Name":["홍길동", "김길동"],
    "Age":[22,30],
    "Sex":["female","male"],
    "Survived":[1,0],
})

titanic = pd.concat([titanic, new_data], ignore_index=True)
# concat: 추가된 애들까지 집어넣어서 인덱스 번호 최종정리하는 애

# 꼬리에서 봐야 한다. 
print(titanic.tail())

# titanic이 갖고 있는 문자열 중에서 S로 시작하는 것만 갖고 오고 싶다면?
titanic["Name"].str.startswith("Sa") # 문자열 데이터가 Sa로 시작하는 자료만 추출
# print(titanic["Name"].str.startswith("Sa"))
# titanic[titanic["Age"].astype(str).str.startswith("2")]
# titanic[titanic["Age"].astype(str).str.startswith("^82")] # 앞에 아무거나 오고+82


# 파일 저장
titanic.to_csv("./sample1.csv", index=False) # > index=False로 걸어주면 인덱스번호 생성 안됨. 안 적으면 생성됨
# titanic.to_excel("./sample1.xls", index=False) 
print("파일 저장이 완료되었습니다")
