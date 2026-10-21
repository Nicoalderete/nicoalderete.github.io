'use strict';
const english = document.documentElement.lang === 'en';
const text = (es, en) => english ? en : es;
// Deliberately fictional data, authored for this public portfolio demonstration.
const churnSample = [
  ['S01','personal',30],['S02','personal',60],['S03','personal',120],['S04','personal',240],
  ['S05','income',20],['S06','income',45],['S07','income',75],['S08','income',180],
  ['S09','company',15],['S10','company',90],['S11','company',150],['S12','company',300]
];
const reasons = {personal:text('Motivos personales','Personal reasons'),income:text('Rentabilidad insuficiente','Insufficient profitability'),company:text('Decisión de la compañía','Company decision')};
const median = values => {const a=[...values].sort((x,y)=>x-y), n=a.length;return n ? (n%2 ? a[(n-1)/2] : (a[n/2-1]+a[n/2])/2) : null;};
const churn = document.querySelector('[data-churn-demo]');
if(churn){
  const update = () => {
    const selected=churn.querySelector('[data-reason]').value;
    const rows=churnSample.filter(r=>selected==='all'||r[1]===selected);
    churn.querySelector('[data-count]').textContent=String(rows.length);
    churn.querySelector('[data-median]').textContent=median(rows.map(r=>r[2])).toLocaleString(english?'en-GB':'es-AR')+' '+text('días','days');
    const early=rows.filter(r=>r[2]<90).length;
    churn.querySelector('[data-early]').textContent=early+'/'+rows.length;
    churn.querySelector('[data-churn-status]').textContent=text('Muestra ficticia: ','Fictional sample: ')+rows.length+text(' casos. El tamaño cambia con el filtro; no son tasas reales de churn.',' cases. The sample size changes with the filter; these are not real churn rates.');
    const tbody=churn.querySelector('[data-churn-rows]');tbody.replaceChildren();
    rows.forEach(row=>{const tr=document.createElement('tr');[row[0],reasons[row[1]],row[2]].forEach(v=>{const td=document.createElement('td');td.textContent=String(v);tr.append(td);});tbody.append(tr);});
  };
  churn.querySelector('[data-reason]').addEventListener('change',update);update();
}
const agenda=document.querySelector('[data-agenda-demo]');
if(agenda){
  const localDate=d=>[d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-');
  const sampleDate=new Date();sampleDate.setDate(sampleDate.getDate()+3);sampleDate.setHours(10,0,0,0);
  while(sampleDate.getDay()===0||sampleDate.getDay()===6)sampleDate.setDate(sampleDate.getDate()+1);
  const sampleValue=localDate(sampleDate), locale=english?'en-GB':'es-AR';
  const dateInput=agenda.querySelector('[data-date]');dateInput.value=sampleValue;
  agenda.querySelector('[data-existing]').textContent=text('Reserva ficticia existente: DEMO01, ','Existing fictional booking: DEMO01, ')+sampleDate.toLocaleDateString(locale)+text(' a las 10:00. Probá DEMO02 para una unidad sin reserva.',' at 10:00. Try DEMO02 for a vehicle without a booking.');
  const weekKey=d=>{const w=new Date(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate()));w.setUTCDate(w.getUTCDate()-((w.getUTCDay()+6)%7));return w.toISOString().slice(0,10);};
  const update=()=>{
    const dateValue=dateInput.value,time=agenda.querySelector('[data-time]').value,vehicle=agenda.querySelector('[data-vehicle]').value;
    let msg='',valid=false;
    const proposed=new Date(dateValue+'T'+time+':00');
    if(!dateValue||Number.isNaN(proposed.getTime()))msg=text('Elegí una fecha válida.','Choose a valid date.');
    else if((proposed-new Date())/3600000<48)msg=text('Revisar: la solicitud no cumple 48 horas de anticipación.','Review: the request does not meet the 48-hour lead time.');
    else if([0,6].includes(proposed.getDay()))msg=text('Revisar: esta demo solo admite turnos de lunes a viernes.','Review: this demo only accepts Monday-to-Friday bookings.');
    else if(time==='18:00')msg=text('Revisar: el horario está fuera de los turnos de demostración.','Review: the time is outside the demonstration slots.');
    else if(vehicle==='DEMO01'&&weekKey(proposed)===weekKey(sampleDate))msg=text('Revisar: DEMO01 ya tiene una reserva en esa semana (lunes a domingo).','Review: DEMO01 already has a booking that week (Monday to Sunday).');
    else {valid=true;msg=text('Cumple las reglas de esta demo. No se creó ninguna reserva ni se verificó capacidad real.','Meets this demo’s rules. No booking was created and real capacity was not checked.');}
    const output=agenda.querySelector('[data-agenda-result]');output.dataset.valid=String(valid);output.textContent=msg;
  };
  agenda.querySelectorAll('input,select').forEach(el=>el.addEventListener('change',update));update();
}
const filters=[...document.querySelectorAll('[data-filter]')];
filters.forEach(button=>button.addEventListener('click',()=>{
  filters.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  let count=0;document.querySelectorAll('[data-category]').forEach(card=>{card.hidden=button.dataset.filter!=='all'&&card.dataset.category!==button.dataset.filter;if(!card.hidden)count++;});
  document.querySelector('#filter-status').textContent=count+text(' proyectos visibles',' projects shown');
}));
const dialog=document.querySelector('#image-dialog');
if(dialog){
  let trigger;
  document.querySelectorAll('[data-enlarge]').forEach(button=>button.addEventListener('click',()=>{
    trigger=button;const source=button.querySelector('img'),target=dialog.querySelector('img');target.src=source.src;target.alt=source.alt;dialog.showModal();
  }));
  dialog.querySelector('[data-close-dialog]').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
  dialog.addEventListener('close',()=>trigger?.focus());
}
