import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv(r'C:\Users\mkrti\OneDrive\Документы\Python projects\Source Data\msft.csv')

# Convert the 'Date' column to Datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the dataframe by Date
df = df.sort_values(by='Date')

# Set the display option to show all columns
pd.set_option('display.max_columns', None)

#Visually checking the data
print(df.head(10))
print(df.tail(10))

# Calculate daily returns using the 'Adj Close' column
df['daily_return'] = df['Adj Close'].pct_change()

# Drop the first row (NaN due to the percentage change)
df = df.dropna()

# Prepare data for regression
X = df[['Adj Close']]
y = df['daily_return']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred, squared=False))

# Plot the regression line
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Adj Close')
plt.ylabel('Daily Return')
plt.title('Linear Regression on MSFT Daily Returns')
plt.show()
