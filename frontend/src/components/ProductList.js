import ProductCard from "./ProductCard";

export default function ProductList({ products, onAddToCart }) {
  if (!products.length) {
    return <p>No products available</p>;
  }

  return (
    <div>
      {products.map((p) => (
        <ProductCard key={p.id} product={p} onAddToCart={onAddToCart} />
      ))}
    </div>
  );
}
