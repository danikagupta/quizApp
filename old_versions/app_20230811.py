import streamlit as st
import pandas as pd


@st.cache_data
def load_csv(url):
  print("\n======REFRESHING")
  print(f"1. Source CSV is {url}")
  df=pd.read_csv(url)
  return df


def one_run():
  print("++++START")
  df=load_csv(st.secrets["QUESTION_SOURCE"])
  row=df.sample()
  dict_row=row.to_dict(orient='list')
  print(f"2. Dict row is {dict_row}")
  question=dict_row["Question"][0]
  a1=dict_row["A1"][0]
  a2=dict_row["A2"][0]
  a3=dict_row["A3"][0]
  a4=dict_row["A4"][0]
  r1=dict_row["R1"][0]
  r2=dict_row["R2"][0]
  r3=dict_row["R3"][0]
  r4=dict_row["R4"][0]
  corr=dict_row["Correct"][0]
  st.text(f"Question is: {question}")
  if st.button(f"{a1}"):
    st.text(f"R1 is: {r1}")
  a2=st.button(f"{a2}")
  a3=st.button(f"{a3}")
  a4=st.button(f"{a4}")
  st.text(f"Correct is: {corr}")
  if a2:
    st.text(f"R2 is: {r2}")
  if a3:
    st.text(f"R3 is: {r3}")
  if a4:
    st.text(f"R4 is: {r4}")
  print(f"Row is {dict_row}")
  print(f"Question is {question}")
  print("++++COMPLETE")

one_run()


