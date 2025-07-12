def response(hey_bob):
    if not hey_bob.strip():
        return 'Fine. Be that way!'
    elif hey_bob.strip()[-1]=='?':
        if str.isupper(hey_bob):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif str.isupper(hey_bob):
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'