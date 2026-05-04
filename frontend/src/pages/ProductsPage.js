import { useEffect, useState } from "react";
import { getProducts, getCategories } from "../api/api";
import ProductList from "../components/ProductList";
import SearchBar from "../components/SearchBar";
import CategoryFilter from "../components/CategoryFilter";
import Loader from "../components/Loader";
import ErrorMessage from "../components/ErrorMessage";
import Pagination from "../components/Pagination";

export default function ProductsPage() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");
  const [page, setPage] = useState(1);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [count, setCount] = useState(0);

  const fetchData = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await getProducts({ q: query, category, page });
      setProducts(res.data);
      setCount(res.count);

      const cats = await getCategories();
      setCategories(cats);

    } catch (e) {
      setError(e.message);
    }

    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, [query, category, page]);

  return (
    <div>
      <h1>Product Catalog</h1>

      <SearchBar onSearch={setQuery} />
      <CategoryFilter categories={categories} onSelect={setCategory} />

      {loading && <Loader />}
      {error && <ErrorMessage message={error} />}

      {!loading && !error && (
        <>
          <ProductList products={products} />
          <Pagination count={count} page={page} setPage={setPage} />
        </>
      )}
    </div>
  );
}