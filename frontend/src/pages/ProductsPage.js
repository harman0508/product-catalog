import React, { useEffect, useState } from "react";
import { getProducts, getCategories } from "../api/api";

/**
 * ProductsPage
 * Displays product list with search, category filter, and pagination.
 */
function ProductsPage() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);

  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");

  const [page, setPage] = useState(1);
  const [totalCount, setTotalCount] = useState(0);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const pageSize = 10;

  /**
   * Fetch categories ONCE
   */
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await getCategories();
        setCategories(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchCategories();
  }, []);

  /**
   * Fetch products with debounce
   */
  useEffect(() => {
    const delay = setTimeout(() => {
      fetchProducts();
    }, 400);

    return () => clearTimeout(delay);
  }, [query, category, page]);

  /**
   * API call for products
   */
  const fetchProducts = async () => {
    setLoading(true);
    setError(null);

    try {
      const res = await getProducts({
        q: query,
        category: category,
        page: page,
      });

      setProducts(res.data);
      setTotalCount(res.count);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  /**
   * Reset page when search changes
   */
  const handleSearch = (value) => {
    setPage(1);  // ✅ FIX: reset pagination
    setQuery(value);
  };

  /**
   * Reset page when category changes
   */
  const handleCategory = (value) => {
    setPage(1);  // ✅ FIX: reset pagination
    setCategory(value);
  };

  const totalPages = Math.ceil(totalCount / pageSize);

  return (
    <div>
      <h1>Products</h1>

      {/* SEARCH */}
      <input
        type="text"
        placeholder="Search..."
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
      />

      {/* CATEGORY FILTER */}
      <select value={category} onChange={(e) => handleCategory(e.target.value)}>
        <option value="">All Categories</option>
        {categories.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name}
          </option>
        ))}
      </select>

      {/* LOADING */}
      {loading && <p>Loading...</p>}

      {/* ERROR */}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* PRODUCT LIST */}
      {!loading && !error && products.length === 0 && <p>No products found</p>}

      {!loading &&
        !error &&
        products.map((p) => (
          <div key={p.id}>
            <strong>{p.name}</strong> - Stock:{" "}
            {p.inventory?.quantity ?? "N/A"}
          </div>
        ))}

      {/* PAGINATION */}
      <div style={{ marginTop: "20px" }}>
        <button
          onClick={() => setPage((p) => Math.max(1, p - 1))}
          disabled={page === 1}
        >
          Prev
        </button>

        <span style={{ margin: "0 10px" }}>
          Page {page} of {totalPages || 1}
        </span>

        <button
          onClick={() => setPage((p) => p + 1)}
          disabled={page >= totalPages}
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default ProductsPage;