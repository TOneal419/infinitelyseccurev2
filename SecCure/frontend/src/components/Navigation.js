import React, { Component } from "react";
import { render } from "react-dom";
// import '../../static/css/index.css';

export default class Navigation extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <React.Fragment>
      <div>
        <nav class="navbar navbar-default navbar-static-top navbar-inverse">
          <div class="container">
            <ul class="nav navbar-nav">
              <li class="active">
                <a href="/"><span class="glyphicon glyphicon-home"></span> Home</a>
              </li>
              <li>
                <a href="/learn.html">Learn</a>
              </li>
              <li>
                <a href="/virustotal.html">File/URL Check</a>
              </li>
              <li>
                <a href="/pwn.html">Pwn Check</a>
              </li>
              <li>
                <a href="/test.html">Test Yourself</a>
              </li>
            </ul>
          </div>
        </nav>
        <div>{this.props.children}</div>
        </div>
      </React.Fragment>
    )
  }
}
const navDiv = document.getElementById("navbar");
render(Navigation, navDiv);
