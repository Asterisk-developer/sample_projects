function EventHandling() {
//   function handleClick() {
//     console.log("button is clicked");
//   }
  const handleClick=()=>{
    console.log("button is clicked");
  }
  return (
    <div>
      Functional component
      <button onClick={handleClick}>Click here</button>
    </div>
  );
}
export default EventHandling;
