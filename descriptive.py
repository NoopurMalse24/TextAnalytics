import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Read data from CSV file
data = pd.read_csv('Reviews_Data.csv')

# Descriptive analysis
descriptive_stats = data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']].describe()
print(descriptive_stats)

# Convert non-numeric columns to numeric, ignoring errors
data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']] = data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']].apply(pd.to_numeric, errors='coerce')



# Visualize trends over time
plt.figure(figsize=(10, 6))
data['REVIEW_COUNT'].plot(label='Review Count')
plt.title('Trend of Review Count')
plt.xlabel('Index')
plt.ylabel('Review Count')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
data['PRICE'].plot(label='Price')
plt.title('Trend of Price')
plt.xlabel('Index')
plt.ylabel('Price')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
data[['PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']].plot()
plt.title('Trend of Ratings')
plt.xlabel('Index')
plt.ylabel('Rating')
plt.legend()
plt.show()




