import json
import removeStopWords as stopwords
import re
def generate_data_for_DB():
	f = open('finefoods1.txt', 'rb')
	data_value=[]
	field={}
	for data in iter(lambda: f.readline(),""):
		#print data
		if data not in ["\n","\r\n"]:
			try:
				if(":" in data):
					sentence=data.split(":")[1].strip()
					stringId=data.split(":")[0].split("/")[1].strip()
					if stringId == "text":
						processedText,stemmedText=stopwords.removeStopWords(sentence)
						field["processedText"] = processedText
						field["stemmedText"] = stemmedText
					field[stringId]=unicode(re.sub("\\[a-z]*","",sentence),"utf-8")
			except Exception, e:
				print str(e)
		else:
			#print "data inserting"
			#print field
			data_value.append(field)
			field={}
	#print field
	#data_json=json.dumps(field,sort_keys=True)
	#field["processedText"]=stopwords.removeStopWords(sentence)
	#print field
	data_value.append(field)
	#print data_value
	f.close()
	print len(data_value)
	return data_value