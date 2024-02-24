from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import nltk
nltk.download('vader_lexicon')
import base64
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from io import BytesIO

app = Flask(__name__)

def generate_graphs(data):
    descriptive_stats = data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']].describe()

    # Convert non-numeric columns to numeric, ignoring errors
    data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']] = data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING']].apply(pd.to_numeric, errors='coerce')

    # Visualize trends over time
    plt.figure(figsize=(10, 6))
    plt.scatter(data['PRICE'], data['REVIEW_COUNT'])
    plt.title('Price vs. Review Count')
    plt.xlabel('Price')
    plt.ylabel('Review Count')
    plt.legend()
    plt.savefig('static/revieCountVSPrice.png')

# Price vs. Price Rating
    plt.figure(figsize=(10, 6))
    plt.scatter(data['PRICE'], data['PRICE_RATING'])
    plt.title('Price vs. Price Rating')
    plt.xlabel('Price')
    plt.ylabel('Price Rating')
    plt.legend()
    plt.savefig('static/priceVSPriceRating.png')

# Product Category vs. Review Count
    plt.figure(figsize=(10, 6))
    data.groupby('PRODUCT_CATEGORY')['REVIEW_COUNT'].sum().plot(kind='bar')
    plt.title('Product Category vs. Review Count')
    plt.xlabel('Product Category')
    plt.ylabel('Review Count')
    plt.legend()
    plt.savefig('static/pcvsrc.png')

# Product Category vs. Average Price
    plt.figure(figsize=(10, 6))
    data.groupby('PRODUCT_CATEGORY')['PRICE'].mean().plot(kind='bar')
    plt.title('Product Category vs. Average Price')
    plt.xlabel('Product Category')
    plt.ylabel('Average Price')
    plt.legend()
    plt.savefig('static/revieCountVSPrice.png')

# Review Date vs. Review Count
    data['REVIEW_DATE'] = pd.to_datetime(data['REVIEW_DATE'])
    plt.figure(figsize=(10, 6))
    data.groupby(data['REVIEW_DATE'].dt.to_period('M')).size().plot(kind='bar')
    plt.title('Review Date vs. Review Count')
    plt.xlabel('Review Date')
    plt.ylabel('Review Count')
    plt.legend()
    plt.savefig('static/rdvsrc.png')

# States vs. Review Count
    plt.figure(figsize=(10, 6))
    data.groupby('STATES')['REVIEW_COUNT'].sum().plot(kind='bar')
    plt.title('States vs. Review Count')
    plt.xlabel('States')
    plt.ylabel('Review Count')
    plt.legend()
    plt.savefig('static/statesvsrc.png')



# Product Category vs. Average Quality Rating
    plt.figure(figsize=(10, 6))
    data.groupby('PRODUCT_CATEGORY')['QUALITY_RATING'].mean().plot(kind='bar')
    plt.title('Product Category vs. Average Quality Rating')
    plt.xlabel('Product Category')
    plt.ylabel('Average Quality Rating')
    plt.legend()
    plt.savefig('static/pcvsavgqr.png')


    plt.figure(figsize=(10, 6))
    state_product_counts = data['STATES'].value_counts()
    state_product_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Products per State')
    plt.xlabel('State')
    plt.ylabel('Number of Products')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('static/novsstates.png')

    plt.figure(figsize=(10, 6))
    category_counts = data['PRODUCT_CATEGORY'].value_counts()
    category_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Products per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Products')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('static/novscat.png')


    plt.figure(figsize=(10, 6))
    data['PRICE'].hist(color='green', bins=20)
    plt.title('Number of Products per Price')
    plt.xlabel('Price')
    plt.ylabel('Number of Products')
    plt.legend()
    plt.savefig('static/novsp.png')

    plt.figure(figsize=(18, 6))
    data['PACK_SIZE'].hist(color='orange', bins=20)
    plt.title('Number of Products per Pack Size')
    plt.xlabel('Pack Size')
    plt.ylabel('Number of Products')
    plt.legend()
    plt.savefig('static/novss.png')


def tlf(data):
    data['tokenized_review'] = data['REVIEW_CONTENT'].apply(lambda x: word_tokenize(str(x)))

# Join tokenized words back into strings for vectorization
    data['cleaned_review'] = data['tokenized_review'].apply(lambda x: ' '.join(x))

# Bag-of-words
    count_vectorizer = CountVectorizer(stop_words='english')
    bow_matrix = count_vectorizer.fit_transform(data['cleaned_review'])

# TF-IDF
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['cleaned_review'])

# Identify high-frequency terms
    bow_word_freq = pd.DataFrame(bow_matrix.sum(axis=0), columns=count_vectorizer.get_feature_names_out()).T
    tfidf_word_freq = pd.DataFrame(tfidf_matrix.sum(axis=0), columns=tfidf_vectorizer.get_feature_names_out()).T

# Visualize key phrases using word clouds
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(bow_word_freq[0])
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of High-Frequency Terms (Bag-of-Words)')
    plt.show()
    plt.legend()
    plt.savefig('static/h1.png')

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(tfidf_word_freq[0])
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of High-Frequency Terms (TF-IDF)')
    plt.legend()
    plt.savefig('static/h2.png')

# Visualize high-frequency terms using bar charts
    top_n = 20
    plt.figure(figsize=(12, 6))
    bow_word_freq[0].sort_values(ascending=False).head(top_n).plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} High-Frequency Terms (Bag-of-Words)')
    plt.xlabel('Term')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()
    plt.legend()
    plt.savefig('static/h3.png')

    plt.figure(figsize=(12, 6))
    tfidf_word_freq[0].sort_values(ascending=False).head(top_n).plot(kind='bar', color='lightgreen')
    plt.title(f'Top {top_n} High-Frequency Terms (TF-IDF)')
    plt.xlabel('Term')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()
    plt.legend()
    plt.savefig('static/h4.png')

def clean_text(text):
    # Check if the input is a string or NaN
    if isinstance(text, str):
        # Remove special characters, punctuation, and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert text to lowercase
        text = text.lower()
        return text
    else:
        # If input is NaN, return an empty string
        return ''

def analyze_sentiment(data):
    sid = SentimentIntensityAnalyzer()
    data['cleaned_review'] = data['REVIEW_CONTENT'].apply(clean_text)
    data['sentiment_score'] = data['cleaned_review'].apply(lambda x: sid.polarity_scores(x)['compound'])

    # Visualize sentiment distribution
    plt.figure(figsize=(8, 6))
    data['sentiment_score'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.savefig('static/sentiment_distribution.png')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No file selected')
        if file:
            data = pd.read_csv(file)
            analysis_type = request.form['analysisType']
            if analysis_type == 'descriptive':
                generate_graphs(data)
                return render_template('result.html')
            elif analysis_type == 'tlk':
                tlf(data)
                return render_template('tlkresult.html')
            
            elif analysis_type=='senti':
                analyze_sentiment(data)
                return render_template('sentimentResult.html')
            
    return render_template('index.html', message='Upload failed')


if __name__ == '__main__':
    app.run(debug=True)
