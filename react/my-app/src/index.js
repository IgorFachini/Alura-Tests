import React from "react"; // criar novos elementos
import ReactDOM from "react-dom"; // cria elemetos em memoria para simular o DOM
import "./index.css";
import App from "./App"; // importodando o modulo
import registerServiceWorker from "./registerServiceWorker";


// <App /> ira se tornar React.createElement(App)
ReactDOM.render(<App />, document.getElementById("root"));
registerServiceWorker();
