class Luhn:
    def __init__(self, card_num):
        card_num=card_num.replace(' ','')
        sum=0
        self.card_num=card_num
        if len(self.card_num)>1 and all(list(map(lambda item: item.isdigit(),self.card_num))):
            for i,digit in enumerate(reversed(card_num)):
                if i%2 != 0:
                    sum += (int(digit)*2) if (int(digit)*2)<=9 else (int(digit)*2)-9
                else:
                    sum+=int(digit)
            self.sum=sum
        else:
            self.sum='invalid'
    def valid(self):
        return self.sum!='invalid' and self.sum % 10 == 0 and len(self.card_num)>1 and all(list(map(lambda item: item.isdigit(),self.card_num)))
