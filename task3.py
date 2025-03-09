# Task 3: Text Analysis Program

def countTokens(text: str) -> int:
    return len(text.split())

def countToken(text: str, token: str) -> int:
    return text.lower().split().count(token.lower())

def normalisedFrequency(text: str, token: str) -> float:
    total_tokens = countTokens(text)
    token_count = countToken(text, token)
    return token_count / total_tokens if total_tokens > 0 else 0

def sentenceCount(text: str) -> int:
    return text.count('.')

def sentencesContaining(text: str, token: str) -> list:
    sentences = text.split('.')
    return [sentence.strip() for sentence in sentences if token.lower() in sentence.lower()]

# Test function with the exact text
if __name__ == "__main__":
    text = "Hello, my name is Raja Babu Ray Yadav and my friend's name is Abishek."
    
    # Running each function and printing the results
    print("Total tokens:", countTokens(text))                        # Total tokens in the text
    print("Count of 'name':", countToken(text, "name"))               # Count of 'name'
    print("Normalized frequency of 'name':", normalisedFrequency(text, "name"))  # Normalized frequency of 'name'
    print("Number of sentences:", sentenceCount(text))                # Number of sentences in the text
    print("Sentences containing 'name':", sentencesContaining(text, "name"))  # Sentences containing 'name'
