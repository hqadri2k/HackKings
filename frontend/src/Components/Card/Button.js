import React, { Component } from 'react';

class Button extends Component {
  render() {
    return (
      <button> <i className={this.props.like ? "fas fa-hand-holding-heart" : "fas fa-skull-crossbones"}></i> </button> 
    );
  }
}

export default Button;
