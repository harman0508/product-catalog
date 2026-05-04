export default function ErrorMessage({ message }) {
  return (
    <div style={{ color: "red" }}>
      <strong>Error:</strong> {message}
    </div>
  );
}