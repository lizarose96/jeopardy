question = {
	"category": "HISTORY",
	"air_date": "2004-12-31",
	"question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'",
	"value": "$200",
	"answer": "Copernicus",
	"round": "Jeopardy!",
	"show_number": "4680"
}

a = raw_input(question['question'] + " ") 

if a == question['answer']:
	print "correct"
else:
	print "incorrect"  
