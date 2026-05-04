import { Link } from "react-router-dom";

export default function ProductCard({ product, onAddToCart }) {
  return (
    <div className="card">
      <h3>
        <Link to={`/products/${product.id}`}>{product.title}</Link>
        {product.is_featured && <span className="badge"> ⭐ Featured</span>}
      </h3>
      <p>Category: {product.category_name || product.category}</p>
      <p>Price: ${product.price}</p>
      <p>Priority: {product.priority || "N/A"}</p>
      {product.inventory && <p>Stock: {product.inventory.quantity}</p>}
      {onAddToCart && (
        <button onClick={() => onAddToCart(product)} className="btn-primary">
          Add to Cart
        </button>
      )}
    </div>
  );
}
