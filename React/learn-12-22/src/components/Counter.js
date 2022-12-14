import {Component} from 'react'

class Counter extends Component {
  constructor() {
    super();
    this.state = {
      likeCounter: 0,
    };
  }
  increment() {
    this.setState({ likeCounter: this.state.likeCounter + 1 });
  }
  decrement() {
    this.setState({ likeCounter: this.state.likeCounter - 1 });
  }
  render() {
    return (
      <div>
        <h3>{this.state.likeCounter} Likes</h3>
        <button onClick={() => this.increment()}>Like</button>
        <button onClick={() => this.decrement()}>DisLike</button>
      </div>
    );
  }
}

export default Counter