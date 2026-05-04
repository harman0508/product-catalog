import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getProduct, updateProduct, deleteProduct } from "../api/api";
import ProductForm from "../components/ProductForm";
import Loader from "../components/Loader";
import ErrorMessage from "../components/ErrorMessage";

export default function ProductDetailPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);
  const [editing, setEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetch = async () => {
      try {
        const data = await getProduct(id);
        setProduct(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetch();
  }, [id]);

  const handleUpdate = async (form) => {
    try {
      const updated = await updateProduct(id, form);
      setProduct(updated);
      setEditing(false);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDelete = async () => {
    if (!window.confirm("Delete this product?")) return;
    try {
      await deleteProduct(id);
      navigate("/");
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) return <Loader />;
  if (error) return <ErrorMessage message={error} />;
  if (!product) return <p>Product not found</p>;

  if (editing) {
    return (
      <div>
        <h1>Edit Product</h1>
        <ProductForm
          initial={product}
          onSubmit={handleUpdate}
          onCancel={() => setEditing(false)}
        />
      </div>
    );
  }

  return (
    <div>
      <h1>{product.title} {product.is_featured && "⭐"}</h1>
      <p>{product.description}</p>
      <p>Category: {product.category_name}</p>
      <p>Price: ${product.price}</p>
      <p>Priority: {product.priority}</p>
      {product.inventory && <p>Stock: {product.inventory.quantity}</p>}
      {product.image_url && <img src={product.image_url} alt={product.title} style={{ maxWidth: 300 }} />}
      <div style={{ marginTop: 20 }}>
        <button onClick={() => setEditing(true)} className="btn-primary">Edit</button>{" "}
        <button onClick={handleDelete} className="btn-danger">Delete</button>{" "}
        <button onClick={() => navigate("/")} className="btn-secondary">Back</button>
      </div>
    </div>
  );
}
