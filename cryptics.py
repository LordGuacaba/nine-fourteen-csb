# Gets all of the information (message, encryption key, function, and file for output) necessary to run the program
message = input("Enter original message: ")
keyword = input("Enter keyword: ")
function = input("encrypt or decrypt? ")
file_name = input("File for output: ")

# Sets up a list of all characters in the message
in_list = []
for char in message:
  in_list.append(char)

# Creates the list used to shift characters for the encryption based on the key, and adds those characters once to the reference list
keylist = []
shiftlist = []
for lett in keyword:
  shiftlist.append(lett)
  if lett not in keylist:
    keylist.append(lett)

# Adds all ASCII characters to conveyor list
conveyor = []
for num in range(32, 127):
  conveyor.append(chr(num))

# Adds all ASCII characters not already in the reference list to it
for letter in conveyor:
  if letter not in keylist:
    keylist.append(letter)

# This list will be for characters to output
out_list = []  

# Takes the list of characters in the message, shifts each character over in the reference list based on the letters in the key, and adds the new characters to the output list
def encrypt_message(thing):
  shift_count = 1
  for char in thing:
    tp = ord(char)
    tp += (ord(shiftlist[shift_count - 1]) - 31)
    shift_count += 1
    if shift_count > len(shiftlist):
      shift_count -= len(shiftlist)
    if tp > 126:
      tp -= 94
    new_letter = keylist[(tp - 32)]
    out_list.append(new_letter)

# Performs the same function as the last function, but shifts the letters backwards, so this is used for decryption
def decrypt_message(stuff):
  shift_count = 1
  for char in in_list:
    tp = (keylist.index(char) + 32)
    tp -= (ord(shiftlist[shift_count - 1]) - 31)
    shift_count += 1
    if shift_count > len(shiftlist):
      shift_count -= len(shiftlist)
    if tp < 32:
      tp += 94
    new_letter = chr(tp)
    out_list.append(new_letter)       

# Based on the user-inputted function, either encrypts or decrypts the message, creating the appropriate output list
if function == "encrypt":
  encrypt_message(in_list)
elif function == "decrypt":
  decrypt_message(in_list)
  
# Converts the output list to a string, adding each character, and then printing it to the console
message_out = ""
for letter in out_list:
  message_out += letter
print(message_out)

# If a file for output was given, writes the message in that file
if file_name != "none":
  rum = open(file_name, "w")
  rum.write(message_out)
  rum.close()
