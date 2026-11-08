sentence = str(input("Enter a short sentence : "))
splits = sentence.split()
word_count  = len(splits)
longest_word = max(splits ,key=len)
sentence_reversed = " ".join(splits[::-1])

print()

print(f"Sentence: {sentence}")
print(f"Word Count: {word_count}")
print(f"Longest word in the Sentence: {longest_word}")
print(f"Reversed sentence: {sentence_reversed}")

print()
num = int(input("Enter an Integar: "))
if num % 2 == 0:
    print(f"Number is Even: {num}")
else:
    print(f"Number is ODD: {num}")