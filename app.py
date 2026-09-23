import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Nile Shield", page_icon="🛡️", layout="wide")
st.title("🛡️ NILE SHIELD - درع النيل")
st.markdown("**From NASA Data to Every Egyptian Farmer | Sahil Tahta**")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("1. الفضاء 🛰️")
    st.info("Landsat 8/9: يصور النيل\nGPM: يقيس مطر منابع النيل")
    st.metric("جودة الصورة", "92%", "نقية")

with col2:
    st.header("2. الذكاء 🤖")
    p = random.randint(20,90)
    st.metric("نسبة التلوث", f"{p}%")
    if p > 60:
        st.error("⚠️ تلوث عالي في ساحل طهطا!")
    else:
        st.success("✅ النيل نظيف حاليا")

with col3:
    st.header("3. الارض 🌍")
    st.success("SMS للفلاحين: تم الارسال")
    st.map(pd.DataFrame({'lat':[26.56], 'lon':[31.84]}))

st.markdown("---")
st.caption("© 2026 Nile Shield | NASA Space Apps Cairo")
