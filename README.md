# hyperface_expense_tracker
This Streamlit app is a simple CRUD-based expense tracker. It allows users to add, view, update, and delete financial transactions stored in an SQLite database. The app also calculates and displays the current balance based on credit and debit records. I used Pandas for data handling, and created a clean UI with Streamlit’s forms, columns, and expanders. All DB operations are handled in a separate database.py file for modularity.

Follow these steps to run the project locally:

1. Clone the Repository
Edit
git clone https://github.com/LikithKumar24/hyperface_expense_tracker.git
cd expense-tracker

3. Create and Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
macOS/Linux

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run the App
streamlit run app.py
The app will open automatically in your default browser at http://localhost:8501.

Structure
expense-tracker
 app.py                # Streamlit frontend
database.py           # SQLite functions (CRUD operations)
 requirements.txt      # Required Python libraries
 README.md             # Project documentation
 .gitignore            # Files and folders to ignore in Git
