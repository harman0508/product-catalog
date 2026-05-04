import React, { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import { getProducts, getCategories } from "../api/api";
import SearchBar from "../components/SearchBar";
import CategoryFilter from "../components/CategoryFilter";
import ProductList from "../components/ProductList";
import Pagination from "../components/Pagination";
import Loader from "../components/Loader";
import ErrorMessage from "../components/ErrorMessage";

/**
 * ProductsPage
 *
 * Main page that composes reusable components for
 * search, filtering, listing, and pagination.
 */
function ProductsPage({ onAddToCart }) {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");
  const [page, setPage] = useState(1);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    getCategories().then(setCategories).catch((err) => setError(err.message));
  }, []);

  const fetchProducts = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await getProducts({ q: query, category, page });
      setProducts(res.data);
      setTotalCount(res.count);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [query, category, page]);

  useEffect(() => {
    const delay = setTimeout(() => fetchProducts(), 400);
    return () => clearTimeout(delay);
  }, [fetchProducts]);

  const handleSearch = (value) => { setPage(1); setQuery(value); };
  const handleCategory = (value) => { setPage(1); setCategory(value); };

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Products</h1>
        <Link to="/products/new" className="btn-primary">+ Add Product</Link>
      </div>

      <SearchBar onSearch={handleSearch} />
      <CategoryFilter categories={categories} onSelect={handleCategory} />

      {loading && <Loader />}
      {error && <ErrorMessage message={error} />}
      {!loading && !error && <ProductList products={products} onAddToCart={onAddToCart} />}

      <Pagination count={totalCount} page={page} setPage={setPage} />
    </div>
  );
}

export default ProductsPage;
