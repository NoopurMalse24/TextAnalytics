import pandas as pd
from langdetect import detect
from translate import Translator
import time
# import fasttext

def descriptive_analysis(df):
    new_df = df[["PRICE","REVIEW_COUNT","PRICE_RATING", "QUALITY_RATING","VALUE_RATING"]].copy()
    new_df = new_df.dropna()
    # print(new_df)
    # new_df.to_csv("descriptive_sheet.csv")
    return new_df

def review_col(df):
    new_df = df[["REVIEW_CONTENT"]].copy()
    new_df = new_df.dropna()

    for index in new_df.index:
        # time.sleep(0.1)
        review = new_df.at[index, "REVIEW_CONTENT"]
        # print(review)
        try:
            language = detect(review)
        except:
            language = "unknown"
        try:
            if language ==  "hi":
                print(index,",",review)
                translator = Translator(to_lang='en', from_lang='hi')
                translation = translator.translate(review)
                print(translation)
                new_df["REVIEW_CONTENT"][index] = translation
        except Exception as e:
            print(f"Error translating review at index {index}: {e}")
    return new_df
    # new_df.to_csv("review_col.csv")
        

def rating_analysis(df):
    new_df = df[["PRICE","PRICE_RATING"]].copy()
    new_df = new_df.dropna()
    # print(new_df)
    # new_df.to_csv("rating_analysis.csv")
    return new_df

# def test_lang(df):
#     model = fasttext.load_model('lid.176.bin')
#     new_df = df[["REVIEW_CONTENT"]].copy()
#     new_df = new_df.dropna()
#     for index in new_df.index:
#         review = new_df["REVIEW_CONTENT"][index]
#         predictions = model.predict(review, k=1)  # k=1 means we want only the top prediction
#         predicted_language = predictions[0][0].split('_')[-1]
#         # print(language, confidence)
#         if predicted_language != 'en':
#             print(index,",",review,",",predicted_language)

    
df = pd.read_csv("./Reviews Data.csv")
descriptive_df = descriptive_analysis(df)
review_df = review_col(df)
print(review_df)
rating_df = rating_analysis(df)
# test_lang(df)