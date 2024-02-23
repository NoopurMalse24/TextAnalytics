import pandas as pd
from langdetect import detect
from googletrans import Translator
# import fasttext

def descriptive_analysis(df):
    new_df = df[["PRICE","REVIEW_COUNT","PRICE_RATING", "QUALITY_RATING","VALUE_RATING"]].copy()
    new_df = new_df.dropna()
    # print(new_df)
    new_df.to_csv("descriptive_sheet.csv")

def review_col(df):
    new_df = df[["REVIEW_CONTENT"]].copy()
    new_df = new_df.dropna()
    translator = Translator()

    for index in new_df.index:
        review = new_df["REVIEW_CONTENT"][index]
        try:
            language = detect(review)
        except:
            language = "unknown"
        if language ==  "hi" or language == 'so':
            translation = translator.translate(review, src=language, dest='en')
            # print(index,",",review,",",translation.text)
            new_df["REVIEW_CONTENT"][index] = translation.text
    # print(new_df)
    new_df.to_csv("review_col.csv")
        

def rating_analysis(df):
    new_df = df[["PRICE","PRICE_RATING"]]
    new_df = new_df.dropna()
    # print(new_df)
    new_df.to_csv("rating_analysis.csv")

def test_lang(df):
    model = fasttext.load_model('lid.176.bin')
    new_df = df[["REVIEW_CONTENT"]].copy()
    new_df = new_df.dropna()
    for index in new_df.index:
        review = new_df["REVIEW_CONTENT"][index]
        predictions = model.predict(review, k=1)  # k=1 means we want only the top prediction
        predicted_language = predictions[0][0].split('_')[-1]
        # print(language, confidence)
        if predicted_language != 'en':
            print(index,",",review,",",predicted_language)

if __name__ == "__main__":
    df = pd.read_csv("./Reviews Data.csv")
    # print(df) 
    descriptive_analysis(df)
    review_col(df)
    rating_analysis(df)
    # test_lang(df)