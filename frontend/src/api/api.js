import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 5000
});

export const getProducts = async (params = {}) => {
  try {
    const res = await api.get("/products/", { params });

    return {
      data: res.data.results || res.data,
      count: res.data.count || 0
    };

  } catch (error) {
    if (error.response) {
      throw new Error(error.response.data.detail || "Server error");
    } else if (error.request) {
      throw new Error("Network error");
    } else {
      throw new Error("Unexpected error");
    }
  }
};

export const getCategories = async () => {
  const res = await api.get("/categories/");
  return res.data;
};