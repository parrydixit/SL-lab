import functools #impppppppp
myFile = open("/Users/mac/MEGA/AD CN/[Coding Ninjas] Android App Development [Premium]/7. Kotlin Assignment/Assignment/1.0 Othello.txt")
text = myFile.read()

words = text.split(' ')
myFile.close()

freq = dict.fromkeys(words, 0)

for word in words :
	freq[word] += 1 

sortedFreqList = sorted(freq.items(), key = lambda item : item[1], reverse=True)
# print(sortedFreqList)

sortedFreq = sortedFreqList[:10]

print('top 10 frequent words')
print(sortedFreq)

wordLen = []

for word in sortedFreq:
	wordLen.append(len(word[0]))

print("Length of top 10 frequent words")
print(wordLen)

avgLen = reduce(lambda a,b : a+b, wordLen)/10
print('Avg of all word length is')
print(avgLen)

sqrLen = [x**2 for x in wordLen if x%2 != 0]
print('Square of odd positioned word length')
print(sqrLen)