import React, { useState } from 'react';
import './Calculator.css'; 

// Calculator component
const Calculator = () => {
    const [expression, setExpression] = useState('');

    // Function to handle button clicks for numbers and operators
    const handleButtonClick = (value) => {
        setExpression((prev) => prev + value);
    };

    // Function to handle button clicks for numbers and operators
    const handleEspaceClick = (value) => {
      setExpression((prev) => prev + " ");
  };

  // Function to handle the calculation
    const handleCalculate = async () => {
        const expressionArray = expression.split(' ')
        const payload = { expression: expressionArray };

        try {
            // Sending a POST request to the backend API to calculate the result
            const response = await fetch('http://localhost:8000/calculate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });
            // Handling an unsuccessful response
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
             // Parsing the response from the API
            const data = await response.json();
            setExpression(data.result.toString());
        } catch (error) {
            // Error handling in case the fetch request fails or the expression is invalid
            console.error('Error fetching data:', error);
            setExpression('Error: Invalid Expression');
        }
    };

    // Function to clear the input (resetting the expression)
    const handleClear = () => {
        setExpression('');
    };
    // Rendering the calculator interface
    return (
        <div className="calculator">
            <h1>Calculator</h1>
            <div className="display">
                <input
                    type="text"
                    value={expression}
                    readOnly
                />
            </div>
            <div className="buttons">
                <div className="button-row">
                    <button onClick={() => handleButtonClick('1')}>1</button>
                    <button onClick={() => handleButtonClick('2')}>2</button>
                    <button onClick={() => handleButtonClick('3')}>3</button>
                    <button onClick={() => handleButtonClick('+')}>+</button>
                </div>
                <div className="button-row">
                    <button onClick={() => handleButtonClick('4')}>4</button>
                    <button onClick={() => handleButtonClick('5')}>5</button>
                    <button onClick={() => handleButtonClick('6')}>6</button>
                    <button onClick={() => handleButtonClick('-')}>-</button>
                </div>
                <div className="button-row">
                    <button onClick={() => handleButtonClick('7')}>7</button>
                    <button onClick={() => handleButtonClick('8')}>8</button>
                    <button onClick={() => handleButtonClick('9')}>9</button>
                    <button onClick={() => handleButtonClick('*')}>*</button>
                </div>
                <div className="button-row">
                    <button onClick={handleClear}>C</button>
                    <button onClick={() => handleButtonClick('0')}>0</button>
                    <button onClick={handleCalculate}>=</button>
                    <button onClick={() => handleButtonClick('/')}>/</button>
                </div>
                <div className="button-row">
                  <button className='space' onClick={handleEspaceClick}>
                    espace
                  </button>
                </div>
            </div>
        </div>
    );
};

export default Calculator;
