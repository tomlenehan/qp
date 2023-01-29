import React, {Component} from "react";
import ReactDOM from "react-dom";
import HomePage from "./HomePage";
import BillsPage from './BillsPage';
import MembersPage from './MembersPage';
import {BrowserRouter, Route} from 'react-router-dom';


export default class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <Route exact path="/" component={HomePage} />
            <Route path="/bills" component={BillsPage}/>
            <Route path="/members" component={MembersPage}/>
        </BrowserRouter>
    );
  }
}

const appDiv = document.getElementById("app");
ReactDOM.render(<App />, appDiv);
