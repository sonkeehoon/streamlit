import streamlit as st
import pandas as pd

f = open("./damage.txt",'r',encoding="utf-8")
lines = f.readlines()
view=[]
for line in lines:
    view.append(int(line))
f.close()
st.write('# 메이플 스탯공격력 변화')
st.write('## raw')
view
st.write('## Chart')

st.bar_chart(view)

sview=pd.Series(view)
sview
