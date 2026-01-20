# import streamlit as st/
import pandas as pd
import numpy as np

# 교수님ver
trade=pd.read_csv("./raw_trade_data.csv", encoding='cp949') #read.csv 라는 명령어 자체가 판다스 명령어
# print(trade)  # 이걸해야...안터짐..?

# 1. hs 85로 시작하는 것
# print(trade.info())

# trade["hs_code"].astype(str) > hs 코드를 문자로 바꿔주는 과정
cond_hs=trade["hs_code"].astype(str).str.startswith("85")
# print(cond_hs.head()) #hs_code의 85로 시작하는애만 True로 보인다. 

# 2. 미국, 베트남 > 국가명 필드에 있는 애들만
cond_country=trade["국가명"].isin(["미국","베트남"]) # 엑셀에서는 if, or로 여러번 써야함
# print(cond_country) # 미국, 베트남만 True로 보인다. 




# 3. 수출금액이 0인 데이터 제외
# print(trade.head(10))
cond_value=trade["수출금액"]>0
#cond_value=cond_country["수출금액"]>0
# print(cond_value) # 0만 False로 나온다. 
#  여기까지는 조건에 맞는 걸 True, False로 나오게 하기만 함


# 결합하기
# step1=trade[cond_hs]
# step2=step1[cond_country]
# step3=step2[cond_value]

step3=trade[cond_hs & cond_country & cond_value] # & = and , | = or
print(step3)


# 이게 제일 간단한 방법

# 파일 저장
trade.to_csv("저장할 파일명.csv", encoding='cp949', index=False)

