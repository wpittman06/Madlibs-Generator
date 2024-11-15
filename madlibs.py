# open our story in read mode

with open("story.txt", "r") as f:
    story = f.read()

# create a set of our unique words

words = set()
startOfWord = -1

targetStart = "<"
targetEnd = ">"

# locates all our words insode of our story

for i, char in enumerate(story):
    if char == targetStart:
        startOfWord = i

    # if we found the ending bracket and found starting bracket we can #take the word and add it to word list
    
    if char == targetEnd and startOfWord != -1:
       
        #gives us the start and end of slice of a word we're adding 
        
        word = story[startOfWord: i + 1] 
        words.add(word)
        
        #found one whole word and now resetting startofword so were ready to to handle next word to find
       
        startOfWord = -1

# establishing a dictionarym replaces all instances of word with user answers

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)