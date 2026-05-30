

# Parent class representing a general flight
class Flight:
	def __init__(self, flight_number, origin, destination, duration, starttime, endtime, price):
		self.flight_number = flight_number
		self.origin = origin
		self.destination = destination
		self.duration = duration
		self.price = price
		self.starttime = starttime
		self.endtime = endtime

	def display_info(self):
		print(f"Flight Number: {self.flight_number}")
		print(f"Origin: {self.origin}")
		print(f"Destination: {self.destination}")
		print(f"Duration: {self.duration} hours")
		print(f"Price: ${self.price}")
		print(f"Start Time: {self.starttime}")
		print(f"End Time: {self.endtime}")

	def update_price(self, new_price):
		self.price = new_price
		print(f"Price updated to ${self.price}")

	def delay(self, extra_time):
		self.duration += extra_time
		print(f"Flight delayed by {extra_time} hours. New duration: {self.duration} hours")


# DomesticFlight inherits from Flight
class DomesticFlight(Flight):
	def __init__(self, flight_number, origin, destination, duration, starttime, endtime, price, region):
		super().__init__(flight_number, origin, destination, duration, starttime, endtime, price)
		self.region = region

	def display_domestic(self):
		print("--- Domestic Flight Details ---")
		self.display_info()
		print(f"Region: {self.region}")

	def assign_gate(self, gate):
		self.gate = gate
		print(f"Gate {self.gate} assigned to Domestic Flight {self.flight_number}")

	def is_regional(self):
		# Example: North Island or South Island
		return self.region in ["North Island", "South Island"]


# InternationalFlight inherits from Flight
class InternationalFlight(Flight):
	def __init__(self, flight_number, origin, destination, duration, starttime, endtime, price, country):
		super().__init__(flight_number, origin, destination, duration, starttime, endtime, price)
		self.country = country

	def display_international(self):
		print("--- International Flight Details ---")
		self.display_info()
		print(f"Destination Country: {self.country}")

	def assign_gate(self, gate):
		self.gate = gate
		print(f"Gate {self.gate} assigned to International Flight {self.flight_number}")

	def requires_visa(self):
		# Example: Assume all non-NZ destinations require a visa
		return self.country != "New Zealand"


# Hybrid Inheritance: FlightManager inherits from both DomesticFlight and InternationalFlight
class FlightManager(DomesticFlight, InternationalFlight):
	def __init__(self):
		self.flights = []

	def add_flight(self, flight):
		self.flights.append(flight)
		print(f"Flight {flight.flight_number} added to the system.")

	def remove_flight(self, flight_number):
		self.flights = [f for f in self.flights if f.flight_number != flight_number]
		print(f"Flight {flight_number} removed from the system.")

	def list_flights(self):
		print("--- All Flights in System ---")
		for flight in self.flights:
			flight.display_info()
			print()


# Example usage
if __name__ == "__main__":
	# Create Domestic and International flights
	dom = DomesticFlight(
		flight_number="NZ123",
		origin="Auckland",
		destination="Wellington",
		duration=1.0,
		starttime="08:00",
		endtime="09:00",
		price=200.0,
		region="North Island"
	)
	intl = InternationalFlight(
		flight_number="NZ456",
		origin="Auckland",
		destination="Sydney",
		duration=3.5,
		starttime="10:00",
		endtime="13:30",
		price=600.0,
		country="Australia"
	)

	# Assign gates
	dom.assign_gate("A1")
	intl.assign_gate("I5")

	# Update price and delay
	dom.update_price(220.0)
	intl.delay(0.5)

	# Flight Manager
	manager = FlightManager()
	manager.add_flight(dom)
	manager.add_flight(intl)
	manager.list_flights()
	manager.remove_flight("NZ123")
	manager.list_flights()
