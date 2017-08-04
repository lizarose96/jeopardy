questions = [
{
	"category": "HISTORY",
	"air_date": "2004-12-31",
	"question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'",
	"value": "$200",
	"answer": "Copernicus",
	"round": "Jeopardy!",
	"show_number": "4680"
},
{
  "category": "FARMVILLE",
  "air_date": "2010-07-09",
  "question": "'It's the time when ripened crops are gathered, or the yield of crops themselves.'",
  "value": "$1,000",
  "answer": "harvest",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "E BEFORE I",
  "air_date": "2010-07-09",
  "question": "'Not native'",
  "value": "$800",
  "answer": "foreign",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "HUMAN BODY NUMBERS",
  "air_date": "2010-07-09",
  "question": "'These are the largest of the 6 major pairs of joints in the human body'",
  "value": "$1000",
  "answer": "knees",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "PRO SPORTS",
  "air_date": "2010-07-09",
  "question": "'<a href=\"http://www.j-archive.com/media/2010-07-09_J_07.jpg\" target=\"_blank\">This</a> <a href=\"http://www.j-archive.com/media/2010-07-09_J_07a.jpg\" target=\"_blank\">golfer</a> dominated her sport like no other in recent decades'",
  "value": "$1000",
  "answer": "(Annika) Sorenstam",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "SOUNDS LIKE A NEW POKEMON",
  "air_date": "2010-07-09",
  "question": "'Plateosaurus was a grass type of dinosaur; it wasn't a carnivore or omnivore but this third type'",
  "value": "$1000",
  "answer": "a herbivore",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "LITERARY MONSTERS",
  "air_date": "2010-07-09",
  "question": "'In a Barbara Jean Hicks story, monsters are tricked into eating these veggies when told they're giant trees'",
  "value": "$1000",
  "answer": "broccoli",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "FARMVILLE",
  "air_date": "2010-07-09",
  "question": "'Important breeds of this on a farm include the brown Swiss & Holstein'",
  "value": "$1000",
  "answer": "cows",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "E BEFORE I",
  "air_date": "2010-07-09",
  "question": "'5-letter adjective meaning unusual or eccentric'",
  "value": "$1000",
  "answer": "weird",
  "round": "Jeopardy!",
  "show_number": "5960"
},
{
  "category": "THE CIVIL WAR",
  "air_date": "2010-07-09",
  "question": "'Lincoln wrote 5 different versions of this Nov. 19, 1863 speech & made several changes as he spoke; nice ad-libbing, Abe!'",
  "value": "$400",
  "answer": "the Gettysburg Address",
  "round": "Double Jeopardy!",
  "show_number": "5960"
}]

import random

score = 0

r = random.randint(0,len(questions) - 1)
q = questions[r]

a = raw_input(q['question'] + " ")

if a == q['answer']:
	# add to score
else:
	# subtract from score

print score
