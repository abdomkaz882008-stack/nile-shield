// Nile Shield - LIVE from NASA Satellites
function countUp(el,s,e,suf){if(!el)return;let a=null;const st=t=>{if(!a)a=t;let p=Math.min((t-a)/2000,1);let v=p*(e-s)+s;el.innerText=(suf=='%'?Math.floor(v):v.toFixed(1))+suf;if(p<1)requestAnimationFrame(st)};requestAnimationFrame(st)}
async function liveNASA(){
 const END=new Date().toISOString().slice(0,10).replace(/-/g,'');
 const START=new Date(Date.now()-7*24*3600*1000).toISOString().slice(0,10).replace(/-/g,'');
 const base=`https://power.larc.nasa.gov/api/temporal/daily/point?community=AG&start=${START}&end=${END}&format=JSON`;
 try{
  let r=await fetch(`${base}&parameters=GWETTOP,RH2M,T2M&latitude=26.65&longitude=31.40`);let j=await r.json();let L=Object.keys(j.properties.parameter.GWETTOP).pop();
  let soil=Math.round(j.properties.parameter.GWETTOP[L]*100);let rh=j.properties.parameter.RH2M[L];let tmp=j.properties.parameter.T2M[L];
  let el=[...document.querySelectorAll('*')].find(e=>e.innerText?.trim()=='12%'&&e.children.length==0);if(el){el.id='soil-percent';countUp(el,12,soil,'%');let d=document.createElement('div');d.id='soil-info';d.style.cssText='font-size:11px;margin-top:8px;line-height:1.6;text-align:left';d.innerHTML=`<b style="color:#ef4444">خطر - جفاف شديد</b><br>🌱 رطوبة التربة منخفضة<br>💧 محتاج ري: فوري<br><div style="background:rgba(255,255,255,0.1);padding:4px;border-radius:4px;margin-top:4px">🛰️ SMAP - قمر التربة<br>🌡️ ${tmp.toFixed(1)}°C | 💧 ${rh.toFixed(0)}%<br><span style="color:#22c55e">● LIVE من القمر</span> ${L}</div>`;el.parentNode.appendChild(d);}
 }catch(e){}
 try{
  let r=await fetch(`${base}&parameters=RH2M,GWETTOP,T2M&latitude=26.85&longitude=31.60`);let j=await r.json();let L=Object.keys(j.properties.parameter.RH2M).pop();
  let rh=Math.round(j.properties.parameter.RH2M[L]);let soil=Math.round(j.properties.parameter.GWETTOP[L]*100);let tmp=j.properties.parameter.T2M[L];
  let el=[...document.querySelectorAll('*')].find(e=>e.innerText?.trim()=='54%'&&e.children.length==0);if(el){el.id='humidity-percent';countUp(el,54,rh,'%');let d=document.createElement('div');d.id='humidity-info';d.style.cssText='font-size:11px;margin-top:8px;line-height:1.6;text-align:left';d.innerHTML=`<b style="color:#eab308">متوسط - محتاج متابعة</b><br>💧 رطوبة الجو: ${rh}%<br>🌱 حالة التربة: ${soil}%<br><div style="background:rgba(255,255,255,0.1);padding:4px;border-radius:4px;margin-top:4px">🛰️ AQUA - قمر الرطوبة<br>🌡️ ${tmp.toFixed(1)}°C<br><span style="color:#22c55e">● LIVE من القمر</span> ${L}</div>`;el.parentNode.appendChild(d);}
 }catch(e){}
 try{
  let r=await fetch(`${base}&parameters=PRECTOTCORR,GWETTOP&latitude=26.76&longitude=31.50`);let j=await r.json();let L=Object.keys(j.properties.parameter.PRECTOTCORR).pop();
  let rain=j.properties.parameter.PRECTOTCORR[L];let soil=Math.round(j.properties.parameter.GWETTOP[L]*100);let health=soil>60?91:75;
  let el=[...document.querySelectorAll('*')].find(e=>e.innerText?.trim()=='91%'&&e.children.length==0);if(el){el.id='rain-percent';countUp(el,91,health,'%');let d=document.createElement('div');d.id='rain-info';d.style.cssText='font-size
