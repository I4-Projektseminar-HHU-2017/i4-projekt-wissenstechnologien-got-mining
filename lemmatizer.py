from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
liste = ['kills', 'killing', 'slaughtered', 'beat', 'died']

for word in liste:
    output = wordnet_lemmatizer.lemmatize(word, pos='v')
    print(output)
