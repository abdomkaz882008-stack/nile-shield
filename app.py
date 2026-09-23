import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random

st.set_page_config(page_title="NILE SHIELD - درع النيل", page_icon="🛰️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600&display=swap');
html, body, [class*="css"] {font-family:'Cairo',sans-serif;}
.color-box {padding:14px; border-radius:12px; text-align:center; font-weight:600; border:1px solid #ddd;}
.green {background:#e8f5e9; color:#2e7d32;}
.yellow {background:#fff8e1; color:#8d6e00;}
.red {background:#ffebee; color:#b71c1c;}
.blue {background:#e3f2fd; color:#0d47a1;}
.gray {background:#f5f5f5; color:#424242;}
.sat-card {background:white; border:1px solid #e0e0e0; border-radius:14px; padding:16px;}
.footer {text-align:center; padding:15px; background:#fafafa; border-radius:10px; margin-top:20px; color:#666;}
</style>
""", unsafe_allow_html=True)

st.title("درع النيل | NILE SHIELD")
st.caption("نظام مراقبة المحاصيل بالاقمار الصناعية | Satellite Monitoring - Live")

c1,c2 = st.columns([1,2])
with c1:
    st.markdown("**التوقيت | Time**")
    components.html("""
    <div style="background:#fff;padding:14px;border-radius:16px;text-align:center;border:3px solid #000">
      <canvas id="clock" width="200" height="200"></canvas>
      <div id="digital" style="color:#000;margin-top:8px;font-weight:bold;font-size:18px;font-family:monospace;"></div>
    </div>
    <script>
    const c=document.getElementById('clock'), ctx=c.getContext('2d'), d=document.getElementById('digital');
    function draw(){
        const n=new Date(); const h=n.getHours()%12,m=n.getMinutes(),s=n.getSeconds();
        d.innerText=n.toLocaleTimeString('en-GB');
        ctx.clearRect(0,0,200,200);
        ctx.beginPath(); ctx.arc(100,100,88,0,2*Math.PI); ctx.strokeStyle='#000000'; ctx.lineWidth=5; ctx.stroke();
        ctx.fillStyle='#000'; ctx.font='bold 18px Cairo'; ctx.textAlign='center';
        ctx.fillText('12',100,30); ctx.fillText('3',175,108); ctx.fillText('6',100,185); ctx.fillText('9',25,108);
        let ha=h*Math.PI/6+m*Math.PI/360; ctx.beginPath(); ctx.moveTo(100,100); ctx.lineTo(100+45*Math.sin(ha),100-45*Math.cos(ha)); ctx.strokeStyle='#000'; ctx.lineWidth=5; ctx.lineCap='round'; ctx.stroke();
        let ma=m*Math.PI/30; ctx.beginPath(); ctx.moveTo(100,100); ctx.lineTo(100+65*Math.sin(ma),100-65*Math.cos(ma)); ctx.strokeStyle='#333'; ctx.lineWidth=3; ctx.stroke();
        let sa=s*Math.PI/30; ctx.beginPath(); ctx.moveTo(100,100); ctx.lineTo(100+75*Math.sin(sa),100-75*Math.cos(sa)); ctx.strokeStyle='#c62828'; ctx.lineWidth=1.5; ctx.stroke();
        ctx.beginPath(); ctx.arc(100,100,7,0,2*Math.PI); ctx.fillStyle='#000'; ctx.fill();
    }
    setInterval(draw,1000); draw();
    </script>
    """, height=285)
with c2:
    st.markdown("**حالة الحقل | Field Status**")
    a,b,c = st.columns(3)
    a.markdown('<div class="color-box green">🟩 سليم<br>76%</div>', unsafe_allow_html=True)
    b.markdown('<div class="color-box yellow">🟨 مراقبة<br>17%</div>', unsafe_allow_html=True)
    c.markdown('<div class="color-box red">🟥 خطر<br>7%</div>', unsafe_allow_html=True)
    st.write("")
    x1,x2,x3,x4=st.columns(4)
    x1.metric("الحرارة", f"{round(31.7,1)} °م")
    x2.metric("الرطوبة", "26 %")
    x3.metric("الرياح", "10.7 km/h")
    x4.metric("المطر", "0.0 mm")

st.divider()
st.subheader("🛰️ قراءات الأقمار | Satellite Readings")
q1,q2,q3=st.columns(3)
with q1:
    st.markdown(f'<div class="sat-card"><div class="color-box green">1- Terra MODIS<br>NDVI</div><h2 style="text-align:center;color:#2e7d32;">{round(random.uniform(0.72,0.78),2)}</h2></div>', unsafe_allow_html=True)
with q2:
    st.markdown(f'<div class="sat-card"><div class="color-box blue">2- Landsat-9<br>Soil Temp</div><h2 style="text-align:center;color:#0d47a1;">{round(32.5,1)} °م</h2></div>', unsafe_allow_html=True)
with q3:
    st.markdown(f'<div class="sat-card"><div class="color-box gray">3- SMAP<br>Water</div><h2 style="text-align:center;">{random.randint(240,260)} mm</h2></div>', unsafe_allow_html=True)

st.divider()
st.subheader("📈 توقع المحصول | Yield Forecast")
df = pd.DataFrame({"NILE SHIELD": [2.0, 2.1, 2.2, 3
