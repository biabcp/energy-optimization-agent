import React, { useEffect, useState } from 'react';
import axios from 'axios';
const api = axios.create({ baseURL: 'http://localhost:8000' });
export default function App(){
  const [summary,setSummary]=useState<any>({}); const [recs,setRecs]=useState<any[]>([]); const [answer,setAnswer]=useState(''); const [q,setQ]=useState('Which machine is wasting the most energy?');
  useEffect(()=>{api.get('/analytics/summary').then(r=>setSummary(r.data)); api.get('/recommendations').then(r=>setRecs(r.data.slice(0,5)));},[]);
  const ask=async()=>{const r=await api.post('/advisor/query',{question:q});setAnswer(r.data.answer)};
  return <div style={{fontFamily:'Arial',padding:20,background:'#f8fafc',color:'#334155'}}>
    <h1>Energy Optimization Agent</h1>
    <div>Total kWh: {summary.total_kwh} | Est. Monthly Cost: ${summary.estimated_cost} | Savings Opp: ${summary.monthly_savings_opportunity}</div>
    <h2>Top machines</h2><pre>{JSON.stringify(summary.top_machines,null,2)}</pre>
    <h2>Recommendations</h2>{recs.map((r,i)=><div key={i} style={{border:'1px solid #cbd5e1',background:'#fff',padding:8,marginBottom:8}}><b>{r.title}</b> ({r.priority}) - {r.recommended_action}</div>)}
    <h2>Energy Advisor</h2><input value={q} onChange={e=>setQ(e.target.value)} style={{width:'70%'}}/><button onClick={ask}>Ask</button><p>{answer}</p>
  </div>
}
