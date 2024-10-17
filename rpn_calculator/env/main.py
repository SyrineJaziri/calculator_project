from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Data model for the calculation request
class CalculationRequest(BaseModel):
    expression: str 

# Initialize the FastAPI application
app = FastAPI()

# Set up CORS (Cross-Origin Resource Sharing) to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for Reverse Polish Notation (RPN) expression
class Operation(BaseModel):
    expression: List[str] # List of expression elements (numbers and operators)


# Function to calculate RPN expression
def rpn_calculate(expression: List[str]):
    stack = []
    for token in expression:
        if token.isdigit():  # If the token is a number, push it onto the stack
            stack.append(int(token))
        else:   # Otherwise, process the operator
            try:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:  # Check for division by zero
                        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
                    stack.append(a / b)
                else:
                    raise HTTPException(status_code=400, detail="Invalid operator")
            except IndexError: # Handle errors if the stack is empty
                raise HTTPException(status_code=400, detail="Invalid expression")
    if len(stack) != 1:  #If the stack does not contain exactly one element at the end, the expression is invalid
        raise HTTPException(status_code=400, detail="Invalid expression")
    return stack[0]

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('calculations.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS calculations
                    (id INTEGER PRIMARY KEY, expression TEXT, result REAL)''')
    conn.close()

init_db()

# Function to save calculation result to the database
def save_to_db(expression: str, result: float):
    conn = sqlite3.connect('calculations.db')
    conn.execute("INSERT INTO calculations (expression, result) VALUES (?, ?)", (expression, result))
    conn.commit()
    conn.close()

# Route to calculate RPN
@app.post("/calculate/")
async def calculate(operation: Operation):
    try:
        result = rpn_calculate(operation.expression)
        expression_str = " ".join(operation.expression)
        save_to_db(expression_str, result)
        return {"expression": expression_str, "result": result}
    except HTTPException as e:
        raise e

# Route to retrieve all calculated expressions
@app.get("/calculations/")
async def get_calculations():
    conn = sqlite3.connect('calculations.db')
    df = pd.read_sql_query("SELECT * FROM calculations", conn)
    conn.close()
    return df.to_dict(orient="records")


# Route to download calculations as CSV
@app.get("/calculations/csv/")
async def get_calculations_csv():
    conn = sqlite3.connect('calculations.db')
    df = pd.read_sql_query("SELECT * FROM calculations", conn)
    conn.close()
    csv_data = df.to_csv(index=False)
    return {"csv_data": csv_data}
