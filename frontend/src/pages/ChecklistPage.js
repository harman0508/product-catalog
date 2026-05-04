import { useState } from "react";

const sections = [
  {
    title: "Product Management Features",
    items: [
      "Improve product listing layout",
      "Implement product detail view",
      "Add product creation form",
      "Add product creation form (Backend submitting the add form updates the models/table on the backend)",
      "Implement product edit functionality",
      "Implement product edit functionality (Backend edit submit form updates the model on the backend)",
      "Implement product deletion",
      "Implement product deletion (Backend delete submit form updates the models/table on the backend)",
    ],
  },
  {
    title: "Shopping Cart Features",
    items: [
      "Add products to cart",
      "View cart contents",
      "Update product quantities in cart",
      "Add a quantity field to products model and restrict the cart additions based on available stock (Backend & Frontend)",
      "Remove products from cart",
      "When a product price is updated, the cart should reflect the changes",
    ],
  },
  {
    title: "UI/UX Nice to Haves",
    items: [
      "Design responsive layout",
      "Add loading states and spinners",
      "Implement error handling and toast notifications",
      "Add pagination for product list",
      "Create featured products carousel",
      "Add product image gallery",
    ],
  },
];

export default function ChecklistPage() {
  const [checked, setChecked] = useState({});
  const [openSection, setOpenSection] = useState(0);

  const toggle = (key) => {
    setChecked((prev) => ({ ...prev, [key]: !prev[key] }));
  };

  return (
    <div>
      <h1>🚀 Product Showcase - Development Assignment</h1>
      <p style={{ color: "#666", marginBottom: 20 }}>Task list for building this application</p>

      {sections.map((section, si) => (
        <div key={si} className="card" style={{ marginBottom: 10 }}>
          <div
            onClick={() => setOpenSection(openSection === si ? -1 : si)}
            style={{ cursor: "pointer", padding: 15, fontWeight: "bold", background: "#f8f9fa" }}
          >
            {openSection === si ? "▼" : "▶"} {section.title}
          </div>
          {openSection === si && (
            <div style={{ padding: 15 }}>
              {section.items.map((item, ii) => {
                const key = `${si}-${ii}`;
                return (
                  <div key={key} style={{ padding: "8px 0", borderBottom: "1px solid #eee" }}>
                    <label>
                      <input
                        type="checkbox"
                        checked={!!checked[key]}
                        onChange={() => toggle(key)}
                        style={{ marginRight: 10 }}
                      />
                      {item}
                    </label>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
