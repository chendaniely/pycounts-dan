from collections import Counter

words = ["a", "happy", "hello", "a", "world", "happy"]
word_counts = Counter(words)
word_counts

with open("zen.txt") as file:
  text = file.read()

text = text.lower()

from string import punctuation
punctuation

for p in punctuation:
  text = text.replace(p, "")

words = text.split()
words

word_counts = Counter(words)
word_counts
