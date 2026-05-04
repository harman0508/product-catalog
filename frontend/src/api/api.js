import axios from "axios";

/**
 * Axios instance for API communication.
 * Uses environment variable if available, otherwise falls back to localhost.
 */
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://127.0.0.1:8000/api",
  timeout: 5000
});

/**
 * Centralized error handler for API responses.
 */
const handleError = (error) => {
  if (error.response) {
    // Server responded with error status
    return new Error(
      error.response.data?.error?.detail ||
      error.response.data?.detail ||
      "Server error"
    );
  } else if (error.request) {
    // No response received
    return new Error("Network error - please check your connection");
  } else {
    // Unexpected error
    return new Error("Unexpected error occurred");
  }
};

/**
 * Fetch products with optional filters (search, category, pagination)
 */
export const getProducts = async (params = {}) => {
  try {
    const res = await api.get("/products/", { params });

    return {
      data: res.data.results || res.data,
      count: res.data.count || 0
    };

  } catch (error) {
    throw handleError(error);
  }
};

/**
 * Fetch all categories
 */
export const getCategories = async () => {
  try {
    const res = await api.get("/categories/");
    return res.data.results || res.data;
  } catch (error) {
    throw handleError(error);
  }
};

export default api;
