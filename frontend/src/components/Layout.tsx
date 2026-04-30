import { Link } from 'react-router-dom';

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div style={{ fontFamily: 'Arial', padding: 20, background: '#f8fafc', color: '#334155' }}>
      <h1>Energy Optimization Agent</h1>
      <nav style={{ marginBottom: 16 }}>
        <Link to="/" style={{ marginRight: 12 }}>Dashboard</Link>
        <Link to="/advisor">Advisor</Link>
      </nav>
      {children}
    </div>
  );
}
