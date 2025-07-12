def convert(number):
    pling,plang,plong=not number%3,not number%5,not number%7
    return 'Pling'*pling+'Plang'*plang+'Plong'*plong or str(number)