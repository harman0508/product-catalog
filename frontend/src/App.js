import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import ProductsPage from "./pages/ProductsPage";
import ChecklistPage from "./pages/ChecklistPage";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Products</Link> |{" "}
        <Link to="/checklist">Checklist</Link>
      </nav>

      <Routes>
        <Route path="/" element={<ProductsPage />} />
        <Route path="/checklist" element={<ChecklistPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;