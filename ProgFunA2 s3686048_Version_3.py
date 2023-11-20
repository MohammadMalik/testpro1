class Customer:
    
    def __init__(self, ID: str, name):
        self.name = name
        self.ID = ID

    def get_name(self):
        return self.name
    
    def get_ID(self):
        return self.ID

    def get_discount(self, distance_fee):
        return 0

    def display_info(self):
        pass
    
class BasicCustomer(Customer):
    
    default_discount_rate = 0.10
    
    def __init__(self, name: str, ID, discount_rate=None):
        super().__init__(name, ID)
        self.discount_rate = discount_rate or self.default_discount_rate
    
    def get_discount(self, distance_fee):
        return self.discount_rate * distance_fee
    
    def display_info(self):
        print(f"Basic Customer ID: {self.get_ID()}, Name: {self.get_name()}, Discount Rate: {self.discount_rate*100}%")
    
    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate


class EnterpriseCustomer(Customer):
    
    default_rate_1 = 0.15
    default_rate_2 = 0.20
    default_threshold = 100

    def __init__(self, name: str, ID, rate_1=None, rate_2=None, threshold=None):
        super().__init__(name, ID)
        self.rate_1 = rate_1 or self.default_rate_1
        self.rate_2 = rate_2 or self.default_rate_2
        self.threshold = threshold or self.default_threshold
        
    def get_discount(self, distance_fee):
        if distance_fee < self.threshold:
            return self.rate_1 * distance_fee
        else:
            return self.rate_2 * distance_fee
    
    def display_info(self):
        print(f"Enterprise Customer ID: {self.get_ID()}, Name: {self.get_name()}")
        print(f"Rate 1: {self.rate_1*100}%, Rate 2: {self.rate_2*100}%, Threshold: ${self.threshold}")

    @classmethod
    def set_discount_rate(cls, rate_1, rate_2):
        cls.default_rate_1 = rate_1
        cls.default_rate_2 = rate_2 

    @classmethod
    def set_threshold(cls, threshold):
        cls.default_threshold = threshold


class Location:    
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def display_info(self):
        print(f"Location ID: {self.ID}, Name: {self.name}")


class Rate:
    def __init__(self, ID, name, price_per_km):
        self.ID = ID
        self.name = name 
        self.price_per_km = price_per_km

    def display_info(self):
        print(f"Rate ID: {self.ID}, Name: {self.name}, Price per km: ${self.price_per_km}")

