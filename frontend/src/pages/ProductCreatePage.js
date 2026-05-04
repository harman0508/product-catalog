import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createProduct } from "../api/api";
import ProductForm from "../components/ProductForm";
import ErrorMessage from "../components/ErrorMessage";

export default function ProductCreatePage() {
  const navigate = useNavigate();
  const [error, setError] = useState(null);

  const handleSubmit = async (form) => {
    try {
      await createProduct(form);
      navigate("/");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h1>Add New Product</h1>
      {error && <ErrorMessage message={error} />}
      <ProductForm onSubmit={handleSubmit} onCancel={() => navigate("/")} />
    </div>
  );
}
