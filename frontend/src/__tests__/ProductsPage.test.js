import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import ProductsPage from "../pages/ProductsPage";
import * as api from "../api/api";

jest.mock("../api/api");

beforeEach(() => {
  api.getProducts.mockResolvedValue({ data: [], count: 0 });
  api.getCategories.mockResolvedValue([]);
});

afterEach(() => {
  jest.clearAllMocks();
});

const renderPage = () =>
  render(
    <MemoryRouter>
      <ProductsPage />
    </MemoryRouter>
  );

test("renders product page title", () => {
  renderPage();
  expect(screen.getByText(/Products/i)).toBeInTheDocument();
});

test("displays products from API", async () => {
  api.getProducts.mockResolvedValue({
    data: [
      {
        id: 1,
        title: "Laptop",
        category_name: "Electronics",
        price: "999.99",
        is_featured: true,
        priority: "high",
        inventory: { quantity: 10 },
      },
    ],
    count: 1,
  });

  renderPage();

  await waitFor(() => {
    expect(screen.getByText(/Laptop/)).toBeInTheDocument();
    expect(screen.getByText(/Stock: 10/)).toBeInTheDocument();
    expect(screen.getByText(/Featured/)).toBeInTheDocument();
    expect(screen.getByText(/Priority: high/)).toBeInTheDocument();
    expect(screen.getByText(/\$999.99/)).toBeInTheDocument();
  });
});

test("displays error on API failure", async () => {
  api.getProducts.mockRejectedValue(new Error("Network error"));

  renderPage();

  await waitFor(() => {
    expect(screen.getByText(/Network error/)).toBeInTheDocument();
  });
});

test("shows no products message for empty results", async () => {
  renderPage();

  await waitFor(() => {
    expect(screen.getByText(/No products available/)).toBeInTheDocument();
  });
});

test("renders category filter options", async () => {
  api.getCategories.mockResolvedValue([
    { id: 1, name: "Electronics" },
    { id: 2, name: "Books" },
  ]);

  renderPage();

  await waitFor(() => {
    expect(screen.getByText("Electronics")).toBeInTheDocument();
    expect(screen.getByText("Books")).toBeInTheDocument();
  });
});

test("search input triggers API call with query", async () => {
  renderPage();

  const input = screen.getByPlaceholderText("Search...");
  fireEvent.change(input, { target: { value: "Laptop" } });

  await waitFor(() => {
    expect(api.getProducts).toHaveBeenCalledWith(
      expect.objectContaining({ q: "Laptop" })
    );
  });
});

test("shows loading state", () => {
  api.getProducts.mockReturnValue(new Promise(() => {}));

  renderPage();

  expect(screen.getByText(/Loading/)).toBeInTheDocument();
});
