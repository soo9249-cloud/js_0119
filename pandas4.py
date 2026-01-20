'''[26.01.20 진행 예제]

📊 실무 프로젝트: 글로벌 무역 실적 통합 분석 보고서

본 과제는 제공된 "두 개의 데이터를 결합"하여 우리 회사의 무역 현황을 다각도로 분석하고, 전략적 인사이트를 도출하는 것을 목표로 합니다.

📂 활용 데이터

trade_performance.csv: 일자별/국가별 수출입 금액 및 중량 실적
country_master.csv: 국가 코드별 국가명, 대륙, FTA 체결 여부 정보

💡 핵심 체크 포인트

Pandas의 merge() 함수를 정확히 사용하는가?
groupby()를 통해 다차원적인 통계를 산출할 수 있는가?
산술 연산을 통해 '무역수지', '단가' 등 새로운 지표(파생 변수)를 생성할 수 있는가?'''

# import streamlit as s
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # 차트에 데이터를 뿌리는 것 
import seaborn as sns
import datetime as dt

# 데이터 불러오기 
try: 
    # 실제 실적 데이터 가져오기/오류가 없으면 파일 불러내기? trade_performance   / try는 정상적일 때 실행되는 애고 except는 오류가 났을때...
    df_pref = pd.read_csv("./trade_performance.csv", encoding = "cp949")
    # 마스터 데이터 국가 코드 국가명 country_master
    df_master = pd.read_csv("./country_master.csv", encoding = "cp949")

except FileNotFoundError:
    print("❌ CSV 파일이 없습니다. 경로를 다시 확인해주세요.")

print(df_pref)
print(df_master)

# 🎯 프로젝트 과제 (5단계)

# Step 1: 데이터 통합 (Merge)
# 두 파일을 ctry_code를 기준으로 병합하여, 실적 데이터에 국가명과 대륙 정보가 나타나도록 하세요.
# 1. 머지(Merge): 데이터 병합 / ctry_code로 병합
df = pd.merge(df_pref, df_master, on="ctry_code",how="left")  
 # vlookup엑셀 함수랑 논리가 똑같다 / how는 기준치를 어디에 잡을거니? 라는 뜻. left는 두 데이터 중 왼쪽 맨 앞 파일 기준(데이터 3개 이상도 합칠 수 있다)
print(df)


# Step 2: 대륙별 성과 분석 (Aggregation)

# 병합된 데이터를 활용하여 대륙별 총 수출액과 총 수입액을 구하세요.
print("\n ----[대륙별 성과 분석 - 총 수출액과 총 수입액]----")
continent_states=df.groupby("continent")[["export_val","import_val"]].sum()
print(continent_states)
# > 엑셀 툴보다 더 간단하게 구할 수 있다. 

# 어느 대륙과의 거래에서 가장 큰 무역수지(수출-수입) 흑자가 발생했는지 확인하세요.
continent_states["무역수지"] = continent_states["export_val"]-continent_states["import_val"]
print("----대륙별 무역 성과 요약----")
print(continent_states)  # API를 갖고 오면 알아서 흑자인지 적자인지 커멘트를 달아줌. Saas할 때 할 것. saas가 오픈 api를 활용해서 유료 api를 갖고 자료분석하는?
# 어느 대륙이 제일 돈 많이 남았나?
best_continent=continent_states["무역수지"].idxmax()
print(f"분석 결과 : {best_continent} 대륙과의 거래에서 가장 큰 무역 수지 흑자가 발생했습니다.")

'''
.max() 최댓값 #숫자
.idxmax() 최댓값의 위치/이름 #인덱스
.min() 최솟값 # 숫자
.idxmin() 최솟값의 위치/이름 # 인덱스
'''


# Step 3: FTA 효과 분석 (Groupby)

# FTA 체결 국가(fta_status == 'Y')와 미체결 국가(fta_status == 'N')의 **평균 수출 단가(수출금액/중량)**를 비교하세요.
# 평균 수출 단가 구하기
df["평균수출단가"] = df["export_val"]/df["weight"] # 평균 수출 단가 시리즈 만들기
# FTA 체결 여부에 따른 평균 수출 단가 비교 > FTA로 그룹화하기
fta_ans = df.groupby("fta_status")["평균수출단가"].mean()
print("\n ----[FTA 여부에 따른 평균 수출 단가 비교]---- ")
print(fta_ans)

# FTA 체결이 수출 경쟁력에 기여하고 있는지 수치로 증명하세요.
# 시사점 도출
if fta_ans["Y"] > fta_ans["N"]: # key를 사용해 value값을 물어보는 것. Y와 N의 값을 각각 가져와서 비교해라
    print("결과: FTA 왜 체결했니? FTA 체결 국가의 평균 단가가 더 높게 나타나며 수출 경쟁력이 떨어진다는 것이 수치로 증명되었습니다.")
else: 
    print("결과: FTA 체결 국가의 평균 단가가 미 체결국가 간의 단가 차이에 대한 추가 분석이 필요함.")


# Step 4: 품목별 집중도 분석 (Filtering)
# 특정 품목(hs_code) 중 수출 금액이 가장 큰 상위 2개 품목을 찾으세요.
top2_hs = df.groupby("hs_code")["export_val"].sum().nlargest(2).index.tolist()
# nlargest(2) 가장 높은 값 2개 # nsmallest(2)가장 낮은 값 2개
# tolist > 리스트 형태로 바꿔라(value)값만 나온다.
print(f"\n 수출 상위 2개 품목: {top2_hs}")


# 해당 품목들이 주로 어느 국가로 수출되고 있는지 분석하세요.(해당 품목들의 국가별 수출 현황)
top2_df=df[df["hs_code"].isin(top2_hs)]
#isin은 있다 없다를 찾는 것. 
# 코드도, 국가도 각각 그룹을 잡아야 한다. 
country_focus=top2_df.groupby(["hs_code","ctry_name"])["export_val"].sum().reset_index() #reset_index()프레인 형태로 보여주는 것. 안써도 나오긴 함
print(country_focus)



# Step 5: 시각화 및 인사이트 도출 (Visualization)

# 날짜 데이터 월 정보 추출
df["ymd"]=pd.to_datetime(df["ymd"]) # object를 날짜로 바꾸고
df["month"]=df["ymd"].dt.month  # 그 데이터를 월별로 묶어라? 판다스 관련 뭐지?
# print(df.info())
# print(df.head())


# 월별 수출입 추이를 선 그래프로 시각화하세요.
monthly = df.groupby("month")[["export_val","import_val"]].sum()
plt.figure(figsize=(12,6)) # 12:6의 비율 크기의 차트를 만들 것.
plt.plot(monthly.index, monthly["export_val"], label="수출액", marker="o", linewidth=2)
plt.plot(monthly.index, monthly["import_val"], label="수입액", marker="s", linewidth=2)
# 데이터가 1월 하나밖에 없어서 점만 찍힘.. 

plt.title("월별 수출입 실적 추이")
plt.xlabel("월(month)")
plt.ylabel("금액")
plt.show()



# 분석 결과를 바탕으로 "다음 분기에 마케팅을 집중해야 할 국가/대륙"을 1문장으로 제안하세요.
# matplotlib 관계...???

# gemini에게 구글 사이트 보내고 데이터 구조를 분석하라고 지시 (바로 코드 짜라고 하지 말기)
# 내가 그 데이터를 갖고 뭘 할 수 있는지 고민해보기