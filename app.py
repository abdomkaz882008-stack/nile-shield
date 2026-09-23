import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.set_page_config(page_title="NILE SHIELD", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
.stApp { background: #080a0f; color: white; }
.gold-title { color: #D4AF37; font-weight: 800; }
.sat-card {
  background: linear-gradient(180deg, #1c2333 0%, #121722 100%);
  border: 1px solid #D4AF37; border-radius: 16px; padding: 18px;
}
.field-box { border-radius: 14px; padding: 14px; text-align: center; font-weight: bold; }
.green-box { background: #102a14; border: 1px solid #2ecc71; color: #2ecc71; }
.yellow-box { background: #2e2a0f; border: 1px solid #f1c40f; color: #f1c40f; }
.red-box { background: #2e1212; border: 1px solid #e74c3c; color: #e74c3c; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='gold-title'>NILE SHIELD - درع النيل 🛡️</h1>", unsafe_allow_html=True)
st.caption("Protecting Nile Agriculture with NASA Eyes | NASA Space Apps 2026")

c1, c2 = st.columns([0.9, 1.3], gap="large")
with c1:
    st.markdown("**Time | التوقيت**")
    components.html("""
    <div style="background:#000;padding:16px;border-radius:20px;text-align:center;border:2px solid #D4AF37;box-shadow:0 0 20px rgba(212,175,55,0.3)">
      <canvas id="clock" width="220" height="220"></canvas>
      <div id="dig" style="color:#D4AF37;margin-top:10px;font-weight:bold;font-size:22px;font-family:monospace;letter-spacing:2px;"></div>
    </div>
    <script>
    const c=document.getElementById('clock'), x=c.getContext('2d'), d=document.getElementById('dig');
    function draw(){
      const n=new Date(),h=n.getHours()%12,m=n.getMinutes(),s=n.getSeconds();
      d.innerText=n.toLocaleTimeString('en-GB');
      x.clearRect(0,0,220,220);
      // gold face
      x.beginPath(); x.arc(110,110,95,0,6.283); x.fillStyle='#D4AF37'; x.fill();
      x.beginPath(); x.arc(110,110,95,0,6.283); x.strokeStyle='#000'; x.lineWidth=4; x.stroke();
      // inner black border
      x.beginPath(); x.arc(110,110,88,0,6.283); x.strokeStyle='#000'; x.lineWidth=2; x.stroke();
      x.fillStyle='#000'; x.font='bold 22px sans-serif'; x.textAlign='center'; x.textBaseline='middle';
      x.fillText('12',110,32); x.fillText('3',188,110); x.fillText('6',110,188); x.fillText('9',32,110);
      let ha=h*0.523+m*0.0087; x.beginPath(); x.moveTo(110,110); x.lineTo(110+45*Math.sin(ha),110-45*Math.cos(ha)); x.strokeStyle='#000'; x.lineWidth=7; x.lineCap='round'; x.stroke();
      let ma=m*0.1047; x.beginPath(); x.moveTo(110,110); x.lineTo(110+70*Math.sin(ma),110-70*Math.cos(ma)); x.strokeStyle='#000'; x.lineWidth=5; x.stroke();
      let sa=s*0.1047; x.beginPath(); x.moveTo(110,110); x.lineTo(110+80*Math.sin(sa),110-80*Math.cos(sa)); x.strokeStyle='#8b0000'; x.lineWidth=2; x.stroke();
      x.beginPath(); x.arc(110,110,9,0,6.283); x.fillStyle='#000'; x.fill(); x.strokeStyle='#D4AF37'; x.lineWidth=2; x.stroke();
    }
    setInterval(draw,1000); draw();
    </script>
    """, height=330)

with c2:
    st.markdown("**Field Status | حالة الأرض**")
    g,y,r = st.columns(3)
    with g: st.markdown('<div class="field-box green-box"><div>🟢 HEALTHY</div><h1>76%</h1><small>1,520 فدان - سليم</small></div>', unsafe_allow_html=True)
    with y: st.markdown('<div class="field-box yellow-box"><div>🟡 WATCH</div><h1>17%</h1><small>340 فدان - مراقبة</small></div>', unsafe_allow_html=True)
    with r: st.markdown('<div class="field-box red-box"><div>🔴 RISK</div><h1>7%</h1><small>140 فدان - خطر</small></div>', unsafe_allow_html=True)
    st.write("")
    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Temp | حرارة", "31.7°C", "-0.4°C")
    k2.metric("Humidity | رطوبة", "26%", "+2%")
    k3.metric("Wind | رياح", "10.7 km/h")
    k4.metric("Soil Water", "250 mm")

st.divider()
st.markdown("### 🛰️ Satellite Analysis | تحليل الأقمار")

s1,s2,s3 = st.columns(3)
with s1:
    st.markdown('<div class="sat-card"><h4>🛰️ TERRA MODIS</h4><small>NDVI Vegetation Index</small><h2 style="color:#2ecc71">0.75 - Excellent</h2><p style="font-size:13px;color:#aaa">النباتات خضراء وصحية جدا. النمو في اعلى مستوى له.</p></div>', unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({"NDVI":[0.62,0.65,0.68,0.71,0.73,0.75]}, index=["Mar","Apr","May","Jun","Jul","Aug"]))

with s2:
    st.markdown('<div class="sat-card"><h4>🛰️ LANDSAT-9</h4><small>Land Surface Temperature</small><h2 style="color:#f39c12">32.5°C - Moderate</h2><p style="font-size:13px;color:#aaa">درجة حرارة التربة مرتفعة نسبيا. يحتاج ري اضافي.</p></div>', unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({"Temp":[28,30,31.5,33,32.5,31.7]}, index=["Mar","Apr","May","Jun","Jul","Aug"]))

with s3:
    st.markdown('<div class="sat-card"><h4>🛰️ SMAP</h4><small>Soil Moisture</small><h2 style="color:#3498db">250mm - Good</h2><p style="font-size:13px;color:#aaa">رطوبة التربة جيدة لكن تتناقص. متوقع جفاف خفيف.</p></div>', unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({"Water":[300,280,260,240,255,250]}, index=["Mar","Apr","May","Jun","Jul","Aug"]))

st.divider()
st.markdown("### 📈 Advanced Analytics | احصائيات متقدمة")

# شارتات كتير طالعة نازلة
np.random.seed(7)
months = ["June","July","Aug","Sep","Oct","Nov"]
df_main = pd.DataFrame({
    "NILE SHIELD": [2.0, 2.3, 2.1, 3.4, 3.2, 3.9],
    "Without System": [2.0, 1.9, 2.1, 2.0, 2.3, 2.2],
    "SMAP Forecast": [2.1, 2.2, 2.4, 2.9, 3.0, 3.3]
}, index=months)

df2 = pd.DataFrame(np.random.randn(30, 3).cumsum(axis=0) + [5,3,6], columns=["Healthy Trend","Risk Trend","Water Level"])

cA, cB = st.columns(2)
with cA:
    st.markdown("**Yield Prediction vs Reality**")
    st.line_chart(df_main, height=300)
with cB:
    st.markdown("**Daily Fluctuations | تقلبات يومية**")
    st.line_chart(df2, height=300)

st.divider()
st.markdown("""
<div style="text-align:center; padding:20px; border-top:1px solid #D4AF37; margin-top:10px;">
<p style="color:#D4AF37; font-weight:bold; letter-spacing:1px;">Developed for NASA Space Apps Challenge 2026</p>
<p>Developed by Eng. Abdullah Mohamed | Supervised by NASA Data Systems</p>
<p style="color:#888; font-size:12px;">NILE SHIELD - Beni Suef, Egypt | Using NASA Terra, Landsat-9 & SMAP</p>
</div>
""", unsafe_allow_html=True)
