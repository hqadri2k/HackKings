import React, { Component } from "react";

import Button from "./Button";

export default class Card extends Component {
  render() {
    return (
      <div class="card" style={{ width: "18rem" }}>
        <img
          class="card-img-top"
          src="https://www.cornwallbusinessawards.co.uk/wp-content/uploads/2017/11/dummy450x450.jpg"
          alt=""
        />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <div className="row">
            <Button />
            <Button like={true} />
          </div>
        </div>
      </div>
    );
  }
}
