import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { App } from './App.jsx';
import * as serviceWorker from './serviceWorker';
import { positions, Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";
import { BrowserRouter } from "react-router-dom";

const options = {
    timeout: 2500,
    position: positions.TOP_RIGHT,
    containerStyle: {
        zIndex: 10000
    }
};

const Root = () => (
    <BrowserRouter>
        <AlertProvider template={AlertTemplate} {...options}>
            <App />
        </AlertProvider>
    </BrowserRouter>
);

ReactDOM.render(<Root />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
