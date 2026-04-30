import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import Advisor from './pages/Advisor';

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/advisor" element={<Advisor />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}
