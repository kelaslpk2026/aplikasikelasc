import streamlit as st

st.title("🎈 Aplikasi Kelas C")
st.header("Mari coba membuat kalkulator sederhana")
number1=st.number_input("Masukkan angka 1")
number2=st.number_input("Masukkan angka 2")

tambah=st.button("+")
kurang=st.button("-")
kali=st.button("x")
tambah,kurang,kali=st.columns(3)
if tambah:
    st.subheader(f"{number1}+{number2}={number1+number2}")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