#########################################################################################
class Booking:
    def __init__(self,records_instance):
        self.basic_fee = 4.20
        self.customer_name = self.get_customer_name().capitalize()
        self.departure_location = self.get_departure_location().capitalize()
        self.destination_location = self.get_destination_location().capitalize()
        self.distance_dep_and_desti = self.get_distance()
        self.rate_type = self.get_rate_type()
        self.distance_fee = self.calculate_distance_fee()
        self.fee_without_discount = self.basic_fee + self.distance_fee
        self.discount = self.calculate_discount()
        self.total_cost = self.calculate_total_cost()
        self.records_instance = records_instance
        

    def get_customer_name(self):
        while True:
            customer_name = input("Please Enter Customer's name: ")
            if customer_name.isalpha():
                return customer_name
            else:
                print("Invalid Entry. Try again")


    def get_departure_location(self):
        while True:
            dep_input = input("Please Enter Departure Location: ")
            if dep_input.isalpha():
                return dep_input
            else:
                print("Invalid response. Try again")


    def get_destination_location(self):
        while True:
            input_des = input("Please enter destination location: ")
            if input_des.isalpha():
                return input_des
            else:
                print("Invalid response. Try again")

    def get_distance(self):
        while True:
            try:
                input_float = float(input("Please enter the distance between departure and destination (in km): "))
                if input_float <= 0:
                    print("The distance cannot be less than or equal to zero.")
                else:
                    return input_float
            except ValueError:
                print("Please enter a valid numeric distance.")

    

    def get_rate_type(self):
        rates_dict = {
            "standard": 1.5,
            "peak": 1.8,
            "weekends": 2,
            "holidays": 2.5
        }
        while True:
            question_rate_type = input("Please provide one of the 4 rates (Standard/ Peak/ Weekends/ Holiday): ").lower()
            if question_rate_type in rates_dict:
                return rates_dict[question_rate_type]
            else:
                print("Please enter a valid rate (Standard/ Peak/ Weekends/ Holiday).")

    def calculate_distance_fee(self):
        return self.distance_dep_and_desti * self.rate_type

    def calculate_discount(self):
        existing_customer_list = ["Ella", "Louis"] #This needs to fixed 
        if self.customer_name in existing_customer_list:
            return self.distance_fee * 0.10
        else:
            return 0

    def calculate_total_cost(self):
        return self.fee_without_discount - self.discount

    def print_receipt(self):
        print("---------------------------------------------------------")
        print("-----------------------Taxi Receipt----------------------")
        print("---------------------------------------------------------")
        print(f"Name: {self.customer_name}")
        print(f"Departure: {self.departure_location}")
        print(f"Destination: {self.destination_location}")
        print(f"Rate: {self.rate_type} (AUD per km)")
        print(f"Distance: {self.distance_dep_and_desti} (km)")
        print("---------------------------------------------------------")
        print(f"Basic fee: {self.basic_fee} (AUD)")
        print(f"Distance fee: {self.distance_fee:.2f} (AUD)")
        print(f"Discount: {self.discount} (AUD)")
        print("---------------------------------------------------------")
        print(f"Total cost: {self.total_cost:.2f} (AUD)")

    ####################################################################################################    
    # def __init__(self, customer, departure, destination, distance, rate):
    #     self.customer = customer
    #     self.departure = departure
    #     self.destination = destination
    #     self.distance = distance
    #     self.rate = rate

    # def compute_cost(self):
    #     distance_fee = self.distance * self.rate.price_per_km
    #     basic_fee = 4.2  # Assuming a fixed basic fee for simplicity
    #     discount = self.customer.get_discount(distance_fee)
    #     total_cost = distance_fee + basic_fee - discount
    #     return distance_fee, basic_fee, discount, total_cost

    # def display_info(self):
    #     print(f"Booking Information:")
    #     print(f"Customer: {self.customer.get_name()}, ID: {self.customer.get_ID()}")
    #     print(f"Departure: {self.departure.display_info()}")  # Assuming Location has a display_info method
    #     print(f"Destination: {self.destination.display_info()}")  # Assuming Location has a display_info method
    #     print(f"Distance: {self.distance} km")
    #     print(f"Rate: {self.rate.display_info()}")  # Assuming Rate has a display_info method

# Assuming Location and Rate classes are defined as described earlier

