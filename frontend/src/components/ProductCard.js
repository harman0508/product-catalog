export default function ProductCard({ product }) {
  return (
    <div className="card">
      <h3>{product.name}</h3>
      <p>Category: {product.category_name || product.category}</p>
      {product.inventory && (
        <p>Stock: {product.inventory.quantity}</p>
      )}
    </div>
  );
}