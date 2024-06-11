import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# 데이터 불러오기
df = pd.read_csv('data/VAR_감염자수예측_1.csv',index_col=0, encoding='cp949')

# 연도 데이터 추출
years = df.index.str.split('-').str[0].unique()
years = sorted(years)  # 연도를 오름차순으로 정렬

# streamlit 앱 제목 설정
st.title('대표 감염병 환자 수 예측')

# 연도 선택 위젯
selected_index = st.select_slider('연도 선택', options=range(len(years)), format_func=lambda x: years[x])

# 선택된 연도에 해당하는 데이터 필터링
selected_year = years[selected_index]
filtered_df = df[df.index.str.startswith(selected_year)]

# 대표질환 감염자수 시각화
st.subheader(selected_year + '년 예측')

# Matplotlib를 사용하여 바차트 생성
fig, ax = plt.subplots()
ax.bar(filtered_df.index, filtered_df['대표질환감염자수'])

# y축 범위 조절
ax.set_ylim(350, 500)  # 원하는 범위로 설정

# Streamlit에 Matplotlib 그림 표시
st.pyplot(fig)