import React, { useEffect, useState } from 'react'
import axios from 'axios'
import InventoryTable from '../components/InventoryTable'
import ProductForm from '../components/ProductForm'

export default function Dashboard(){
  const [products, setProducts] = useState([])

  useEffect(()=>{
    axios.get('/api/v1/products').then(r=> setProducts(r.data)).catch(()=>{})
  },[])

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
      <div className="lg:col-span-2">
        <InventoryTable products={products} />
      </div>
      <div>
        <ProductForm onCreate={p => setProducts([p, ...products])} />
      </div>
    </div>
  )
}
