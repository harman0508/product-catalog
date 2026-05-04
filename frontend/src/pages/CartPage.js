import { useState } from "react";

/**
 * CartPage
 *
 * Client-side shopping cart using localStorage.
 * Respects inventory stock limits and reflects current prices.
 */
export default function CartPage({ cart, setCart }) {
  const [message, setMessage] = useState(null);

  const updateQty = (productId, newQty) => {
    setMessage(null);
    setCart((prev) =>
      prev.map((item) => {
        if (item.id !== productId) return item;
        const maxStock = item.inventory?.quantity ?? Infinity;
        if (newQty > maxStock) {
          setMessage(`Only ${maxStock} in stock for "${item.title}"`);
          return item;
        }
        if (newQty < 1) return item;
        return { ...item, qty: newQty };
      })
    );
  };

  const removeItem = (productId) => {
    setCart((prev) => prev.filter((item) => item.id !== productId));
  };

  const total = cart.reduce(
    (sum, item) => sum + parseFloat(item.price || 0) * item.qty,
    0
  );

  if (!cart.length) {
    return (
      <div>
        <h1>Shopping Cart</h1>
        <p>Your cart is empty.</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Shopping Cart</h1>
      {message && <p style={{ color: "orange" }}>{message}</p>}

      {cart.map((item) => (
        <div key={item.id} className="card" style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div>
            <strong>{item.title}</strong>
            <p>${item.price} × {item.qty} = ${(parseFloat(item.price || 0) * item.qty).toFixed(2)}</p>
          </div>
          <div>
            <button onClick={() => updateQty(item.id, item.qty - 1)}>−</button>
            <span style={{ margin: "0 10px" }}>{item.qty}</span>
            <button onClick={() => updateQty(item.id, item.qty + 1)}>+</button>
            <button onClick={() => removeItem(item.id)} className="btn-danger" style={{ marginLeft: 10 }}>Remove</button>
          </div>
        </div>
      ))}

      <div style={{ marginTop: 20, fontSize: "1.2em" }}>
        <strong>Total: ${total.toFixed(2)}</strong>
      </div>
    </div>
  );
}
