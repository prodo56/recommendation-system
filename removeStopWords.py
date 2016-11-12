from nltk.corpus import stopwords
import re
import nltk
#test_samples=["I don't know if it's the cactus or the tequila or just the unique combination of ingredients, but the flavour of this hot sauce makes it one of a kind!  We picked up a bottle once on a trip we were on and brought it back home with us and were totally blown away!  When we realized that we simply couldn't find it anywhere in our city we were bummed.<br /><br />Now, because of the magic of the internet, we have a case of the sauce and are ecstatic because of it.<br /><br />If you love hot sauce..I mean really love hot sauce, but don't want a sauce that tastelessly burns your throat, grab a bottle of Tequila Picante Gourmet de Inclan."]
porter = nltk.PorterStemmer()
def removeStopWords(sentence):
	sentence = re.sub("<[a-z 0-9A-Z]*\/>","",sentence)
	#print sentence
	sentence=re.sub("\\[a-z]*","",sentence)
	tokens=nltk.word_tokenize(sentence)
	words = [w.lower() for w in tokens]
	#words = [w for w in re.search("<[a-z 0-9A-Z]*\/>")]
	#print words
	stops = set(stopwords.words("english"))
	words = [w for w in words if not w in stops and len(w)>1]
	#print words
	words=sorted(set(words))
	stem = [porter.stem(d) for d in tokens]
	return " ".join(x for x in words)," ".join(y for y in stem)