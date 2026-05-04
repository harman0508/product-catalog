import { render, screen } from "@testing-library/react";
import ProductsPage from "../pages/ProductsPage";

test("renders product page title", () => {
  render(<ProductsPage />);
  expect(screen.getByText(/Products/i)).toBeInTheDocument();
});