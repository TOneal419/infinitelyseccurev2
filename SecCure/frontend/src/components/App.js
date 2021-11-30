import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import LearnPage from "./LearnPage";


export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return ( 
        <div>
            <HomePage />
            <LearnPage />
        </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);