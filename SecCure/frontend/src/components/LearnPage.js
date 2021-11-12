import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";


export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <div>
            <LearnPage />
        </div>
        );
    }
}

const appDiv = document.getElementById("learn");
render(<learn />, learnDiv);