class Records:
    def __init__(self):
        self.customers = []  # List to store customer objects
        self.locations = []  # List to store location objects
        self.rates = []      # List to store rate objects

    def example(self):
        return 'Rafeh'

    def read_customers(self, file_name):
        # Implement logic to read and add customers from the file to the customers list
        # Assume file format: customer_ID, customer_name, customer type, discount_rate, threshold
        
        try:
            with open(file_name, 'r') as file:
                line_from_file = file.readline()

                while line_from_file:
                    fields_from_line = line_from_file.strip().split(',')
                    customer_id, customer_name, customer_type = fields_from_line[:3]
                    # if customer_type == 'B':
                    #     self.customers.append(BasicCustomer(customer_id, customer_name))
                    # elif customer_type == 'E':
                    #     self.customers.append(EnterpriseCustomer(customer_id, customer_name))
                    
                    line_from_file = file.readline()
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Therefore Exiting")
            exit()
        except PermissionError:
            print(f"Error: Permission denied to open '{file_name}'.")
        except IOError as e:
            print(f"Error: An I/O error occurred while reading '{file_name}': {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def read_locations(self, file_name):
        # Implement logic to read and add locations from the file to the locations list
        # Assume file format: location_ID, location_name
        
        try:
            with open(file_name, 'r') as file:
                line_from_file = file.readline()

                while line_from_file:
                    fields_from_line = line_from_file.strip().split(',')
                    location_id, location_name, = fields_from_line[:2]
                    self.locations.append(Location(location_id, location_name))
                    line_from_file = file.readline()

        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.Therefore Exiting")
            exit()
        except PermissionError:
            print(f"Error: Permission denied to open '{file_name}'.")
        except IOError as e:
            print(f"Error: An I/O error occurred while reading '{file_name}': {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    
    

    def read_rates(self, file_name):
        # Implement logic to read and add rates from the file to the rates list
        # Assume file format: rate_ID, rate_name, price_per_km
        try:
            with open(file_name, 'r') as file:
                line_from_file = file.readline()

                while line_from_file:
                    fields_from_line = line_from_file.strip().split(',')
                    rate_id, rate_name, price_per_km = fields_from_line[:3]
                    self.rates.append(Rate(rate_id, rate_name, price_per_km))
                    line_from_file = file.readline()

        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.Therefore Exiting")
            exit()
        except PermissionError:
            print(f"Error: Permission denied to open '{file_name}'.")
        except IOError as e:
            print(f"Error: An I/O error occurred while reading '{file_name}': {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def find_customer(self, search_value):
        # Implement logic to search for a customer by name or ID
        # Return the customer object if found, otherwise return None
        pass

    def find_location(self, search_value):
        # Implement logic to search for a location by name or ID
        # Return the location object if found, otherwise return None
        pass

    def find_rate(self, search_value):
        # Implement logic to search for a rate by name or ID
        # Return the rate object if found, otherwise return None
        pass

    def list_customers(self):
        # Display information of existing customers on screen
        for customer in self.customers:
            customer.display_info()

    def list_locations(self):
        # Display information of existing locations on screen
        for location in self.locations:
            location.display_info()

    def list_rates(self):
        # Display information of existing rates on screen
        for rate in self.rates:
            rate.display_info()

    def display_records(self):   #For checking ###################################################### Delete Later ###########
        for customer in self.customers:
            customer.display_info()
############################################################################ down chat

class Operations:
    records = Records()
    def __init__(self):
        pass
        # self.records = Records()  # Assuming Records class has been implemented

    def start_menu(self):

        self.load_data_from_files()

        while True:
            print("\nMenu:")
            print("1. Book a trip")
            print("2. Display existing customers")
            print("3. Display existing locations")
            print("4. Display existing rate types")
            print("5. Exit the program")

            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.book_trip()
            elif choice == '2':
                self.records.list_customers()
            elif choice == '3':
                self.records.list_locations()
            elif choice == '4':
                self.records.list_rates()
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                exit()
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def load_data_from_files(self): # To ensure that the program first reads the text files when it runs
        try:
            self.records.read_customers("customers.txt") 
            self.records.read_locations("locations.txt")
            self.records.read_rates("rates.txt")
        except FileNotFoundError as e:
            print(f"Error: {e}. Exiting the program.")
            exit(0)   
        
            

    def book_trip(self):
        records_instance = Records()
        records_instance.read_customers('customers.txt')
        records_instance.read_locations('locations.txt')
        records_instance.read_rates('rates.txt')
        book_trip = Booking(records_instance)
        book_trip.print_receipt()
        # Implement the logic to book a trip as specified in the assignment
        # Use the Records class to find existing customers, locations, and rates
        # Display the receipt as specified in the assignment

# Example usage
if __name__ == "__main__":
    program = Operations()
    program.start_menu()
    
    


######################################################################


# record1 = Records()
# record1.read_customers('customers.txt')
# record1 = Records()
# record1.read_customers('customers.txt')
# record1.read_locations('locations.txt')
# record1.read_rates('rates.txt')

# record1.list_rates()
# record1.list_customers()
# record1.list_locations()

