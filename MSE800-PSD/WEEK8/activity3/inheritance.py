

# Parent class representing a general flight
class Flight:
	def __init__(self, flight_number, origin, destination, duration, starttime, endtime, price):
		# Attributes common to all flights
		self.flight_number = flight_number
		self.origin = origin
		self.destination = destination
		self.duration = duration
		self.price = price
		self.starttime = starttime
		self.endtime = endtime

	def display_info(self):
		# Method to display general flight information
		print(f"Flight Number: {self.flight_number}")
		print(f"Origin: {self.origin}")
		print(f"Destination: {self.destination}")
		print(f"Duration: {self.duration} hours")
		print(f"Price: ${self.price}")
		print(f"Start Time: {self.starttime}")
		print(f"End Time: {self.endtime}")


# Subclass representing a domestic flight (inherits from Flight)
class DomesticFlight(Flight):
	def __init__(self, flight_number, origin, destination, duration, starttime, endtime, price, region):
		# Call the parent class constructor to initialize inherited attributes
		super().__init__(flight_number, origin, destination, duration, starttime, endtime, price)
		# Attribute specific to domestic flights
		self.region = region

	def display_domestic(self):
		# Method specific to domestic flights
		print("--- Domestic Flight Details ---")
		# Call the inherited method to display general info
		self.display_info()
		print(f"Region: {self.region}")


# Example usage
if __name__ == "__main__":
	# Create a DomesticFlight object
	nz_domestic = DomesticFlight(
		flight_number="NZ123",
		origin="Auckland",
		destination="Wellington",
		duration=1.0,
		starttime="08:00",
		endtime="09:00",
		price=200.0,
		region="North Island"
	)
	# Demonstrate inherited and subclass methods
	nz_domestic.display_domestic()
