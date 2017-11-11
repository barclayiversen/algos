# This algo takes a list of tuples. the first number in each tuple is the number of passengers getting on the bus, the 
# second number is the passengers disembarking. The function returns the total number of passengers left.


def number(bus_stops):
    number_of_passengers = 0
    for stop in bus_stops:
        number_of_passengers += stop[0]
        number_of_passengers -= stop[1]
    return number_of_passengers  
