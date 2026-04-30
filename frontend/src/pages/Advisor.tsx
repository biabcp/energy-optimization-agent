import { useState } from 'react';
import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost:8000' });

export default function Advisor() {
  const [answer, setAnswer] = useState('');
  const [q, setQ] = useState('Which machine is wasting the most energy?');

  const ask = async () => {
    try {
      const r = await api.post('/advisor/query', { question: q });
      setAnswer(r.data.answer);
    } catch (e) {
      setAnswer('Sorry, the advisor encountered an error.');
    }
  };

  return <>
    <h2>Energy Advisor</h2>
    <input value={q} onChange={e => setQ(e.target.value)} style={{ width: '70%' }} />
    <button onClick={ask}>Ask</button>
    <p>{answer}</p>
  </>;
}
