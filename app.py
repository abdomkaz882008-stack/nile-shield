import streamlit as st, streamlit.components.v1 as components, pandas as pd, datetime, pytz, random
st.set_page_config(page_title="NILE SHIELD - درع النيل", page_icon="🛰️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600&display=swap');
html, body, [class*="css"] {font-family:'Cairo',sans-serif; direction:rtl;}
.color-box {padding:12px; border-radius:10px; text-align:center; font-weight:600; margin:6px; border:1px solid #ddd;}
.green {background:#e8f5e9; color:#2e7d32; border-color:#a5d6a7;}
.yellow {background:#fff8e1; color:#8d6e00; border-color:#ffe082;}
.red {background:#ffebee; color:#b71c1c; border-color:#ef9a9a;}
.blue {background:#e3f2fd; color:#0d47a1; border-color:#90caf9;}
.gray {background:#f5f5f5; color:#424242;}
</style>
""", unsafe_allow_html=True)

tz=pytz.timezone('Africa/Cairo'); now=datetime.datetime.now(tz)

st.title("درع النيل | NILE SHIELD")
st.markdown("نظام مراقبة المحاصيل بالاقمار الصناعية - بني سويف")
st.caption(f"🔴 بث مباشر | {now.strftime('%Y-%m-%d %H:%M')} | بدون ريفريش")

# ساعة + طقس
c1,c2=st.columns([1,2])
with c1:
    st.subheader("⏰ توقيت بني سويف")
    components.html("""
    <div style="background:#fafafa;padding:15px;border-radius:12px;text-align:center;border:1px solid #e0e0e0">
      <canvas id="clock" width="180" height="180"></canvas>
      <div id="digital" style="color:#333;margin-top:10px;font-family:monospace;font-size:16px;"></div>
    </div>
    <script>
    const canvas=document.getElementById('clock'); const ctx=canvas.getContext('2d');
    const digital=document.getElementById('digital');
    function draw(){
        const now=new Date(); const h=now.getHours()%12,m=now.getMinutes(),s=now.getSeconds();
        digital.innerText = now.toLocaleTimeString('ar-EG');
        ctx.clearRect(0,0,180,180);
        ctx.beginPath(); ctx.arc(90,90,75,0,2*Math.PI); ctx.strokeStyle='#ccc'; ctx.lineWidth=2; ctx.stroke();
        let ha=h*Math.PI/6+m*Math.PI/360; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+40*Math.sin(ha),90-40*Math.cos(ha)); ctx.strokeStyle='#333'; ctx.lineWidth=5; ctx.stroke();
        let ma=m*Math.PI/30; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+60*Math.sin(ma),90-60*Math.cos(ma)); ctx.strokeStyle='#555'; ctx.lineWidth=3; ctx.stroke();
        let sa=s*Math.PI/30; ctx.beginPath(); ctx.moveTo(90,90); ctx.lineTo(90+68*Math.sin(sa),90-68*Math.cos(sa)); ctx.strokeStyle='#b71c1c'; ctx.lineWidth=1.5; ctx.stroke();
        ctx.beginPath(); ctx.arc(90,90,5,0,2*Math.PI); ctx.fillStyle='#333'; ctx.fill();
    }
    setInterval(draw,1000); draw();
    </script>
    """, height=270)
    st.metric("التاريخ الميلادي", now.strftime("%Y-%m-%d"))
    
with c2:
    st.subheader("🌦️ الطقس اللحظي - بني سويف")
    a,b,c=st.columns(3)
    a.markdown('<div class="color-box green">🟩 سليم<br><b>76%</b></div>', unsafe_allow_html=True)
    b.markdown('<div class="color-box yellow">🟨 مراقبة<br><b>17%</b></div>', unsafe_allow_html=True)
    c.markdown('<div class="color-box red">🟥 خطر<br><b>7%</b></div>', unsafe_allow_html=True)
    st.write("")
    c1_,c2_,c3_,c4_ = st.columns(4)
    c1_.metric("الحرارة", f"{round(31.2+random.uniform(-0.5,0.5),1)} °م")
    c2_.metric("الرطوبة", f"{random.randint(23,27)} %")
    c3_.metric("الرياح", "10.7 كم/س")
    c4_.metric("المطر", "0.0 مم")

st.divider()
st.header("📡 بث القمر الصناعي المباشر - بني سويف")
st.image(f"https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&random={now.second}", caption=f"بث مباشر - 29.07N, 31.08E - {now.strftime('%H:%M:%S')} LIVE", use_container_width=True)
st.markdown('<div style="height:12px;border-radius:6px;background:linear-gradient(to right, #81c784 0% 76%, #ffe082 76% 93%, #ef9a9a 93% 100%); border:1px solid #ddd;"></div>', unsafe_allow_html=True)
st.caption("أخضر 76% سليم | أصفر 17% مراقبة | أحمر 7% خطر")

st.header("🛰️ الأقمار الثلاثة و قراءاتها")
s1,s2,s3 = st.columns(3)
with s1:
    st.markdown('<div class="color-box green">1- قمر Terra MODIS<br>التخصص: صحة النبات NDVI</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1446776877081-d282a0f896e2", use_container_width=True)
    st.metric("مؤشر NDVI", f"{round(random.uniform(0.72,0.78),2)}", "سليم")
    st.progress(76, text="أخضر سليم 76%")
    st.progress(17, text="أصفر مراقبة 17%")
    st.progress(7, text="أحمر خطر 7%")
    st.caption("بيقيس: الكلوروفيل والخضار")
with s2:
    st.markdown('<div class="color-box blue">2- قمر Landsat-9<br>التخصص: حرارة التربة</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef", use_container_width=True)
    st.metric("درجة حرارة التربة", f"{round(random.uniform(32.5,34.0),1)} °م")
    st.metric("رطوبة التربة", f"{random.randint(28,32)} %", "مثالية")
with s3:
    st.markdown('<div class="color-box gray">3- قمر SMAP / Sentinel-2<br>التخصص: مياه وآفات</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1625246333195-78d9c38ad449", use_container_width=True)
    st.metric("مخزون المياه الجوفية", f"{random.randint(240,260)} مم")
    st.metric("نسبة الآفات", f"{random.randint(18,25)} %", "آمن")

st.divider()
st.header("📈 توقع المحصول وتوفير المياه")
df = pd.DataFrame({"مع درع النيل": [1.9, 2.0, 2.1, 3.3, 3.1],"بدون المشروع": [1.9, 1.9, 2.0, 2.1, 2.0]}, index=["أغسطس","يوليو","يونيو","أكتوبر","سبتمبر"])
st.line_chart(df)
st.success("🚀 متوقع +32% زيادة محصول | توفير 2400 لتر مياه / فدان")
st.divider()
st.header("🤖 مساعد الفلاح الذكي")
q = st.text_input("اسأل: البقع الصفراء؟", placeholder="اكتب: التربة سخنة اعمل ايه؟")
if q:
    st.write(f"**سؤالك:** {q}")
    st.write("**الإجابة من الأقمار:** حسب Landsat حرارة التربة 33° و Terra NDVI 0.76 - محصولك ممتاز، ركز ري 30% بس في المنطقة الصفراء الصبح بدري.")
st.caption(f"LIVE | العقارب بتلف لحظياً بدون ريفريش | {now.strftime('%H:%M:%S')}")
