import {useState} from "react"
import Listitem from "./ListItem";
export default function Todo(){
    const [todo,setTodo] = useState("")
    const [todoList,setToDoList] = useState([])    
   const handleChange = (event) => {
        setTodo(event.target.value)        
      };
    const handleSubmit = (event) => {
      event.preventDefault();
      let tempList = todoList;
      tempList.push(todo);
      setToDoList(tempList);
      console.log(todoList)
      setTodo('')
    };

    return (
      <div>
        <form onSubmit={handleSubmit}>
          <input onChange={handleChange} value={todo} type="text"></input>
          <button type="submit">Add</button>
        </form>
        {todoList.map((item, index) => (
          <Listitem key={index} name={item}>         
          </Listitem>
        ))}
      </div>
    );
}