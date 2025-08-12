"use client"
import AuthGuard from '@/components/AuthGuard'
import api from '@/lib/api'
import { useQuery } from '@tanstack/react-query'

export default function AumReportPage() {
  const { data } = useQuery({
    queryKey: ['aum-by-client'],
    queryFn: async () => (await api.get('/api/reports/aum-by-client/')).data,
  })

  const exportCsv = () => {
    if (!data) return
    const headers = ['Client', 'Total AUM']
    const rows = data.map((d: any) => [d.client_name, d.total_aum])
    const csv = [headers, ...rows].map(r => r.join(',')).join('\n')
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = 'aum-by-client.csv'
    link.click()
  }

  return (
    <AuthGuard>
      <main className="p-6 space-y-4">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold">AUM by Client</h1>
          <button onClick={exportCsv} className="bg-black text-white px-3 py-1 rounded">Export CSV</button>
        </div>
        <div className="border rounded">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left border-b">
                <th className="p-2">Client</th>
                <th className="p-2">Total AUM</th>
              </tr>
            </thead>
            <tbody>
              {data?.map((d: any) => (
                <tr key={d.client_id} className="border-b last:border-0">
                  <td className="p-2">{d.client_name}</td>
                  <td className="p-2">{d.total_aum}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </AuthGuard>
  )
}