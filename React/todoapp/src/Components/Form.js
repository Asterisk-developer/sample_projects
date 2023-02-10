import styles from "../style.module.css"
const Forms = ({todo,setTodo,todoList,setTodoList}) =>{
    const handleChange = (event) =>{
        setTodo(event.target.value)
        console.log(todo)
    }
    const handleSubmit =(event)=>{   
        console.log('hello') 
        event.preventDefault()    
        setTodoList([...todoList,todo])
        console.log(todoList)
    }
    return (
      <div className={styles.todoForm}>
        <form onSubmit={handleSubmit}>
          <input
            value={todo}
            onChange={handleChange}
            className={styles.itemform}
            placeholder="Add todo item"
          ></input>
          <button type="submit" className={styles.addButton}>Add Item</button>
        </form>
      </div>
    );
}
export default Forms