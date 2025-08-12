"use client"
import AuthGuard from '@/components/AuthGuard'
import api from '@/lib/api'
import { useQuery } from '@tanstack/react-query'

export default function DashboardPage() {
  const { data } = useQuery({
    queryKey: ['dashboard-summary'],
    queryFn: async () => (await api.get('/api/dashboard/summary/')).data,
  })

  return (
    <AuthGuard>
      <main className="p-6 space-y-6">
        <h1 className="text-xl font-semibold">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="border rounded p-4"><div className="text-sm text-gray-600">Total Clients</div><div className="text-2xl">{data?.total_clients ?? '-'}</div></div>
          <div className="border rounded p-4"><div className="text-sm text-gray-600">Total AUM</div><div className="text-2xl">{data?.total_aum ?? '-'}</div></div>
          <div className="border rounded p-4"><div className="text-sm text-gray-600">Active SIPs</div><div className="text-2xl">{data?.active_sip_count ?? '-'}</div></div>
        </div>
        <section>
          <h2 className="font-medium mb-2">Recent Transactions</h2>
          <div className="border rounded">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left border-b">
                  <th className="p-2">Fund</th>
                  <th className="p-2">Type</th>
                  <th className="p-2">Units</th>
                  <th className="p-2">NAV</th>
                  <th className="p-2">Date</th>
                </tr>
              </thead>
              <tbody>
                {data?.recent_transactions?.map((t: any) => (
                  <tr key={t.id} className="border-b last:border-0">
                    <td className="p-2">{t.fund_name}</td>
                    <td className="p-2">{t.type}</td>
                    <td className="p-2">{t.units}</td>
                    <td className="p-2">{t.nav}</td>
                    <td className="p-2">{t.date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
        <section>
          <h2 className="font-medium mb-2">Alerts</h2>
          <ul className="list-disc pl-6 text-sm">
            {data?.alerts?.sip_expiring?.map((s: any) => (
              <li key={s.id}>SIP {s.fund_name} expires on {s.end_date}</li>
            ))}
          </ul>
        </section>
      </main>
    </AuthGuard>
  )
}