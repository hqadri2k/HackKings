import React, { Component } from "react";

import Card from "./Card/Card";
import SidePanel from "./SidePanel/SidePanel";

class App extends Component {
  render() {
    return (
      <div className="App">
        <SidePanel />
        <Card />
      </div>
    );
  }
}

export default App;
