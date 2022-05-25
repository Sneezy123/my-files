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

res = reg.search("[0-9]+\.*[0-9]*", user_input)
wert = float(res.group())
cups = reg.search("[\s|0-9]*[cC][uU][pP][sS]?", user_input)

if res:
    print(wert)
    if cups:
        mills = wert * 240
        print(reg.sub("[0-9]+\.*[0-9]*\s*[cC][uU][pP][sS]?",
              str(mills) + " ml", user_input, 1))


else:
    print("keine Zahl!")


input("Drücke Enter, um fortzufahren...")
