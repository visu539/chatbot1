"use client"
import Link from 'next/link'

export default function Nav() {
  const logout = () => {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    window.location.href = '/login'
  }
  return (
    <nav className="border-b p-3 flex items-center gap-4 text-sm">
      <Link href="/dashboard">Dashboard</Link>
      <Link href="/clients">Clients</Link>
      <Link href="/reports/aum">Reports</Link>
      <Link href="/proposals/new">New Proposal</Link>
      <button onClick={logout} className="ml-auto text-red-600">Logout</button>
    </nav>
  )
}