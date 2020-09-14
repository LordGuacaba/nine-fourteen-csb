message = input("Enter original message: ")
keyword = input("Enter keyword: ")
function = input("encrypt or decrypt? ")
file_name = input("File for output: ")

in_list = []
for char in message:
  in_list.append(char)

keylist = []
shiftlist = []
for lett in keyword:
  shiftlist.append(lett)
  if lett not in keylist:
    keylist.append(lett)

conveyor = []
for num in range(32, 127):
  conveyor.append(chr(num))

for letter in conveyor:
  if letter not in keylist:
    keylist.append(letter)
 
out_list = []  

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
