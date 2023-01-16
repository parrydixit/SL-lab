vowels = ['a','e','i','o','u','A','E','I','O','U']

class stringReverse :
	wordDict = {}
	wordList = []
	sentance = ""

	def __init__(self, sentance):
		self.sentance = sentance

	def reverse(self):
		self.wordList = self.sentance.split(' ')
		self.wordList.reverse()
		revSen = ' '.join(self.wordList)
		return revSen

	def sort(self) :
		for word in self.wordList :
			count = 0 

			for char in word :
				if char in vowels:
					count += 1
			
			self.wordDict[word] = count 

		print(self.wordDict)

		#  self.wordDict.items() returns list of tupple(key, value), in 2nd parameter (key) touples are passed in the lambda
		print(self.wordDict.items())
		newList = sorted(self.wordDict.items(), key = lambda item : item[1], reverse = True)
		print('newList ' + str(newList))
		
		finalList = []
		for i in range(len(newList)): 
			finalList.append(newList[i][0])

		sortedWordList = ' '.join(finalList)
		return sortedWordList
		

mySent = stringReverse("My name is Bhagya")

reverseSent = mySent.reverse()
print(reverseSent)

sortedSent = mySent.sort()
print(sortedSent)