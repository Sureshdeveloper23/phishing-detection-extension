import pandas as pd
import re
import pickle
import tldextract
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("../dataset/phishing_dataset.csv")

# Feature extraction
def extract_features(url):

    features = []

    # URL length
    features.append(len(url))

    # number of dots
    features.append(url.count('.'))

    # number of hyphens
    features.append(url.count('-'))

    # special characters
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('='))

    # https presence
    if url.startswith("https"):
        features.append(1)
    else:
        features.append(0)

    # detect IP address
    ip_pattern = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
    if re.search(ip_pattern,url):
        features.append(1)
    else:
        features.append(0)

    # subdomain length
    ext = tldextract.extract(url)
    features.append(len(ext.subdomain))

    return features


# Extract features
X = []
for url in data['url']:
    X.append(extract_features(url))

y = data['label']

# Train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=30,
    random_state=42
)

model.fit(X_train,y_train)

# Accuracy
pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)

print("Model Accuracy:",accuracy)

# Save model
pickle.dump(model,open("phishing_model.pkl","wb"))

print("Model trained successfully")
