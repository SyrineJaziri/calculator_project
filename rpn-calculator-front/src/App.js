import React from 'react';
import Calculator from './Calculator';
import "./App.css"

const App = () => {
  return (
    <div>
      <h1 className="page-title">Calculatrice en notation polonaise inverse (NPI)</h1>
      <Calculator />
    </div>
  );
};

export default App;
