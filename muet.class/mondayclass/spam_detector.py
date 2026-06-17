# SPAM DETECTOR - Machine Learning Example

from sklearn.feature_extraction.text import CountVectorizer # change words to numbers
from sklearn.naive_bayes import MultinomialNB  # spam or normal

# STEP 1: Training Data (emails + labels)

# Yeh woh emails hain jin se model seekhega
emails = [
    "Win free money now! Click here to claim your prize",   
    "Hey, are we still meeting tomorrow at 3pm?"            
]

# 1 = spam,  0 = not spam (ham)
labels = [1, 0]

# STEP 2: Text ko Numbers 

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails) 

# STEP 3: Model banana aur train karna

# Naive Bayes - spam detection
model = MultinomialNB()
model.fit(X, labels)  # model ko emails aur unke labels deke train krte hen



# STEP 4: Naya Email deke Prediction lena

new_email = ["Hey, are you coming to the class tomorrow?"]

new_email_transformed = vectorizer.transform(new_email)

# Model se poochho: spam hai ya nahi?
prediction = model.predict(new_email_transformed)

# Result 

# Kya yeh email spam hai?
print("Spam ?", "Yes" if prediction[0] == 1 else "No")

