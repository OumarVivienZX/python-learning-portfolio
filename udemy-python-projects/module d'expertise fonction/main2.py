
def questionnaire(q,r1,r2,r3,r4,good) :
    global score 
    print(q)
    print(" a:",r1)
    print(" b:",r2)
    print(" c:",r3)
    print(" d:",r4)   
    réponse = input(":")
    
    if réponse == good:
      print("bonne réponse ")
      score += 1
    else:    
      print("mauvaise réponse ")
    print()

score =0
questionnaire("quel est la capital de la CI ? :"," Grand Bassam "," Cocody"," Abidjan","Touleupleu","c")
questionnaire("quel est la devise de la  CI ? : ? :"," UNION DISCIPLINE TRAVAIL","GBAIRAI DICIPLINE TRAVAIL","ATTIEKE EST MIEUX QUE FEMME"," EST CE QUE C'EST MINCHEU","a")
questionnaire("quel est le premier président de la Ci ?  :","GBAGBO"," BEDIE ","ADO","FELIX HOUPHOUET BOIGNY","d")
questionnaire("quel est le plat le plus consommé en CI ? :","Placali ","Garba","Wintchin","Auber la légende ","b")
print("score final :", score)



