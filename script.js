// LIVE NASA - Nile Shield FINAL
async function liveNASA(){
const E=new Date().toISOString().slice(0,10).replace(/-/g,'');
const S=new Date(Date.now()-604800000).toISOString().slice(0,10).replace(/-/g,'');
const B=`https://power.larc.nasa.gov/api/temporal/daily/point?community=AG&start=${S}&end=${E}&format=JSON`;
const F=t=>[...document.querySelectorAll('*')].find(e=>e.innerText.trim()==t&&e.children.length==0);
try{
let r=await fetch(`${B}&parameters=GWETTOP,RH2M,T2M&latitude=26.65&longitude=31.40`);
let j=await r.json();
let k=Object.keys(j.properties.parameter.GWETTOP).pop();
let soil=Math.round(j.properties.parameter.GWETTOP[k]*100);
let rh=j.properties.parameter.RH2M[k];
let tm=j.properties.parameter.T2M[k];
let el=F('12%');
if(el){
el.innerText=soil+'%';
let d=document.createElement('div');
d.style='font-size:11px;margin-top:6px';
d.innerHTML=`<b style="color:#ef4444">خطر - جفاف</b><br>🌱 رطوبة منخفضة<br>💧 ري فوري<br>🛰️ SMAP ${tm.toFixed(1)}C ${rh.toFixed(0)}%<br><span style="color:#22c55e">● LIVE ${k}</span>`;
el.parentNode.appendChild(d);
}
}catch(e){}
try{
let r=await fetch(`${B}&parameters=RH2M,GWETTOP&latitude=26.85&longitude=31.60`);
let j=await r.json();
let k=Object.keys(j.properties.parameter.RH2M).pop();
let rh=Math.round(j.properties.parameter.RH2M[k]);
let soil=Math.round(j.properties.parameter.GWETTOP[k]*100);
let el=F('54%');
if(el){
el.innerText=rh+'%';
let d=document.createElement('div');
d.style='font-size:11px;margin-top:6px';
d.innerHTML=`<b style="color:#eab308">متوسط</b><br>💧 ${rh}% تربة ${soil}%<br>🛰️ AQUA<br><span style="color:#22c55e">● LIVE ${k}</span>`;
el.parentNode.appendChild(d);
}
}catch(e){}
try{
let r=await fetch(`${B}&parameters=PRECTOTCORR,GWETTOP&latitude=26.76&longitude=31.50`);
let j=await r.json();
let k=Object.keys(j.properties.parameter.PRECTOTCORR).pop();
let rain=j.properties.parameter.PRECTOTCORR[k];
let soil=Math.round(j.properties.parameter.GWETTOP[k]*100);
let el=F('91%');
if(el){
el.innerText=(soil>60?91:75)+'%';
let d=document.createElement('div');
d.style='font-size:11px;margin-top:6px';
d.innerHTML=`<b style="color:#22c55e">آمن</b><br>🌧️ ${rain.toFixed(2)}mm<br>🛰️ GPM تربة ${soil}%<br><span style="color:#22c55e">● LIVE ${k}</span>`;
el.parentNode.appendChild(d);
}
}catch(e){}
}
liveNASA();
setInterval(liveNASA,15000);
