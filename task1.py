import math
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
if num <= 1:
        print(f"{num} is not a prime number.")
else:
    is_prime = True
        
    for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        
    if is_prime:
            print(f"{num} is a prime number.")
    else:
            print(f"{num} is not a prime number.")
