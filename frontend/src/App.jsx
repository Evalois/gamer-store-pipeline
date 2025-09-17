import React from 'react'
import Dashboard from './pages/Dashboard'
export default function App(){
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-4">Lojinha Gamer — Dashboard</h1>
        <Dashboard />
      </div>
    </div>
  )
}
