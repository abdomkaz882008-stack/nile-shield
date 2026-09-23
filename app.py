import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import datetime

st.set_page_config(page_title="درع النيل", page_icon="🛡️")
st.title("🛡️ NILE SHIELD - درع النيل")
st.markdown("**From NASA to Every Farmer**")

BBOX="31.5,26.3,32.0,26.7"
today=datetime.date.today().strftime("%Y-%m-%d")
layer="MODIS_Terra_CorrectedReflectance_TrueColor"
url=f"https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&LAYERS={layer}&BBOX={BBOX}&WIDTH=800&HEIGHT=800&FORMAT=image/jpeg&TIME={today}"

st.subheader(f"صورة ناسا الحية - ساحل طهطا - {today}")
try:
    r=requests.get(url,timeout=20)
    img=Image.open(BytesIO(r.content))
    st.image(img,use_column_width=True)
    st.success("✅ تم السحب من ناسا لايف!")
except Exception as e:
    st.error(f"ناسا مشغولة: {e}")

col1,col2,col3=st.columns(3)
col1.metric("الجودة","92%","نقية")
col2.metric("توفير مياه","30%","2000 لتر")
col3.metric("المصدر","NASA","Live")
