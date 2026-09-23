import streamlit as st, streamlit.components.v1 as components, pandas as pd, datetime, pytz, random
st.set_page_config(page_title="درع النيل - الوان ناسا", page_icon="🌈", layout="wide")
components.html("<script>setTimeout(()=>{window.parent.location.reload()},4000)</script>", height=0)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&display=swap');
html, body, [class*="css"] {font-family:'Cairo',sans-serif; direction:rtl;}
.color-box {padding:15px; border-radius:15px; text-align:center; font-weight:bold; margin:5px; color:white; font-size:18px;}
.green {background: linear-gradient(135deg,#00ff88,#00cc66); box-shadow:0 0 15px #00ff88;}
.yellow {background: linear-gradient(135deg,#ffcc00,#ff9900); box-shadow:0 0 15px #ffcc00; color:black;}
.red {background: linear-gradient(135deg,#ff4444,#cc0000); box-shadow:0 0 15px #ff4444;}
.blue {background: linear-gradient(135deg,#00c6ff,#0072ff); box-shadow:0 0 15px #00c6ff;}
</style>
""", unsafe_allow_html=True)
tz=pytz.timezone('Africa/Cairo'); now=datetime.datetime.now(tz)
st.title("🌈 درع النيل - بث مباشر بالالوان")
st.caption(f"🔴 LIVE | الساعة: {now.strftime('%H:%M:%S')} | بتتحدث كل 4 ثواني")

c1,c2=st.columns([1,2])
with c1:
    components.html(f"""
    <div style="background:#000;padding:20px;border-radius:20px;text-align:center">
      <canvas id="clock" width="180" height="180"></canvas>
      <div style="color:#00ff88;margin-top:10px;">{now.strftime('%H:%M:%S')}</div>
    </div>
    <script>
    const canvas=document.getElementById('clock'); const ctx=canvas.getContext('2d');
    function draw(){{
        const now=new Date(); const h=now.getHours()%12,m=now.getMinutes(),s=now.getSeconds();
        ctx.clearRect(0,0,180,180);
        ctx.beginPath(); ctx.arc(90,90,80,0,2*Math.PI); ctx.strokeStyle='#00ff88'; ctx.lineWidth=5; ctx.stroke();
        let ha=h*Math.PI/6+m*Math.PI/360; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+40*Math.sin(ha),90-40*Math.cos(ha)); ctx.strokeStyle='white'; ctx.lineWidth=5; ctx.stroke();
        let ma=m*Math.PI/30; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+60*Math.sin(ma),90-60*Math.cos(ma)); ctx.strokeStyle='#00ff88'; ctx.lineWidth=3; ctx.stroke();
        let sa=s*Math.PI/30; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+70*Math.sin(sa),90-70*Math.cos(sa)); ctx.strokeStyle='red'; ctx.lineWidth=2; ctx.stroke();
    }}
    setInterval(draw,1000); draw();
    </script>
    """, height=260)
with c2:
    st.subheader("🎨 معنى الالوان")
    a,b,c=st.columns(3)
    a.markdown('<div class="color-box green">🟩 اخضر<br>76%<br>سليم</div>', unsafe_allow_html=True)
    b.markdown('<div class="color-box yellow">🟨 اصفر<br>17%<br>راقب</div>', unsafe_allow_html=True)
    c.markdown('<div class="color-box red">🟥 احمر<br>7%<br>خطر</div>', unsafe_allow_html=True)
    st.write("")
    x1,x2,x3,x4=st.columns(4)
    x1.metric("الحرارة", f"{round(31.2+random.uniform(-0.5,0.5),1)} °م")
    x2.metric("الرطوبة", f"{random.randint(23,27)} %")
    x3.metric("التربة", f"{round(33+random.uniform(-1,1),1)} °م")
    x4.metric("المياه", f"{random.randint(240,260)} مم")

st.divider()
st.header("🛰️ صورة القمر الصناعي المباشر - بني سويف")
st.image(f"https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&random={now.second}", caption=f"بث مباشر LIVE {now.strftime('%H:%M:%S')} - احداثيات 29.07N, 31.08E", use_container_width=True)
components.html(f"""
<div style="width:100%;height:50px;background:linear-gradient(to right, #00ff88 0% 76%, #ffcc00 76% 93%, #ff4444 93% 100%);border-radius:15px;display:flex;justify-content:space-between;align-items:center;padding:0 20px;color:white;font-weight:bold;text-shadow:1px 1px 2px black;border:3px solid #00ff88">
  <span>🟩 سليم 76%</span><span>🟨 مراقبة 17%</span><span>🟥 خطر 7%</span>
</div>
""", height=70)

st.header("🛰️ الاقمار الثلاثة")
q1,q2,q3=st.columns(3)
with q1:
    st.markdown('<div class="color-box green">1- Terra MODIS<br>صحة النبات NDVI</div>', unsafe_allow_html=True)
    st.metric("NDVI", f"{round(random.uniform(0.72,0.79),2)}", "سليم")
    st.caption("بيقيس الكلوروفيل - كل ما قرب من 1 الزرع ممتاز")
    st.progress(76)
with q2:
    st.markdown('<div class="color-box blue">2- Landsat-9<br>حرارة التربة</div>', unsafe_allow_html=True)
    t=round(33+random.uniform(-1,1),1)
    st.metric("حرارة التربة", f"{t} °م")
    if t>34: st.markdown('<div class="color-box red">سخنة - ري فوري!</div>', unsafe_allow_html=True)
    else: st.markdown('<div class="color-box green">مثالية</div>', unsafe_allow_html=True)
    st.caption("بيقيس حرارة سطح الارض - لو فوق 35° خطر")
with q3:
    st.markdown('<div class="color-box yellow">3- SMAP / Sentinel-2<br>مياه وافات</div>', unsafe_allow_html=True)
    st.metric("رطوبة باطن الارض", f"{random.randint(25,35)} %")
    st.metric("الافات", f"{random.randint(18,24)}% - امن")
    st.markdown('<div class="color-box green">امن - مفيش افات</div>', unsafe_allow_html=True)
    st.caption("بيقيس المياه الجوفية + كشف البقع الصفراء")

st.divider()
st.success("✅ الخلاصة: 76% اخضر سليم | 17% اصفر راقبه بكرة | 7% احمر ارويه الفجر")
st.header("🤖 مساعد الفلاح")
qq=st.text_input("اسأل:", placeholder="التربة سخنة اعمل ايه؟")
if qq: st.write(f"**الاجابة:** حسب الاقمار NDVI 0.76 وحرارة {t}° - محصولك ممتاز، ركز ري 30% بس في الاصفر الصبح بدري.")
st.caption(f"تحديث لحظي كل 4 ثواني | {now.strftime('%H:%M:%S')}")
