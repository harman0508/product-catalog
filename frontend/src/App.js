import { useState } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import ProductsPage from "./pages/ProductsPage";
import ProductDetailPage from "./pages/ProductDetailPage";
import ProductCreatePage from "./pages/ProductCreatePage";
import CartPage from "./pages/CartPage";
import ChecklistPage from "./pages/ChecklistPage";

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart((prev) => {
      const existing = prev.find((item) => item.id === product.id);
      if (existing) {
        const maxStock = product.inventory?.quantity ?? Infinity;
        if (existing.qty >= maxStock) {
          alert(`Only ${maxStock} in stock for "${product.title}"`);
          return prev;
        }
        return prev.map((item) =>
          item.id === product.id ? { ...item, qty: item.qty + 1 } : item
        );
      }
      return [...prev, { ...product, qty: 1 }];
    });
  };

  const cartCount = cart.reduce((sum, item) => sum + item.qty, 0);

  return (
    <BrowserRouter>
      <nav className="navbar">
        <Link to="/">Products</Link>
        <Link to="/products/new">Add Product</Link>
        <Link to="/cart">Cart ({cartCount})</Link>
        <Link to="/checklist">Checklist</Link>
      </nav>

      <div className="container">
        <Routes>
          <Route path="/" element={<ProductsPage onAddToCart={addToCart} />} />
          <Route path="/products/new" element={<ProductCreatePage />} />
          <Route path="/products/:id" element={<ProductDetailPage />} />
          <Route path="/cart" element={<CartPage cart={cart} setCart={setCart} />} />
          <Route path="/checklist" element={<ChecklistPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
