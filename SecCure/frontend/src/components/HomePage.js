import React, {Component} from 'react';
import PwnPage from "../components/PwnPage";
import LearnPage from "../components/LearnPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
          <HomePage/>
        );
    }
}
