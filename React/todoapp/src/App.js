import Header from "./Components/Header";
import Forms from "./Components/Form";
import { useState } from "react";
function App() {
  const [todo, setTodo] = useState("");
  const [todoList, setTodoList] = useState([]);
  return (
    <div className="App">
      <Header />
      <Forms
        todo={todo}
        setTodo={setTodo}
        todoList={todoList}
        setTodoList={setTodoList}
      ></Forms>
    </div>
  );
}

export default App;
