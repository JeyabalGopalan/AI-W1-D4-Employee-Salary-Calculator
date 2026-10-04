import streamlit as st
import requests


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Employee Salary Calculator",
    page_icon="💰",
    layout="centered"
)


# ==========================================
# PAGE TITLE
# ==========================================

st.title("💰 Employee Salary Calculator")

st.write(
    "Enter employee details below to calculate the salary."
)


# ==========================================
# INPUT FIELDS
# ==========================================

employee_name = st.text_input(
    "Employee Name"
)

employee_id = st.text_input(
    "Employee ID"
)

basic_salary = st.number_input(
    "Basic Salary",
    min_value=0.0,
    step=1000.0
)


# ==========================================
# CALCULATE BUTTON
# ==========================================

if st.button("Calculate Salary"):

    # Check whether all fields are entered
    if employee_name == "" or employee_id == "":

        st.warning("Please enter employee name and employee ID.")

    else:

        # ==========================================
        # CREATE DATA FOR FASTAPI
        # ==========================================

        data = {
            "name": employee_name,
            "employee_id": employee_id,
            "basic_salary": basic_salary
        }


        # ==========================================
        # SEND DATA TO FASTAPI
        # ==========================================

        api_url = "http://127.0.0.1:8000/calculate-salary"

        try:

            response = requests.post(
                api_url,
                json=data
            )


            # ==========================================
            # CHECK API RESPONSE
            # ==========================================

            if response.status_code == 200:

                result = response.json()


                # ==========================================
                # DISPLAY RESULT
                # ==========================================

                st.success("Salary calculated successfully!")


                st.subheader("📋 Salary Details")


                st.write(
                    f"**Employee Name:** {result['employee_name']}"
                )

                st.write(
                    f"**Employee ID:** {result['employee_id']}"
                )


                # ==========================================
                # SALARY METRICS
                # ==========================================

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Basic Salary",
                        f"₹{result['basic_salary']:,.2f}"
                    )

                    st.metric(
                        "HRA",
                        f"₹{result['hra']:,.2f}"
                    )

                    st.metric(
                        "DA",
                        f"₹{result['da']:,.2f}"
                    )


                with col2:

                    st.metric(
                        "Gross Salary",
                        f"₹{result['gross_salary']:,.2f}"
                    )

                    st.metric(
                        "Tax",
                        f"₹{result['tax']:,.2f}"
                    )

                    st.metric(
                        "Net Salary",
                        f"₹{result['net_salary']:,.2f}"
                    )


                # ==========================================
                # FINAL SALARY
                # ==========================================

                st.divider()

                st.success(
                    f"💵 Net Salary: ₹{result['net_salary']:,.2f}"
                )


            else:

                st.error(
                    f"API Error: {response.status_code}"
                )


        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI. "
                "Please make sure the FastAPI server is running."
            )