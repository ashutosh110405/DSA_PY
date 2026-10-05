def reverse_words(sentence: str) -> str:
    # Reverses each word character-by-character as per the sheet's example
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Example usage:
print(reverse_words("the sky is blue"))  # Output: "eht yks si eulb"