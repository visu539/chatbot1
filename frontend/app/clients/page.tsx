"use client"
import AuthGuard from '@/components/AuthGuard'
import api from '@/lib/api'
import { useQuery } from '@tanstack/react-query'
import { useState } from 'react'

export default function ClientsPage() {
  const [q, setQ] = useState('')
  const { data, refetch } = useQuery({
    queryKey: ['clients', q],
    queryFn: async () => (await api.get('/api/clients/', { params: { search: q, ordering: 'name' } })).data,
  })

  return (
    <AuthGuard>
      <main className="p-6 space-y-4">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold">Clients</h1>
          <div>
            <input placeholder="Search..." value={q} onChange={e => setQ(e.target.value)} className="border rounded px-3 py-1" />
            <button onClick={() => refetch()} className="ml-2 bg-black text-white px-3 py-1 rounded">Search</button>
          </div>
        </div>
        <div className="border rounded">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left border-b">
                <th className="p-2">Name</th>
                <th className="p-2">Email</th>
                <th className="p-2">Stage</th>
                <th className="p-2">Expected Investment</th>
              </tr>
            </thead>
            <tbody>
              {data?.map((c: any) => (
                <tr key={c.id} className="border-b last:border-0">
                  <td className="p-2">{c.name}</td>
                  <td className="p-2">{c.email}</td>
                  <td className="p-2">{c.stage}</td>
                  <td className="p-2">{c.expected_investment}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </AuthGuard>
  )
}