#############################################################
##                                                         ##
##                ** Zutaten Umrechner **                  ##
##                    - Nils Müller -                      ##
##              https://github.com/Sneezy123               ##
##                                                         ##
#############################################################


# Imports
import re as reg  # RegEx

user_input = input("""Gebe die Zutat ein, die Du umwandeln möchtest? 
(Maximal eine; **Beachte, dass die Maßeinheit mit Wert enthalten ist: z. B.: 10g -> zehn Gramm 
oder 2 cups -> zwei Tassen (480ml))\n         -->   """)  # asks user

res = reg.search("[0-9]+", user_input)
wert = res.group()
ml = reg.search("[\s|0-9]*[mM][lL]", user_input)

if res:
    print(wert)
    if ml:
        cups = wert * 240
        print(reg.sub("[0-9]+", cups, user_input))


else:
    print("keine Zahl!")
