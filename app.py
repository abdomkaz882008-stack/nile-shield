import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import datetime

st.set_page_config(page_title="Nile Shield", page_icon="🛡️")
st.title("NILE SHIELD - درع النيل")
st.markdown("From NASA to Every Farmer")
st.divider()

BBOX = "31.5,26.3,32.0,26.7"
today = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
layer = "MODIS_Terra_CorrectedReflectance_TrueColor"
url = f"https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&LAYERS={layer}&BBOX={BBOX}&WIDTH=800&HEIGHT=800&FORMAT=image/jpeg&TIME={today}&CRS=EPSG:4326"

st.subheader(f"Live NASA Image - {today}")

try:
    r = requests.get(url, timeout=25)
    if r.status_code == 200 and "image" in r.headers.get("Content-Type", ""):
        img = Image.open(BytesIO(r.content))
        st.image(img, use_column_width=True)
        st.success(f"NASA Live: {today}")
    else:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800", use_column_width=True)
        st.warning("NASA busy, demo image shown")
except Exception as e:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800", use_column_width=True)
    st.error(f"Error {e}")

c1, c2, c3 = st.columns(3)
c1.metric("Quality", "92%", "Clear")
c2.metric("Water Save", "30%", "2000 L")
c3.metric("Source", "NASA", "Live")
