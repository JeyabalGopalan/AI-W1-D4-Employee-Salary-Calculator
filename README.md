# 💰 Employee Salary Calculator

A simple full-stack Python application that calculates an employee's salary using **FastAPI** as the backend and **Streamlit** as the frontend.

The application allows users to enter employee details through a simple web interface. Streamlit sends the information to the FastAPI backend, where the salary calculations are performed. The calculated results are then returned and displayed in the Streamlit application.

---

## 📌 Project Overview

This project demonstrates how a frontend application can communicate with a backend API.

### Frontend
**Streamlit**

Used to create the user interface where the employee enters:

- Employee Name
- Employee ID
- Basic Salary

### Backend
**FastAPI**

Receives the employee information, calculates:

- HRA
- DA
- Gross Salary
- Tax
- Net Salary

and returns the result as JSON.

---

## 🎯 Objective

The main objective of this project is to learn:

- FastAPI fundamentals
- REST API development
- Streamlit application development
- Frontend-to-backend communication
- JSON data handling
- API requests using Python
- Salary calculation logic
- Virtual environment management

---

# 🏗️ Project Architecture

```text
                 USER
                   │
                   ▼
          ┌─────────────────┐
          │    Streamlit    │
          │    Frontend     │
          └────────┬────────┘
                   │
                   │ HTTP POST
                   │ JSON Data
                   ▼
          ┌─────────────────┐
          │     FastAPI     │
          │     Backend     │
          └────────┬────────┘
                   │
                   ▼
          Salary Calculation
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
       Gross Salary       Tax
          │                 │
          └────────┬────────┘
                   ▼
              Net Salary
                   │
                   ▼
          JSON Response
                   │
                   ▼
          ┌─────────────────┐
          │    Streamlit    │
          │ Display Result  │
          └─────────────────┘
