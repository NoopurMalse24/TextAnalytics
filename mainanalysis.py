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


def rating_analysis(data):
    # Remove commas from the string representation of numbers in the 'PRICE' column
    data['PRICE'] = data['PRICE'].str.replace(',', '')

    # Convert the 'PRICE' column to float
    data['PRICE'] = data['PRICE'].astype(float)

    # Assuming the column name is 'COLUMN_NAME'
    data['PACK_SIZE'] = data['PACK_SIZE'].str.replace('g', '').str.replace('ml', '')

    # Convert the column to float, ignoring errors
    data['PACK_SIZE'] = pd.to_numeric(data['PACK_SIZE'], errors='coerce')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='PRICE', y='REVIEW_COUNT', hue='PACK_SIZE', size='PRICE_RATING', sizes=(20, 200), alpha=0.7)
    plt.title('Price vs. Review Count')
    plt.xlabel('Price')
    plt.ylabel('Review Count')
    plt.legend()
    plt.savefig('static/price_vs_review_count.png')

    # Bubble plot: Price vs. Price Rating vs. Quality Rating
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='PRICE', y='PRICE_RATING', size='QUALITY_RATING', sizes=(20, 200), hue='PACK_SIZE', alpha=0.7)
    plt.title('Price vs. Price Rating vs. Quality Rating')
    plt.xlabel('Price')
    plt.ylabel('Price Rating')
    plt.legend()
    plt.savefig('static/price_vs_price_rating_vs_quality_rating.png')

    # Heatmap: Correlation between numerical features
    plt.figure(figsize=(10, 6))
    sns.heatmap(data[['PRICE', 'PRICE_RATING', 'QUALITY_RATING', 'VALUE_RATING', 'PACK_SIZE']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('static/correlation_heatmap.png')


def preprocess_text(text):
    # Check if the input is a string or NaN
    if isinstance(text, str):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
        return tokens
    else:
        return []  # Return an empty list for non-textual values


def perform_lda(data):
    # Preprocess text data
    data['cleaned_review'] = data['REVIEW_CONTENT'].apply(preprocess_text)

    # Convert text to list of strings
    cleaned_reviews = data['cleaned_review'].apply(' '.join)

    # Create Document-Term Matrix
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(cleaned_reviews)

    # Train LDA Model
    num_topics = 5
    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda_model.fit(dtm)

    # Get topics and their top words
    topics = []
    for idx, topic in enumerate(lda_model.components_):
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics.append((idx, top_words))

    return topics