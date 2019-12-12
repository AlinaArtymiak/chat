def cesar(encrypt):
 alphabet = "abcdefghijklmnopqrstuvwxyz"
 alphabet2 = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
 numbers = "0123456789"
 symbol="!@#$%^&*()_+-\=/?.,:;{}[]"
 key = int(1)
 encrypt = encrypt.lower() #переводить в нижній регістр
 encrypted = ""


 for letter in encrypt:
   position = alphabet.find(letter)
   newPosition = position + key
   if letter in alphabet:
     if newPosition >= 26:
       newPosition = newPosition - 26
     encrypted = encrypted + alphabet[newPosition]
  
   position2 = alphabet2.find(letter)
   newPosition2 = position2 + key
   if letter in alphabet2:
     if newPosition2 >= 33:
       newPosition2 = newPosition2 - 33
     encrypted = encrypted + alphabet2[newPosition2]
  
   position1 = numbers.find(letter)
   newPosition1 = position1 + key
   if letter in numbers:
      if newPosition1 >= 10:
       newPosition1 = newPosition1 - 10
      encrypted = encrypted + numbers[newPosition1]
   if letter ==" ":
     encrypted = encrypted + letter
   if letter in symbol:
    position3 = symbol.find(letter)
    newPosition3 = position3
    encrypted = encrypted + symbol[newPosition3] 
   

 return encrypted



def cesardecode(encrypt):   

 alphabet = "abcdefghijklmnopqrstuvwxyz"
 alphabet2 = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
 numbers = "0123456789"
 symbol="!@#$%^&*()_+-\=/?.,:;{}[]"
 key = int(-1)
 encrypt = encrypt.lower()
 encrypted = ""


 for letter in encrypt:
   position = alphabet.find(letter)
   newPosition = position + key
   if letter in alphabet:
     if newPosition >= 26:
       newPosition = newPosition - 26
     encrypted = encrypted + alphabet[newPosition]
  
   position2 = alphabet2.find(letter)
   newPosition2 = position2 + key
   if letter in alphabet2:
     if newPosition2 >= 33:
       newPosition2 = newPosition2 - 33
     encrypted = encrypted + alphabet2[newPosition2]
  
   position1 = numbers.find(letter)
   newPosition1 = position1 + key
   if letter in numbers:
      if newPosition1 >= 10:
       newPosition1 = newPosition1 - 10
      encrypted = encrypted + numbers[newPosition1]
   if letter ==" ":
     encrypted = encrypted + letter
   if letter in symbol:
    position3 = symbol.find(letter)
    newPosition3 = position3
    encrypted = encrypted + symbol[newPosition3] 
      
   

 return encrypted

