"use client"
import AuthGuard from '@/components/AuthGuard'
import api from '@/lib/api'
import { useQuery } from '@tanstack/react-query'
import { useParams } from 'next/navigation'

export default function ProposalDetailPage() {
  const params = useParams<{ id: string }>()
  const id = params.id
  const { data } = useQuery({
    queryKey: ['proposal', id],
    queryFn: async () => (await api.get(`/api/proposals/${id}/`)).data,
  })

  const exportPdf = () => {
    window.open(`${process.env.NEXT_PUBLIC_API_URL}/api/proposals/${id}/export-pdf/`, '_blank')
  }

  return (
    <AuthGuard>
      <main className="p-6 space-y-4">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold">Proposal #{id}</h1>
          <button onClick={exportPdf} className="bg-black text-white px-3 py-1 rounded">Export PDF</button>
        </div>
        <div className="border rounded p-4 text-sm">
          <p><span className="text-gray-600">Status:</span> {data?.status}</p>
          <p><span className="text-gray-600">Client:</span> {data?.client}</p>
        </div>
        <div className="border rounded">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left border-b">
                <th className="p-2">Fund</th>
                <th className="p-2">Allocation %</th>
              </tr>
            </thead>
            <tbody>
              {data?.items?.map((it: any, idx: number) => (
                <tr key={idx} className="border-b last:border-0">
                  <td className="p-2">{it.fund_name}</td>
                  <td className="p-2">{it.allocation_percent}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </AuthGuard>
  )
}