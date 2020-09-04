message = input("Enter original message: ")
keyword = input("Enter keyword: ")
function = input("encrypt or decrypt? ")
file_name = input("File for output: ")
message_in = message.lower()

in_list = []
for char in message_in:
  in_list.append(char)

keylist = []
shiftlist = []
for lett in keyword.lower():
  shiftlist.append(lett)
  if lett not in keylist:
    keylist.append(lett)
  
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letter in alphabet:
  if letter not in keylist:
    keylist.append(letter)
 
out_list = []  

def encrypt_message(thing):
  shift_count = 1
  for char in thing:
    if char not in alphabet:
      out_list.append(char)
    else:
      tp = ord(char) - 96
      tp += (ord(shiftlist[shift_count - 1]) - 96)
      shift_count += 1
      if shift_count > len(shiftlist):
        shift_count -= len(shiftlist)
      if tp > 26:
        tp -= 26
      new_letter = keylist[tp - 1]
      out_list.append(new_letter)

def decrypt_message(stuff):
  shift_count = 1
  for char in in_list:
    if char not in alphabet:
      out_list.append(char)
    else:
      tp = (keylist.index(char) + 1)
      tp -= (ord(shiftlist[shift_count - 1]) - 96)
      shift_count += 1
      if shift_count > len(shiftlist):
        shift_count -= len(shiftlist)
      if tp < 1:
        tp += 26
      new_letter = alphabet[tp - 1]
      out_list.append(new_letter)       

if function == "encrypt":
  encrypt_message(in_list)
elif function == "decrypt":
  decrypt_message(in_list)
  
message_out = ""
for letter in out_list:
  message_out += letter
  
print(message_out)

if file_name != "none":
  rum = open(file_name, "w")
  rum.write(message_out)
  rum.close()