import { useQuery } from '@tanstack/react-query'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'
import { api } from './api'

const cards = ['Student', 'Faculty', 'Placement', 'Admin', 'Analytics']

export default function App() {
  const { data } = useQuery({
    queryKey: ['students'],
    queryFn: async () => (await api.get('/students', { headers: { Authorization: '******' } })).data,
    retry: false,
  })

  const chartData = [{name:'S1',risk:0.2},{name:'S2',risk:0.7},{name:'S3',risk:0.4}]
  return (
    <main className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Aegis Campus AI Dashboards</h1>
      <div className="grid md:grid-cols-5 gap-4">
        {cards.map(c => <div key={c} className="rounded-lg bg-slate-800 p-4">{c}</div>)}
      </div>
      <div className="rounded-lg bg-slate-900 p-4">
        <h2 className="font-semibold mb-3">Dropout Risk Trend</h2>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData}><XAxis dataKey="name"/><YAxis/><Tooltip/><Line type="monotone" dataKey="risk" stroke="#38bdf8" /></LineChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div className="text-sm text-slate-400">Students loaded: {Array.isArray(data) ? data.length : 'API auth required'}</div>
    </main>
  )
}
