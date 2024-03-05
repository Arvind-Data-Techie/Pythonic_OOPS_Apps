import streamlit as st
from banking_system import Bank

# Function to create bank object only once
@st.cache_resource
def load_bank():
    return Bank("Bank of Arvind")

# Create a global variable to store the bank object
bank = load_bank()

# Create a class to store session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Initialize session state
session_state = SessionState(created_account_numbers=[])

def main():
    st.title('The Bank of Arvind')

    global bank, session_state

    # Retrieve list of account numbers
    account_numbers = [account.account_number for account in bank.accounts.values()]

    st.write('Account Numbers:', account_numbers)

    # Checkbox for Create Account
    create_account_checkbox = st.checkbox("Create Account")
    if create_account_checkbox:
        account_number = st.text_input("Enter Account Number for Create Account")

        if st.button("Create Account"):
            if account_number in account_numbers:
                st.error("Account number already exists!")
            else:
                result = bank.create_account(account_number)
                st.write(result)
                session_state.created_account_numbers.append(account_number)

    # Checkbox for Deposit
    deposit_checkbox = st.checkbox("Deposit")
    if deposit_checkbox:
        account_number = st.text_input("Enter Account Number for Deposit")
        amount = st.number_input("Enter Amount to Deposit")

        if st.button("Deposit"):
            account = bank.get_account(account_number)
            if account=='Account not found':
                st.write("Account not found.")
            else:
                result = account.deposit(amount)
                st.write(result)

    # Checkbox for Withdraw
    withdraw_checkbox = st.checkbox("Withdraw")
    if withdraw_checkbox:
        account_number = st.text_input("Enter Account Number for Withdraw")
        amount = st.number_input("Enter Amount to Withdraw")

        if st.button("Withdraw"):
            account = bank.get_account(account_number)
            if account=='Account not found':
                st.write("Account not found.")
            else:
                result = account.withdraw(amount)
                st.write(result)


    # Checkbox for Display All Accounts
    display_accounts_checkbox = st.checkbox("Display All Accounts")
    if display_accounts_checkbox:
        if st.button("Display All Accounts"):
            result = bank.display_all_accounts()
            st.write(result)

    if st.button("Clear Database Session"):
        load_bank.clear()


if __name__ == "__main__":
    main()
