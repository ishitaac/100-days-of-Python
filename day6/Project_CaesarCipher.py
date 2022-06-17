from art import logo

print(logo)
# without special symbols
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# COMBINING THE TWO BELOW FUNCTIONS INTO ONE
def caesar(start_text,shift,direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for char in start_text:
    if char in alphabet:
      pos = alphabet.index(char)
      new_pos = pos + shift
      new_letter = alphabet[new_pos]
      end_text += new_letter
    else:
      end_text+= char
  print(f"The {direction} form of the text entered is {end_text}") 

contd = True

while contd==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  shift =  shift%25
  caesar(start_text = text, shift =shift, direction = direction)
  result = input("Type 'Yes' if you want to go again. Otherwise type 'no'. \n").lower()
  if result == "No":
    contd= False
    print("GoodBye")
  

  

# OTHER ELABORATED METHOD
# def encrypt(text,shift):
#   cipher_text = ""
#   for letter in text:
#     pos = alphabet.index(letter)
#     new_pos = pos + shift
#     new_letter = alphabet[new_pos]
#     cipher_text+= new_letter
#   print(f"The encoded form of the entered text is {cipher_text} ")


# def decrypt(cipher_text,shift):
#   decoded = ""
#   for letter in text:
#     pos = alphabet.index(letter)
#     new_pos = pos - shift
#     new_letter = alphabet[new_pos]
#     decoded += new_letter
#   print(f"The decoded form of the entered text is {decoded} ")


# if direction=="encode":
#   encrypt(text,shift)
# elif direction == "decode":
#   decrypt(text,shift)
# else:
#   print("Caution: You have entered the wrong word. Either type encode or decode")
  