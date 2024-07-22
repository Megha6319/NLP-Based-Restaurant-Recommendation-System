###  NLP-Based Restaurant Recommendation System

Introduction

In the digital age, the abundance of choices can make finding the perfect restaurant an overwhelming task. With countless dining options available, how can one ensure they are making the best choice? This is where Recommendation Systems come into play. By harnessing the power of Natural Language Processing (NLP), we can transform the way users discover new restaurants.
Problem Statement
Design and implement a Recommendation System for restaurants based on customer reviews.
The goal is to develop a system that suggests restaurants to users based on their preferences and historical review data.

Problem Statement

Design and implement a Recommendation System for restaurants based on customer reviews.

The goal is to develop a system that suggests restaurants to users based on their preferences and historical review data.

Why

The purpose of creating a Restaurant Recommendation System based on customer reviews is to enhance user satisfaction by providing personalized dining suggestions and to drive business growth through data-driven insights and increased user engagement.
For instance, if you are visiting a new city and don't know where to eat, the system can analyze reviews from other customers with similar tastes and recommend the best restaurants for you. This not only ensures a great dining experience for you but also helps restaurants attract more customers through targeted recommendations.

What

Objective : Design and implement a recommendation system that analyzes customer reviews to suggest restaurants to users.
Components : Utilize data preprocessing, NLP Preprocessing, and Recommendation Algorithms to generate personalized restaurant recommendations.

How

Implementation of NLP techniques to analyze customer reviews.
The approach involves several key steps :
1. Data Collection and Preparation
2. Exploratory Data Analysis (EDA)
3. NLP Preprocessing
4. Feature Extraction
5. Topic Modelling
6. Recommendation Algorithm
7. Deployment and Integration

I will explore the step-by-step process of building an NLP-based Restaurant Recommendation System. From data collection and preprocessing to Recommendation Algorithms, I will delve into the technical details and methodologies that power this intelligent system.


Dataset Overview

