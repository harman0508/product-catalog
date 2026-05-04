import React from "react";

export default function ProductItem({ product }) {
  return (
    <div className="product-item">
      <h3>{product.name}</h3>
      {product.category && <p>Category: {product.category}</p>}
    </div>
  );
}