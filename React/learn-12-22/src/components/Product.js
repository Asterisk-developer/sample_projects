export default function Product() {
  const products = ["Mobile", "Computer"];

  return (
    <div>
      {products.map((item) => (
        <h3>{item}</h3>
      ))}
    </div>
  );
}
