import streamlit as st

# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Function to calculate Compound Interest
def calculate_compound_interest(principal, rate, time):
    compound_interest = principal * (1 + rate / 100) ** time - principal
    return compound_interest

# Streamlit App
def main():
    st.title("Interest Calculator")

    principal = st.number_input("Enter Principal Amount:", min_value=0.0)
    rate = st.number_input("Enter Rate of Interest (%):", min_value=0.0)
    time = st.number_input("Enter Time (years):", min_value=0.0)

    if st.button("Calculate Interest"):
        simple_interest = calculate_simple_interest(principal, rate, time)
        compound_interest = calculate_compound_interest(principal, rate, time)

        st.write(f"Simple Interest: {simple_interest:.2f}")
        st.write(f"Compound Interest: {compound_interest:.2f}")

if __name__ == "__main__":
    main()
