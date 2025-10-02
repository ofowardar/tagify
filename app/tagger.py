import re
from sklearn.feature_extraction.text import CountVectorizer
from typing import List

class TagExtractor:
    """
    Simple tag extractor class from notes.
    """
    def __init__(self, max_tags: int = 3):
        self.max_tags = max_tags
    
    def extract(self, text: str) -> List[str]:
        # Case Normalize
        text = text.lower()
        # Remove Punctuations
        text = re.sub(r"[^a-zçğıöşü\s]", "", text)
        # Vectorizer
        vectorizer = CountVectorizer(stop_words="english")
        X = vectorizer.fit_transform([text])
        words = vectorizer.get_feature_names_out()

        # Return high frequency = max_tags words
        return words[:self.max_tags].tolist() 

