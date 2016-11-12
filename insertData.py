from pymongo import MongoClient
import readData as data
import pickle
from bson.binary import Binary
import cosine_similarity as process
client=MongoClient()
db=client.finefoods
posts = db.posts
dataset= data.generate_data_for_DB()
#print type(dataset[0])
textlist=[]
listofdict=[]
i =1
print "inserting data to db"
for d in dataset:
	#print type(d)
	#print i
	datadict={}
	try:
		result=posts.insert_one(d)
		textlist.append(d["processedText"])
		datadict["productId"]=d["productId"]
		datadict["processedText"]=d["processedText"]
		listofdict.append(datadict)
	except Exception, e:
		print d
	#i=i+1
#calculate tfidf
print "calculating tfidf"
f = open('tfidf-food.pkl', 'wb')
try:
	myObj=process.getTfidf(textlist)
	pickle.dump(myObj,f)
except Exception, e:
	print e
#calculate cosine similarity
f.close()
print "calculating cosine similarity"
cosinefile = open('cosine-food.pkl', 'wb')
try:
	for i in range(len(listofdict)):
		cosine=[]
		print i
		for j in range((len(listofdict))):
			if(i!=j):
				cosine.append(process.cosineSimilarity(listofdict[i]["processedText"],listofdict[j]["processedText"]))
		pickle.dump({'cosine': cosine,'productId':listofdict[i]["productId"]},cosinefile)
except Exception, e:
	print e
#print result.inserted_ids
cosinefile.close()
client.close()