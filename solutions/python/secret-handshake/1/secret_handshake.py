ACTIONS=['wink','double blink','close your eyes', 'jump', 'REVERSE']
def commands(binary_str):
    reverse=False
    handshake=[]
    for index,digit in enumerate(binary_str[::-1]):
        if int(digit):
            if ACTIONS[index]=='REVERSE':
                reverse=True
            else:
                handshake.append(ACTIONS[index])
    return handshake[::-1] if reverse else handshake