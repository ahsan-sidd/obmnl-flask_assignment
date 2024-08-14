# Import libraries
from flask import Flask, request, url_for, redirect, render_template
# Instantiate Flask functionality
app = Flask("CRUD Application Design Using Additional Features In Flask")
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation
@app.route("/", methods = ['GET'])
def get_transactions():
    balance = 0
    for txn in transactions:
        balance += txn['amount']
    return render_template("transactions.html",transactions = transactions,total_balance = balance)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        new_transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        transactions.append(new_transaction)
        return redirect(url_for("get_transactions"))

# Update operation
@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        for trans in transactions:
            if trans['id'] == transaction_id:
                trans['date'] == request.form['date']
                trans['amount'] == float(request.form['amount'])
                return redirect(url_for("get_transactions"))
    for trans in transactions:
        if trans['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=trans)
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>", methods = ["GET"])
def delete_transaction(transaction_id):
    for trans in transactions:
            if trans['id'] == transaction_id:
                transactions.remove(trans)
                return redirect(url_for("get_transactions"))

#search operation
@app.route("/search", methods = ["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = [txn for txn in transactions if min_amount <= float(txn["amount"]) <= max_amount]
        return render_template("transactions.html", transactions = filtered_transactions)
    return render_template("search.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)