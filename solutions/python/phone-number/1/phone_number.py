import re
class PhoneNumber:
    def __init__(self, number):
        self.number = re.sub('[+ ()-.]','',number) # Remove special characters
        if any([char.isalpha() for char in self.number]): # Check for letters
            raise ValueError("letters not permitted")
        elif any([(not char.isdigit()) for char in self.number]): # Check for special characters
           raise ValueError("punctuations not permitted")
        elif len(self.number)<10: # Verify number is long enough
            raise ValueError("must not be fewer than 10 digits") 
        elif len(self.number)>11: # Verify number is not too long
            raise ValueError("must not be greater than 11 digits")
        if len(self.number)==10: # If the number is 10 digits (has no country code)
            if int(self.number[0])==0: # Check area code
                raise ValueError("area code cannot start with zero")
            elif int(self.number[0])==1: # Check area code
                raise ValueError("area code cannot start with one")
            elif int(self.number[3])==0: # Check exchange code
                raise ValueError("exchange code cannot start with zero")
            elif int(self.number[3])==1: # Check exchange code
                raise ValueError("exchange code cannot start with one")
        else:
            if self.number[0]!='1':
                raise ValueError("11 digits must start with 1")
            self.number=self.number[1:]
            if int(self.number[0])==0: # Check area code
                raise ValueError("area code cannot start with zero")
            elif int(self.number[0])==1: # Check area code
                raise ValueError("area code cannot start with one")
            elif int(self.number[3])==0: # Check exchange code
                raise ValueError("exchange code cannot start with zero")
            elif int(self.number[3])==1: # Check exchange code
                raise ValueError("exchange code cannot start with one")
        self.area_code = self.number[:3]
    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'