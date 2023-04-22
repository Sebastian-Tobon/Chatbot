"""***********************************************************************************
                              Run this code on Python IDLE
***********************************************************************************"""
#simple chat BOT v1.0.0

import random

#list for greetings
A = [
  "hola",
  "hey",
  "hello"
]

#list for questions
B = [
  "como estas?",
  "que pasa?",
  "estas bien?",
  "todo bien?"
]

C = [
  "cual es tu nombre?",
  "quien eres?",
  "como te identificas?"
]

#list for answers
D = [
  "Estoy bien 😊",
  "Estoy excelente 🙂",
  "Estoy enfermo 🤒",
  "Estoy feliz 😌",
  "Estoy muy bien 😎"
]

E = [
  "Mi nombre es Rodri.",
  "Soy Rodri,",
  "Mi nombre es Rodri. soy tu asistente virtual."
]

#random generator
X1 = A[random.randint(0, 2)]
X2 = B[random.randint(0, 3)]
X3 = D[random.randint(0, 4)]
X4 = E[random.randint(0, 2)]

def list_Ai():
	print ('BOT : '+X1+'!',X2)
def list_Bi():
	print ('BOT : '+X3,'Por cierto, ¿qué hay de ti??')
def list_Ci():
	print ('BOT : '+X4,'Encantado de conocerte.')
def list_Q(ext):
    print ('BOT : A que te refieres con '+'\''+ext+'\''+'?')

while not False:
	try:
		text = input('\nUser : ').lower()
	except EOFError:
		break
	print()
	if not text:
		print ("BOT : Por favor pregúntame algo. Responderé a tus preguntas si es posible. ツ")
		continue
	else:
		if A[0] in text or A[1] in text or A[2] in text:
			list_Ai()
		elif B[0] in text or B[1] in text or B[2] in text or B[3] in text:
			list_Bi()
		elif C[0] in text or C[1] in text or C[2] in text:
			list_Ci()
		elif text.endswith("?"):
			print ("BOT : Eres muy hablador y curioso sobre todo ツ")
		else:
			list_Q(text)