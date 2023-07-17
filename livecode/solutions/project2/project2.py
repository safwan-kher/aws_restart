# Step 1: Import Necessary Libraries
import csv
import random

# Step 2: Read the CSV File
with open('project2/transaction_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Step 3: Create a List of Dictionaries
    transactions = []
    for row in reader:
        date, amount, merchant, card_number = row
        transaction = {date: {'amount': float(amount), 'merchant': merchant, 'card_number': card_number}}
        transactions.append(transaction)

# Step 4: Calculate and Print the Total Amount Spent
total_amount = sum(transaction[list(transaction.keys())[0]]['amount'] for transaction in transactions)
print(f'Total amount spent: ${total_amount:.2f}')

# Step 5: Calculate and Print the Average Amount per Transaction
average_amount = total_amount / len(transactions)
print(f'Average amount per transaction: ${average_amount:.2f}')

# Step 6: Print the Number of Transactions
print(f'Number of transactions: {len(transactions)}')

# Step 7: Select and Print a Random Transaction
random_transaction = random.choice(transactions)
print(f'Random transaction: {random_transaction}')