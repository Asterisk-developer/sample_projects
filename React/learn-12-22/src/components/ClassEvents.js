import { Component } from "react";
class ClassEvents extends Component {
    handleClick() {
    console.log("clicked class");
    
}
  render() {
    return <div>
        This is clas based component
        <button onClick={this.handleClick}></button>
    </div>;
  }
}

export default ClassEvents
