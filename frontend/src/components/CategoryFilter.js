export default function CategoryFilter({ categories, onSelect }) {
  return (
    <select onChange={(e) => onSelect(e.target.value)}>
      <option value="">All Categories</option>
      {categories.map((c) => (
        <option key={c.id} value={c.id}>
          {c.name}
        </option>
      ))}
    </select>
  );
}