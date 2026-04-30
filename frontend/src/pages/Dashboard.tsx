import { useEffect, useState } from 'react';
import axios from 'axios';
import type { AnalyticsSummary, Recommendation } from '../types';

const api = axios.create({ baseURL: 'http://localhost:8000' });

export default function Dashboard() {
  const [summary, setSummary] = useState<AnalyticsSummary>({});
  const [recs, setRecs] = useState<Recommendation[]>([]);

  useEffect(() => {
    api.get('/analytics/summary').then((r) => setSummary(r.data));
    api.get('/recommendations').then((r) => setRecs(r.data.slice(0, 5)));
  }, []);

  return <>
    <div>Total kWh: {summary.total_kwh} | Est. Monthly Cost: ${summary.estimated_cost} | Savings Opp: ${summary.monthly_savings_opportunity}</div>
    <h2>Top machines</h2><pre>{JSON.stringify(summary.top_machines, null, 2)}</pre>
    <h2>Recommendations</h2>{recs.map((r, i) => <div key={i} style={{ border: '1px solid #cbd5e1', background: '#fff', padding: 8, marginBottom: 8 }}><b>{r.title}</b> ({r.priority}) - {r.recommended_action}</div>)}
  </>;
}
