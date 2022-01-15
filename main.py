# Verschlüsselung des Textes
def encrypt(texts,shifts):
	results = ""
	try:
		# Text zur Umwandlung in ASCII in einzelne Buchstaben "Umwandeln"
		for i in range(len(texts)):
			char = texts[i]

			# Verschlüsselung der Großbuchstaben
			if (char.isupper()):
				results += chr((ord(char) + shifts - 65) % 26 + 65)
			# Verschlüsselung der Kleinbuchstaben
			else:
				results += chr((ord(char) + shifts - 97) % 26 + 97)
	except:
		print("Fehler bei der Verschlüsselung")

	return results
# Entschlüsselung des Textes
def decrypt(text,shift):
	result = ""
	try:
		# Text zur Umwandlung in ASCII in einzelne Buchstaben "Umwandeln"
		for i in range(len(text)):
			char = text[i]

			# Entschlüsselung der Großbuchstaben
			if (char.isupper()):
				result += chr((ord(char) -  (shift*(-1))-65) % 26 + 65)
			# Entschlüsselung der Kleinbuchstaben
			else:
				result += chr((ord(char) - (shift*(-1)) - 97) % 26 + 97)
	except:
		print("Fehler bei der Entschlüsselung")

	return result

# Eingaben des Benutzers
text = input("Bitte gib den Text ein den du verschlüsseln bzw. wieder entschlüsseln möchtest:")
shift = int(input("Bitte gebe die Zahl ein um die die Zeichen verschoben werden sollen (beim entschlüsseln gibst du die"
                  " gleiche Zahl ein, die bereits zum verschlüsseln genutzt wurde):"))
encrypt1 = int(input("Wenn du verschlüsseln willst gib bitte eine 1 ein, falls du entschlüsseln willst gib bitte eine 0 "
                    "ein"))

# Ausgabe des Ergebnisses beim verschlüsseln
if (encrypt1 == 1):
    print ("Text : " + text)
    print ("Shift : " + str(shift))
    print ("Cipher: " + encrypt(text,shift))
else:
    print ("Text : " + text)
    print ("Shift : " + str(shift))
    print ("Cipher: " + decrypt(text,shift))