def generate_seat_letters(number):
    for seat in range(number):
        yield ['A','B','C','D'][seat%4]
def generate_seats(number):
    if number//4>=14:
        number+=4
    seat_letters=generate_seat_letters(number)
    for seat in range(number):
        if not seat//4 + 1==13:
            yield str(seat//4 + 1) + next(seat_letters)
    

def assign_seats(passengers):
    seats=generate_seats(len(passengers))
    passenger_seats={}
    for passenger in passengers:
        passenger_seats[passenger]=next(seats)
    return passenger_seats
def generate_codes(seat_numbers, flight_id):
    for number in seat_numbers:
        yield number+flight_id+'0'*(12-len(number)-len(flight_id))