import pickle
import re
import tldextract

model = pickle.load(open("phishing_model.pkl","rb"))

def extract_features(url):

    features = []

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('='))

    if url.startswith("https"):
        features.append(1)
    else:
        features.append(0)

    ip_pattern = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
    if re.search(ip_pattern,url):
        features.append(1)
    else:
        features.append(0)

    ext = tldextract.extract(url)
    features.append(len(ext.subdomain))

    return features


def predict_url(url):

    features = extract_features(url)

    prediction = model.predict([features])[0]

    print("URL:",url)
    print("Features:",features)
    print("Prediction:",prediction)

    if prediction == 1:
        return "⚠️ Phishing Website"
    else:
        return "✅ Legitimate Website"
