import Link from 'next/link'

export default function HomePage() {
  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="max-w-md w-full space-y-6 text-center">
        <h1 className="text-2xl font-semibold">Advisor MVP</h1>
        <p className="text-gray-600">Sign in to access your dashboard</p>
        <Link href="/login" className="inline-block rounded bg-black text-white px-4 py-2">Login</Link>
      </div>
    </main>
  )
}