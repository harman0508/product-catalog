import { render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import ProductsPage from "../pages/ProductsPage";
import * as api from "../api/api";

// Mock the API module
jest.mock("../api/api");

beforeEach(() => {
  api.getProducts.mockResolvedValue({ data: [], count: 0 });
  api.getCategories.mockResolvedValue([]);
});

test("renders product page title", async () => {
  render(
    <MemoryRouter>
      <ProductsPage />
    </MemoryRouter>
  );
  expect(screen.getByText(/Products/i)).toBeInTheDocument();
});

test("displays products from API", async () => {
  api.getProducts.mockResolvedValue({
    data: [{ id: 1, name: "Laptop", inventory: { quantity: 10 } }],
    count: 1,
  });

  render(
    <MemoryRouter>
      <ProductsPage />
    </MemoryRouter>
  );

  await waitFor(() => {
    expect(screen.getByText(/Laptop/)).toBeInTheDocument();
  });
});

test("displays error on API failure", async () => {
  api.getProducts.mockRejectedValue(new Error("Network error"));

  render(
    <MemoryRouter>
      <ProductsPage />
    </MemoryRouter>
  );

  await waitFor(() => {
    expect(screen.getByText(/Network error/)).toBeInTheDocument();
  });
});
