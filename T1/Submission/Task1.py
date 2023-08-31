import pandas as pd

# Provide the correct file path to your CSV file
csv_file_path = r'C:\Path\To\Your\Submission\transactions.csv'

# Read the CSV file into a Pandas dataframe
transactions_df = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe to verify the data has been loaded correctly
transactions_df.head()

column_names = transactions_df.columns.tolist()
print(column_names)

k = 5  
# Using the head() function to get the first k rows
first_k_rows = transactions_df.head(k)

# Display the first k rows
print(first_k_rows)

import random

k = 5  

# Using the sample() function to get a random sample of k rows
random_sample = transactions_df.sample(n=k, random_state=random.seed())

# Display the random sample
print(random_sample)

unique_transaction_types = transactions_df['type'].unique().tolist()
print(unique_transaction_types)

top_destinations = transactions_df['nameDest'].value_counts().head(10)
print(top_destinations)

fraudulent_transactions = transactions_df[transactions_df['isFraud'] == 1]
print(fraudulent_transactions)

import matplotlib.pyplot as plt

# Transaction types bar chart
transaction_type_counts = transactions_df['type'].value_counts()
plt.figure(figsize=(10, 6))
transaction_type_counts.plot(kind='bar')
plt.title('Transaction Types')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.show()

# Transaction types split by fraud bar chart
fraud_by_type = transactions_df.groupby(['type', 'isFraud']).size().unstack()
fraud_by_type.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Transaction Types Split by Fraud')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.legend(title='isFraud')
plt.show()


# Filter transactions for Cash Out type
cash_out_transactions = transactions_df[transactions_df['type'] == 'CASH_OUT']

# Calculate account balance deltas
origin_balance_delta = cash_out_transactions['oldbalanceOrg'] - cash_out_transactions['newbalanceOrig']
destination_balance_delta = cash_out_transactions['oldbalanceDest'] - cash_out_transactions['newbalanceDest']

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(origin_balance_delta, destination_balance_delta, alpha=0.5)
plt.title('Origin vs Destination Account Balance Delta for Cash Out Transactions')
plt.xlabel('Origin Account Balance Delta')
plt.ylabel('Destination Account Balance Delta')
plt.grid(True)
plt.show()

