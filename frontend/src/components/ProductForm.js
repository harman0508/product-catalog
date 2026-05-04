import { useState, useEffect } from "react";
import { getCategories } from "../api/api";

export default function ProductForm({ initial, onSubmit, onCancel }) {
  const [form, setForm] = useState({
    title: "",
    description: "",
    category: "",
    price: "",
    priority: "medium",
    is_featured: false,
    image_url: "",
    ...initial,
  });
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    getCategories().then(setCategories).catch(() => {});
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form);
  };

  return (
    <form onSubmit={handleSubmit} className="product-form">
      <div className="form-group">
        <label>Title</label>
        <input name="title" value={form.title} onChange={handleChange} required />
      </div>
      <div className="form-group">
        <label>Description</label>
        <textarea name="description" value={form.description} onChange={handleChange} />
      </div>
      <div className="form-group">
        <label>Category</label>
        <select name="category" value={form.category} onChange={handleChange} required>
          <option value="">Select category</option>
          {categories.map((c) => (
            <option key={c.id} value={c.id}>{c.name}</option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label>Price</label>
        <input name="price" type="number" step="0.01" value={form.price} onChange={handleChange} required />
      </div>
      <div className="form-group">
        <label>Priority</label>
        <select name="priority" value={form.priority} onChange={handleChange}>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
          <option value="critical">Critical</option>
        </select>
      </div>
      <div className="form-group">
        <label>
          <input name="is_featured" type="checkbox" checked={form.is_featured} onChange={handleChange} />
          {" "}Featured
        </label>
      </div>
      <div className="form-group">
        <label>Image URL</label>
        <input name="image_url" value={form.image_url} onChange={handleChange} />
      </div>
      <div className="form-actions">
        <button type="submit" className="btn-primary">Save</button>
        {onCancel && <button type="button" onClick={onCancel} className="btn-secondary">Cancel</button>}
      </div>
    </form>
  );
}
