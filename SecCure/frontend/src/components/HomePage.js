import React, {Component} from 'react';
import PwnPage from "./PwnPage";
import LearnPage from "./LearnPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (<p>Hey from home</p>
            // <Router>
            //     <Switch>
            //         <Route exact path='/'><p>This is the homepage</p></Route>
            //         <Route path='/learn' Component={LearnPage}></Route>
            //         <Route path='/Pwn' Component={PwnPage}></Route>
            //     </Switch>
            // </Router>
        );
    }
}