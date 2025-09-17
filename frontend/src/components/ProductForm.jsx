import React, {useState} from 'react'
import axios from 'axios'

export default function ProductForm({onCreate}){
  const [sku,setSku]=useState('')
  const [name,setName]=useState('')
  const [price,setPrice]=useState('')

  const submit = async (e) =>{
    e.preventDefault()
    const payload = {sku, name, price_cost:0, price_sale: parseFloat(price)}
    const res = await axios.post('/api/v1/products', payload)
    onCreate(res.data)
    setSku(''); setName(''); setPrice('')
  }

  return (
    <div className="bg-white shadow rounded p-4">
      <h3 className="font-semibold mb-2">Novo Produto</h3>
      <form onSubmit={submit} className="space-y-2">
        <input className="w-full p-2 border rounded" placeholder="SKU" value={sku} onChange={e=>setSku(e.target.value)} />
        <input className="w-full p-2 border rounded" placeholder="Nome" value={name} onChange={e=>setName(e.target.value)} />
        <input className="w-full p-2 border rounded" placeholder="Preço" value={price} onChange={e=>setPrice(e.target.value)} />
        <button className="px-4 py-2 bg-indigo-600 text-white rounded" type="submit">Adicionar</button>
      </form>
    </div>
  )
}
