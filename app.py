import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="NILE SHIELD", layout="wide")
st.title("NILE SHIELD - درع النيل")

c1,c2=st.columns([1,2])
with c1:
 st.markdown("**Time | التوقيت**")
 components.html("""
 <div style="background:#fff;padding:12px;border-radius:16px;text-align:center;border:3px solid #000">
 <canvas id="clock" width="200" height="200"></canvas>
 <div id="d" style="color:#000;margin-top:8px;font-weight:bold;font-size:18px;font-family:monospace;"></div>
 </div>
 <script>
 const c=document.getElementById('clock'),x=c.getContext('2d'),d=document.getElementById('d');
 function draw(){
 const n=new Date(),h=n.getHours()%12,m=n.getMinutes(),s=n.getSeconds();
 d.innerText=n.toLocaleTimeString('en-GB');
 x.clearRect(0,0,200,200);
 x.beginPath();x.arc(100,100,88,0,6.28);x.strokeStyle='#000';x.lineWidth=5;x.stroke();
 x.fillStyle='#000';x.font='bold 18px Cairo';x.textAlign='center';
 x.fillText('12',100,30);x.fillText('3',175,108);x.fillText('6',100,185);x.fillText('9',25,108);
 let ha=h*0.523+m*0.0087;x.beginPath();x.moveTo(100,100);x.lineTo(100+45*Math.sin(ha),100-45*Math.cos(ha));x.strokeStyle='#000';x.lineWidth=5;x.lineCap='round';x.stroke();
 let ma=m*0.104;x.beginPath();x.moveTo(100,100);x.lineTo(100+65*Math.sin(ma),100-65*Math.cos(ma));x.strokeStyle='#333';x.lineWidth=3;x.stroke();
 let sa=s*0.104;x.beginPath();x.moveTo(100,100);x.lineTo(100+75*Math.sin(sa),100-75*Math.cos(sa));x.strokeStyle='#c62828';x.lineWidth=1.5;x.stroke();
 x.beginPath();x.arc(100,100,7,0,6.28);x.fillStyle='#000';x.fill();
 }
 setInterval(draw,1000);draw();
 </script>
 """,height=285)

with c2:
 st.markdown("**Field Status**")
 a,b,c=st.columns(3)
 a.metric("Healthy", "76%")
 b.metric("Watch", "17%")
 c.metric("Risk", "7%")

st.divider()
m=["June","July","Aug","Sep","Oct","Nov"]
df=pd.DataFrame({"NILE SHIELD":[2.0,2.1,2.2,3.1,3.3,3.5],"Without":[2.0,2.0,2.1,2.2,2.3,2.4]},index=m)
st.line_chart(df)
st.success("NILE SHIELD - Black Frame - Working 100%")
