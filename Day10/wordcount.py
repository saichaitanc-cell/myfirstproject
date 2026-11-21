sentence = "the sensor reads the voltage and the ECU checks the voltage"
words = sentence.split()
counts = {}
for word in words:
    counts[word]=counts.get(word,0)+1

for word,num in counts.items():
    print(f"{word}:{num}")