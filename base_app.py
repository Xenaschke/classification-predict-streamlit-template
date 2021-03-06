"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Tweet Classifer")
	st.subheader("Climate change tweet classification")

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Prediction", "Data Insights", "App Overview", "Climate Change News"]
	selection = st.sidebar.selectbox("Choose Option", options)

	# Building out the "Information" page
	if selection == "App Overview":
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some info here")

	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")
		st.markdown("You can now choose which model you would like to try out (we reccomend the neural network though).")
        # Creating selection box to be able to choose a model
		model_option = st.selectbox('You can choose one of the following models:',['Logistic Regression','Naïve Bayes','Linear SVM (Support Vector Machine)','Random Forest','KNN (K Nearest Neighbors)','Neural Networks'])
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Text","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

# Building out the Climate Change News page
	if selection == "Climate Change News":
		st.info("What is climate change? How does it impact us? Am I to blame?")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

# Building out the Data Insights page
	if selection == "Data Insights":
		st.info("A few insights from the dataset.")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

		st.subheader("View visuals")
		if st.checkbox('Distribution of different classes for tweets'): # data is hidden if box is unchecked
			st.write()
        # if st.checkbox('Most common words'):
        #     st.write()


# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
	main()