To build my Recommendation System, I utilized the Restaurant Reviews Dataset sourced from Kaggle. The dataset, titled 10000 Restaurant Reviews, can be accessed here (https://www.kaggle.com/datasets/joebeachcapital/restaurant-reviews/data).

Structure of the Dataset

The dataset comprises 10,000 rows and includes 8 columns with the following attributes:
Restaurant : Name of the restaurant being reviewed.
Reviewer : Information about the reviewer, such as a unique identifier or username.
Review : Text of the review left by the reviewer.
Rating : Numerical rating given by the reviewer (typically on a scale from 1–5 stars).
Metadata : Additional information including details such as the number of reviews and number of followers.
Time : Timestamp or date when the review was posted.
Pictures : Number of pictures included in the review.
7514 : This column seems unusual and might be a placeholder or an error in the description.

In the following sections, I will preprocess this data to ensure it is clean and suitable for analysis. I will then apply various NLP techniques to extract insights and build my Recommendation Model.

Step 1 : Data Collection and Preparation

1. Column '7514' Removal :

The column '7514' has only one unique value (2447), and rest are blank values , neither of which contributes meaningful information to the dataset. To streamline further analysis and improve dataset relevance, the decision is made to remove column '7514' entirely. This action is justified as the column's content does not provide useful variability or contribute meaningfully to the analysis goals.

2. Handling Duplicated Rows :
I decided to drop the 36 duplicated rows from the dataset.

3. Handling Unexpected Values in 'Rating' Column :
The data in the Rating column contained the unexpected value "Like". I replaced the string 'Like' with mode_rating, which represents the most frequent value in the Rating column.

4. Data Type Adjustment for 'Rating' Column:
The 'Rating' column's data type is being changed from 'int' to 'float' to accommodate values like 4.5, 3.5, 2.5, and 1.5, which are decimal numbers.

5. Selection of Relevant Columns for NLP Processing:
I selected the columns 'Restaurant', 'Reviewer', 'Review', 'Rating', and 'Time' for NLP processing. This selection supports my goal of developing a recommendation system that suggests restaurants based on user preferences and historical review data, including timestamps.

Step 2 : Exploratory Data Analysis (EDA)

1. Distribution of Ratings :
The ratings in the dataset range from 1.0 to 5.0.
The highest rating observed is 5.0, with 3835 reviews.
The lowest rating observed is 1.5, with only 9 reviews.

2. Number of Reviews by Year :
The year 2018 had the highest number of reviews, totalling 4903.

3. Number of Reviews by Month:
May 2019 stands out with the highest number of reviews among all months, totalling 1349.

4. Restaurants with High Review Counts :
One restaurant has 78 reviews.
One restaurant has 86 reviews.
98 restaurants have 100 reviews each, indicating varying levels of popularity and customer engagement.

Step 3 : NLP Preprocessing
I. Tokenization and Text Cleaning
To prepare the 'Review' column for NLP analysis, I employed several preprocessing techniques:
URL Removal:

Utilized regex (url_regex = r'http\S+|www\S+') to identify and remove URLs from the text data. This ensures that web links do not interfere with the analysis of restaurant reviews.

2. Email Address Removal:
Employed regex (email_regex = r'\S+@\S+') to identify and remove email addresses from the text data, as they are not relevant to restaurant review analysis.

3. User Mention Removal:
Applied regex (user_regex = r'@\w+') to identify and remove user mentions (e.g., @username) from the text data. This step removes references to specific users that do not contribute to the restaurant review insights.

4. Non-Alphabetic Character Removal:
Implemented regex (general_pattern = r'[^a-zA-Z]') to replace all non-alphabetic characters in the 'Review' column with spaces. This includes special characters, digits, and punctuation marks, ensuring that only alphabetic tokens remain for further analysis.

Tokenization and Lowercasing

Normalized and tokenized the 'Review' column by:
  i. Converting all words to lowercase.
 ii. Splitting the text into individual tokens.
 iii. Replacing punctuation like commas and periods with spaces.
 iv. Removing extra spaces.
 
II. Remove stop words

Stop words refer to the frequently used words such as "the," "and," "is," and "in" that often don't carry significant meaning and can be filtered out to improve the processing efficiency or clarity of text.
To remove stop words from the tokenized 'Review' column, I utilized a standard stop words list from a natural language processing library such as NLTK (Natural Language Toolkit) in Python. This step helps focus on meaningful content words that carry more weight in the analysis and recommendation system.
"The words that were removed as stopwords include: the, was, which, for, a, one, can, also, with, and, or."
Removing stop words ensures that the processed text data contains only relevant content words, which is essential for accurate analysis and effective recommendation generation in the restaurant recommendation system.

III. Words that appear only once based on term frequency.

Hapexes - Hapaxes are words that appear only once in a dataset, indicating uniqueness and potentially limited relevance for broader analysis. Removing Hapaxes helps streamline the dataset by eliminating rare and often erroneous words.
Frequency -Frequency refers to the count of how often each word appears in the dataset, where Hapaxes specifically have a frequency count of 1.
There are 6727 words that appear only once.

I removed words that appeared only once (Hapaxes) from the dataset, including misspellings such as 'wrlcome', 'hhsjoibohoogogigivigigu', 'phtos', and others, were removed to improve the quality and focus of the text data for further analysis.

IV. Check the top 50 most frequent words based on document frequency.

Document Frequency - Document Frequency (DF) of a term indicates how many documents within a given dataset contain that term. 
This metric is valuable for understanding the prevalence and commonality of words across the corpus of restaurant reviews.
The term "good" has a document frequency of 7239, it means that out of the entire dataset, there are 7239 documents that include the word "good." This measure helps in understanding the commonality of a term within a corpus.
These frequently occurring words provide meaningful insights into the characteristics and attributes that reviewers frequently highlight when evaluating restaurants.

V. Stemming and Lemmatization

Stemming is the process of reducing words to their root form by removing suffixes, aiming to achieve this through heuristics rather than linguistic rules. It simplifies words to a base form but may not always result in a valid word.
Example : To stem the word "ambience," a stemming algorithm like Porter Stemmer might reduce it to "ambienc" based on heuristic rules.
Lemmatization, on the other hand, reduces words to their base or dictionary form using linguistic rules that consider the word's part of speech and apply morphological analysis to determine the correct base form. This approach ensures valid words are produced.
Example : For lemmatizing "ambience," a dictionary-based approach like WordNet Lemmatizer correctly identifies it as "ambience," considering its base or dictionary form.
Saving required outputs
For creating the vocabulary in my Recommendation System, I opted for lemmatized words due to its dictionary-based approach, which is generally considered superior to stemming. After alphabetically sorting the lemmatized words, I stored them in a vocab.txt file in dictionary format.
The vocab.txt file contains a dictionary with 6,865 words mapped to their corresponding numeric codes. These words range from "aalishaan" to "zucchini," ensuring comprehensive coverage of the vocabulary used in the system.

Step 4 : Feature Extraction

I. Count Vector Representation
In Natural Language Processing (NLP), a count vector is a sparse numerical representation of a document that captures the frequency of each term (word) it contains.
For instance, if a sentence includes the word "good" three times, the count vector would represent these frequencies in the document.

II. TF-IDF Vector Representation
TF-IDF (Term Frequency-Inverse Document Frequency) vectorization assigns weights to terms in a document based on their frequency within the document and rarity across a collection of documents. This approach facilitates nuanced document representation and enhances tasks such as information retrieval.
In TF-IDF vectorization, terms such as "Soumen" and "effective" stand out due to their higher weights, reflecting their significant presence within specific documents compared to their occurrence across the entire document collection.

III. Vector representation
The word "also," indexed as 158 in the vocabulary file, appears once in the sentence, indicating its presence in the vector representation. In contrast, the word "good," indexed as 2550, appears three times, underscoring its higher frequency within the sentence.
Saving required outputs
Here are two files: `rest_cVector`, which contains the count vectors, and `rest_tVector`, which contains the TF-IDF vectors.

Step 5 : Topic Modelling

Topic modeling serves as a powerful tool for uncovering latent themes within a corpus by examining patterns of word co-occurrence. 
By analyzing the top words associated with each topic and utilizing the topic probabilities saved in topic_probabilities.csv, profound insights emerge into the diverse thematic landscapes encapsulated within the dataset.
To visualize the top 5 words for each topic using a bar chart based on Reviews.
Extract Top Words: Retrieve the top 5 words for each topic from your topic modeling results.
Prepare Data: Organize these words and their associated topics into a format suitable for plotting.
Plotting: Use a bar chart to visually represent the frequency or importance of each word in its respective topic.

"In Topic 0, the prevalent term is 'good,' while 'food' stands out in both Topic 1 and Topic 3. Topic 2 emphasizes the term 'place,' and in Topic 4, 'chicken' is the prominent term."

Step 6 : Recommendation Algorithm: Collaborative Filtering
Collaborative filtering is a Recommendation Technique that predicts user preferences by finding similarities between users or items based on their interactions.

i. Creating a Super-Score Rating

The Super-Score is calculated based on a combination of the Rating and the length of the Review for each row in the DataFrame.
To develop a rating score that reflects each user's overall preference for a restaurant.

ii. Creating User-Item Matrix

One key component of collaborative filtering is the User-Item Matrix, which organizes user-item interactions into a structured format suitable for analysis and recommendation generation.

iii. Cosine Similarity

Cosine similarity is a measure used in natural language processing to determine the similarity between two non-zero vectors by calculating the cosine of the angle between them.
It ranges from -1 to 1, where 1 indicates identical vectors, 0 indicates orthogonal (completely dissimilar) vectors, and -1 indicates diametrically opposite vectors.

iv. Truncated SVD

Truncated SVD (Singular Value Decomposition) is a dimensionality reduction technique that approximates a large matrix by decomposing it into its singular vectors and selecting only the top components. This helps in reducing the computational complexity while preserving the essential structure and relationships within the data.

v. Item-Item Matrix

An Item-Item Matrix, also known as an Item-Item Similarity Matrix, is a matrix that measures the similarity between items (or products) based on user interactions. Unlike the User-Item Matrix, which focuses on user preferences for items, the Item-Item Matrix focuses on relationships between items themselves.

Results

Finally, we have reached our results, showcasing the Top 10 Recommended Restaurants for people who have previously visited Beyond Flavours.
Comparing the Super Score Ratings and Restaurants between Beyond Flavours and the 3 highest recommended restaurants.
Let's also explore the Top 10 Recommended Restaurants for people who have previously visited Paradise.
Comparing the Super Score Ratings and Restaurants between Paradise and the 3 highest recommended restaurants.

Step 7 : Deployment and Integration

Sign Up Page

The Sign-Up page allows new users to create an account on the NLP - Based Restaurant Recommendation System platform. To sign up, users need to provide the following details:
Username: Choose a unique username that will be used to identify your account.
Password: Create a secure password to protect your account. Ensure it is strong and includes a mix of letters, numbers, and special characters.
Email: Enter a valid email address where you can receive account-related notifications and updates.

Once the required information is provided, users can submit the form to create their account. If you already have an account, you can quickly navigate to the Login page to access your existing account.

Login Page

The Login page is designed for users who already have an account and wish to access their account. To log in, users need to provide:
Username: Enter the username associated with your account.
Password: Input the password that you created during sign-up.

After logging in, you'll be directed to the main page. Here, you can explore various features including personalized recommendations.
If you click on the "Recommended Restaurants for Beyond Flavours" button, you'll see a curated list of the Top 10 restaurants that are highly recommended for those who have previously dined at Beyond Flavours. This selection is based on preferences and dining patterns from other patrons of Beyond Flavours, ensuring you receive tailored suggestions for your next culinary adventure.
These are the Top 10 Recommended Restaurants that people should visit if they had previously visited Beyond Flavours.
Similarly, if you select the "Recommended Restaurants for Paradise" button, you'll be presented with a curated list of the top 10 restaurants highly recommended for those who have previously enjoyed dining at Paradise. This recommendation is tailored based on dining preferences and feedback from other patrons of Paradise, helping you discover new and exciting dining options that match your taste.
Top 10 Recommended Restaurants that people should visit if they had previously visited Paradise.

Conclusion

A restaurant recommender system utilizes customer similarity to suggest dining options based on their preferences. By analyzing patterns in user interactions with restaurants, these systems enhance user experience by offering personalized recommendations that align closely with individual tastes and interests. This approach not only increases customer satisfaction but also fosters engagement and loyalty by consistently delivering relevant dining choices.

Explore a website prototype here : https://megha6319.github.io/NLP-Based-Restaurant-Recommendation-System/


References

1. CateGitau. (2021). restaurant-recommendation-system. GitHub. https://github.com/CateGitau/restaurant-recommendation-system/tree/main
2. Priyanka. (2022). Restaurant Recommendation using collaborative filtering. Medium https://medium.com/@pu231195/restaurant-recommendation-using-collaborative-filtering-b5f7634c6534
