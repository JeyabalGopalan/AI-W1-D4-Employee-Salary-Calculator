from fastapi import FastAPI
from pydantic import BaseModel


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(
    title="Employee Salary Calculator API",
    description="Simple API to calculate employee salary",
    version="1.0"
)


# ==========================================
# INPUT DATA MODEL
# ==========================================

class Employee(BaseModel):
    name: str
    employee_id: str
    basic_salary: float


# ==========================================
# SALARY CALCULATOR API
# ==========================================

@app.post("/calculate-salary")
def calculate_salary(employee: Employee):

    # --------------------------------------
    # Get basic salary
    # --------------------------------------

    basic_salary = employee.basic_salary


    # --------------------------------------
    # Calculate HRA
    # HRA = 20% of Basic Salary
    # --------------------------------------

    hra = basic_salary * 0.20


    # --------------------------------------
    # Calculate DA
    # DA = 10% of Basic Salary
    # --------------------------------------

    da = basic_salary * 0.10


    # --------------------------------------
    # Calculate Gross Salary
    # --------------------------------------

    gross_salary = basic_salary + hra + da


    # --------------------------------------
    # Calculate Tax
    # --------------------------------------

    if gross_salary <= 30000:

        tax = 0

    elif gross_salary <= 50000:

        tax = gross_salary * 0.05

    else:

        tax = gross_salary * 0.10


    # --------------------------------------
    # Calculate Net Salary
    # --------------------------------------

    net_salary = gross_salary - tax


    # --------------------------------------
    # Return Result
    # --------------------------------------

    return {
        "employee_name": employee.name,
        "employee_id": employee.employee_id,
        "basic_salary": round(basic_salary, 2),
        "hra": round(hra, 2),
        "da": round(da, 2),
        "gross_salary": round(gross_salary, 2),
        "tax": round(tax, 2),
        "net_salary": round(net_salary, 2)
    }