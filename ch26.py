def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorow. 415-555-9999 is my office.'
for i in range(len(message)): #on each iteration, new 12 characters from message is assigned to chunk
    chunk = message[i:i+12]
    if isPhoneNumber(chunk): #on each iteration of chunk, it is passed through the function, until the 12-digit phone number pattern is recognized, and then it is printed
        print('Phone number found: ' + chunk)
print('Done')
