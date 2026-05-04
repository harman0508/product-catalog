export default function Pagination({ count, page, setPage }) {
  const totalPages = Math.ceil(count / 10);

  if (totalPages <= 1) return null;

  return (
    <div>
      <button disabled={page === 1} onClick={() => setPage(page - 1)}>
        Prev
      </button>

      <span> Page {page} of {totalPages} </span>

      <button disabled={page === totalPages} onClick={() => setPage(page + 1)}>
        Next
      </button>
    </div>
  );
}