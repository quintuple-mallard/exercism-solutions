def convert(number):
    pling,plang,plong=number%3==0,number%5==0,number%7==0
    return 'Pling'*pling+'Plang'*plang+'Plong'*plong if pling or plang or plong else str(number)