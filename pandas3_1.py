import pandas as pd
import numpy as np

#파일읽기
trade=pd.read_csv("./raw_trade_data.csv", encoding='cp949')

# 2번 문제: 전처리 과정 클렌징 및 정규화

# 1. 중량 컬럼 결측치 처리
print(trade.head(15))
trade.groupby("hs_code") # hs 코드가 같은 것끼리 그룹화 > 이들에 대한 중량의 평균을 계산해야함. 
hs_mean=trade.groupby("hs_code")["중량"].mean() # 그룹에 대한 평균을 각각 구함.

print(hs_mean)
'''hs_code
8471300000    287.961951
8541100000    247.668298
8542311010    270.992593
8703231010    273.699889
Name: 중량, dtype: float64'''

for hs in hs_mean.index : #따로 딕셔너리를 안만들어도 됨. key랑 value를 둘다 가져와야 하므로 item / 아니면 value값(여기선 평균)만 갖고오고 싶으면 .index
    # 첫번째, 현재 순서의 HS코드에 해당하는 평균값을 가져오기
    avg_val=hs_mean[hs]
    # 두번째, 원본 데이터에서 해당 hs코드이면서 중량이 비어있는 null값인 행만 찾기
    target = (trade["hs_code"]==hs) & (trade["중량"].isna())   # 이 때 & 는 and이다. 
    # 세번째, 해당되는 칸에만 평균값을 대입하기(데이터 넣기)
    trade.loc[target,"중량"]=avg_val

#만약 빈칸을 0으로 채우고 싶다면?
'''trade.loc[trade["중량"].isna()]=0 # 이렇게 하면 빈칸이 0으로 채워진다. '''



# 2. 수입, 수출로 자료 변경

trade.loc[trade["수출입구분"]=="Export", "수출입구분"]="수출"
trade.loc[trade["수출입구분"]=="Import", "수출입구분"]="수입"

# 3. 수출금액 단위 변환 원 > 백만달러 : (금액/1470)/1000000 새 컬럼을 만들어야 함. 

exchange_rate=1470
trade["수출금액_M_USD"] = (trade["수출금액"]/exchange_rate)/1000000


# 4. 변경 후 데이터의 각 컬럼별 데이터 타입(df.dtypes)을 확인하여 수치형 데이터가 맞는지 검증

print("\n ----[최종 데이터 확인]---- ")
print(trade.dtypes) 

print("\n ----[클렌징 결과 샘플 확인]---- ")
print(trade[["날짜","hs_code","수출금액","수출입구분","수출금액_M_USD"]].head(10)) # 필드를 여러 개 갖고 오고 싶으면 [[]] 이중 괄호 쓰기

# 최종 데이터 저장(이 폴더 내에 저장)
trade.to_csv("./cleaned_trade_data.csv", encoding="cp949",index=False) # ./ : 현재 있는 폴더에 저장
print("과제2 완료 'cleaned_trade_data.csv'이 저장되었습니다")
