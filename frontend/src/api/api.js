import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://127.0.0.1:8000/api",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

const handleError = (error) => {
  if (error.response) {
    return new Error(
      error.response.data?.error?.detail ||
        error.response.data?.detail ||
        JSON.stringify(error.response.data?.error || error.response.data) ||
        "Server error"
    );
  } else if (error.request) {
    return new Error("Network error - please check your connection");
  }
  return new Error("Unexpected error occurred");
};

// --- Products ---

export const getProducts = async (params = {}) => {
  try {
    const res = await api.get("/products/", { params });
    return { data: res.data.results || res.data, count: res.data.count || 0 };
  } catch (error) {
    throw handleError(error);
  }
};

export const getProduct = async (id) => {
  try {
    const res = await api.get(`/products/${id}/`);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const getFeaturedProducts = async () => {
  try {
    const res = await api.get("/products/featured/");
    return res.data.results || res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const createProduct = async (data) => {
  try {
    const res = await api.post("/products/", data);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const updateProduct = async (id, data) => {
  try {
    const res = await api.put(`/products/${id}/`, data);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const patchProduct = async (id, data) => {
  try {
    const res = await api.patch(`/products/${id}/`, data);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const deleteProduct = async (id) => {
  try {
    await api.delete(`/products/${id}/`);
  } catch (error) {
    throw handleError(error);
  }
};

export const searchProducts = async (query) => {
  try {
    const res = await api.get("/products/", { params: { search: query, page_size: 20 } });
    return res.data.results || res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const toggleFeatured = async (id, isFeatured) => {
  return await patchProduct(id, { is_featured: isFeatured });
};

// --- Categories ---

export const getCategories = async () => {
  try {
    const res = await api.get("/categories/");
    return res.data.results || res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const getCategory = async (id) => {
  try {
    const res = await api.get(`/categories/${id}/`);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const createCategory = async (data) => {
  try {
    const res = await api.post("/categories/", data);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const updateCategory = async (id, data) => {
  try {
    const res = await api.put(`/categories/${id}/`, data);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export const deleteCategory = async (id) => {
  try {
    await api.delete(`/categories/${id}/`);
  } catch (error) {
    throw handleError(error);
  }
};

export const getCategoryProducts = async (id) => {
  try {
    const res = await api.get(`/categories/${id}/products/`);
    return res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export default api;
