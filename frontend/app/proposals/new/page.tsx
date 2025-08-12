"use client"
import AuthGuard from '@/components/AuthGuard'
import api from '@/lib/api'
import { useRouter } from 'next/navigation'
import { useState } from 'react'

export default function NewProposalPage() {
  const router = useRouter()
  const [clientId, setClientId] = useState('')
  const [items, setItems] = useState([{ fund_name: '', allocation_percent: 0 }])

  const addItem = () => setItems([...items, { fund_name: '', allocation_percent: 0 }])
  const updateItem = (idx: number, key: 'fund_name'|'allocation_percent', value: any) => {
    const next = [...items]
    ;(next[idx] as any)[key] = key === 'allocation_percent' ? Number(value) : value
    setItems(next)
  }

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await api.post('/api/proposals/', { client: Number(clientId), status: 'DRAFT', items })
    router.push(`/proposals/${res.data.id}`)
  }

  return (
    <AuthGuard>
      <main className="p-6 space-y-4 max-w-2xl">
        <h1 className="text-xl font-semibold">New Proposal</h1>
        <form onSubmit={onSubmit} className="space-y-4">
          <div>
            <label className="block text-sm mb-1">Client ID</label>
            <input value={clientId} onChange={e => setClientId(e.target.value)} className="border rounded px-3 py-2 w-full" />
          </div>
          <div className="space-y-2">
            {items.map((it, idx) => (
              <div key={idx} className="grid grid-cols-2 gap-2">
                <input placeholder="Fund Name" value={it.fund_name} onChange={e => updateItem(idx, 'fund_name', e.target.value)} className="border rounded px-3 py-2" />
                <input type="number" step="0.01" placeholder="Allocation %" value={it.allocation_percent} onChange={e => updateItem(idx, 'allocation_percent', e.target.value)} className="border rounded px-3 py-2" />
              </div>
            ))}
            <button type="button" onClick={addItem} className="text-sm text-blue-600">+ Add Fund</button>
          </div>
          <button className="bg-black text-white px-4 py-2 rounded">Save Draft</button>
        </form>
      </main>
    </AuthGuard>
  )
}