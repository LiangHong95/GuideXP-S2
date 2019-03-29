import React, { Component } from 'react';
import logo from './GuideXPLogo.PNG';
import './App.css';
//import GiudeXPLogo;

class App extends Component {

  render() {

    return (

      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Administrator Login</h2>
          <input type="text" id="username" value="Username" size="30"/>
          <br/>
          <input type="text" id="password" value="Password" size="30"/>
          <br/>
          <button onClick='clickAlert()'>Login</button>
                
        </header>
      </div>
    );
  }
}

export default App;
