import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import (
    add_transaction, fetch_all_transactions, delete_transaction,
    update_transaction, get_expense_distribution, get_credit_debit_summary
)

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💰 Expense Tracker")


with st.form(key='add_form'):
    col1, col2 = st.columns(2)
    with col1:
        t_type = st.selectbox("Transaction Type", ["Credit", "Debit"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    with col2:
        date = st.date_input("Date")
        description = st.text_input("Description (e.g., Food, Rent, Salary)")
    submit_button = st.form_submit_button(label="Add Transaction")
    if submit_button:
        add_transaction(str(date), t_type, amount, description)
        st.success("Transaction added!")


st.subheader("📜 Transaction History")
data = fetch_all_transactions()
df = pd.DataFrame(data, columns=["ID", "Date", "Type", "Amount", "Description"])
st.dataframe(df, use_container_width=True)


if not df.empty:
    credit = df[df["Type"] == "Credit"]["Amount"].sum()
    debit = df[df["Type"] == "Debit"]["Amount"].sum()
    balance = credit - debit
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Credit", f"₹{credit:.2f}")
    col2.metric("Total Debit", f"₹{debit:.2f}")
    col3.metric("Balance", f"₹{balance:.2f}")


st.subheader("📊 Visual Insights")
col1, col2 = st.columns(2)


with col1:
    st.markdown("### Expense Distribution by Description")
    dist = get_expense_distribution()
    if dist:
        labels = [row[0] for row in dist]
        values = [row[1] for row in dist]
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
    else:
        st.info("No debit transactions yet.")


with col2:
    st.markdown("### Credit vs Debit")
    summary = get_credit_debit_summary()
    if summary:
        labels = [row[0] for row in summary]
        values = [row[1] for row in summary]
        fig2, ax2 = plt.subplots()
        ax2.bar(labels, values, color=['green', 'red'])
        ax2.set_ylabel("Amount")
        ax2.set_title("Credit vs Debit")
        st.pyplot(fig2)
    else:
        st.info("No transactions to visualize.")


with st.expander("🗑️ Delete Transaction"):
    id_to_delete = st.number_input("Enter ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        delete_transaction(id_to_delete)
        st.success(f"Transaction ID {id_to_delete} deleted!")


with st.expander("✏️ Edit Transaction"):
    id_to_edit = st.number_input("Enter ID to edit", min_value=1, step=1)
    new_date = st.date_input("New Date")
    new_type = st.selectbox("New Type", ["Credit", "Debit"])
    new_amount = st.number_input("New Amount", min_value=0.0, format="%.2f")
    new_description = st.text_input("New Description")
    if st.button("Update"):
        update_transaction(id_to_edit, str(new_date), new_type, new_amount, new_description)
        st.success(f"Transaction ID {id_to_edit} updated!")
