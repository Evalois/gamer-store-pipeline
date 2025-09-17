import React from 'react'

export default function InventoryTable({products}){
  return (
    <div className="bg-white shadow rounded p-4">
      <h2 className="text-xl font-semibold mb-2">Estoque</h2>
      <table className="w-full text-left">
        <thead>
          <tr>
            <th>SKU</th>
            <th>Produto</th>
            <th>Preço</th>
          </tr>
        </thead>
        <tbody>
          {products.map(p => (
            <tr key={p.id} className="border-t">
              <td className="py-2">{p.sku}</td>
              <td>{p.name}</td>
              <td>R$ {Number(p.price_sale).toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
