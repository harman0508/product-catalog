export default function ProductCard({ product }) {
  return (
    <div className="card">
      <h3>
        {product.title}
        {product.is_featured && <span className="badge"> ⭐ Featured</span>}
      </h3>
      <p>Category: {product.category_name || product.category}</p>
      <p>Price: ${product.price}</p>
      <p>Priority: {product.priority || "N/A"}</p>
      {product.inventory && (
        <p>Stock: {product.inventory.quantity}</p>
      )}
    </div>
  );
}
