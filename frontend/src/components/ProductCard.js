export default function ProductCard({ product }) {
  return (
    <div className="card">
      <h3>
        {product.name}
        {product.featured && <span className="badge"> ⭐ Featured</span>}
      </h3>
      <p>Category: {product.category_name || product.category}</p>
      <p>Priority: {product.priority || "N/A"}</p>
      {product.inventory && (
        <p>Stock: {product.inventory.quantity}</p>
      )}
    </div>
  );
}
