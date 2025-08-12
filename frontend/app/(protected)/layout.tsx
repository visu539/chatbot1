import Nav from '@/components/Nav'
import { ReactNode } from 'react'

export default function ProtectedLayout({ children }: { children: ReactNode }) {
  return (
    <div>
      <Nav />
      {children}
    </div>
  )
}