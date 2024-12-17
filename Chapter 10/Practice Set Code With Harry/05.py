#  5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 

class Train:
    def __init__(self, ticket_info, no_of_seats, fare):
        self.ticket_info = ticket_info
        self.no_of_seats = no_of_seats
        self.fare = fare

    def ticket(self):
        print(f"Customer Name: {self.ticket_info}")

    def seat_status(self):
        print(f'No of seats booked: {self.no_of_seats}')
        

        
        

