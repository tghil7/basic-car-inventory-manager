import datetime;






class Vehicle():
    __stockID: int
    __vin: str
    __vehicleType: str
    __year: int
    __make: str
    __model: str
    __odometer: int
    __price: int

    def getStockId(self):
        return self.__stockID
    
    def getVin(self):
        return self.__vin
    
    def getVehicleType(self):
        return self.__vehicleType
    
    def getYear(self):
        return self.__year
    
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getOdometer(self):
        return self.__odometer
    
    def getPrice(self):
        return self.__price
    
    # Setters
    def setStockId(self, stockId):
        self.__stockID = stockId

    def setVin(self, vin):
        self.__vin  = vin

    def setVehicleType(self, vehicleType):
        self.__vehicleType  = vehicleType

    def setYear (self, carYear):
        self.__year = carYear

    def setMake (self, carMake):
        self.__year = carMake


    def setModel (self, model):
        self.__year = model

    def setOdometer(self, odometer):
        self.__odometer = odometer

    def setPrice (self, price):
        self.__price = price

    def __init__(self, stockID, vin, vehicleType, year, make, model, odometer, price):
        self.__stockID = stockID
        self.__vin = vin
        self.__vehicleType = vehicleType
        self.__year = year
        self.__make = make
        self.__model = model
        self.__odometer = odometer
        self.__price = price

    def showDescription(self):  
       #Format the description and display
       output = f"{self.getMake():<10} {self.getModel():<10} {self.getYear():<10} {self.getStockId():<10} {self.getVin():<15} {self.getVehicleType():<10} {self.getOdometer():<10} {self.getPrice():<10}"
       print(output)

        

class ElectricVehicle(Vehicle):
    __batterySize: str

    def getBatterySize(self):
        return self.__batterySize
    
    def setBatterySize(self, size):
        self.__batterySize = size

    def __init__(self, stockID, vin, vehicleType, year, make, model, odometer, price, batterySize):
        Vehicle.__init__(self,stockID, vin, vehicleType, year, make, model, odometer, price)
        self.__batterySize = batterySize

    def showDescription(self):
        #Format the description and display
        output = f"{self.getMake():<10} {self.getModel():<10} {self.getYear():<10} {self.getStockId():<10} {self.getVin():<15} {self.getVehicleType():<10} {self.getOdometer():<10} {self.getPrice():<10} {self.__batterySize:<10}"
        print(output)

        


class HybridVehicle(Vehicle):
    __mpg: int     #Attribute specific to the HybridVehicle class
    
    # Get the private attribute Mpg
    def getMpg(self):
        return self.__mpg
    
    #Set the private attribute Mpg
    def setMpg(self, mpg):
        self.__mpg = mpg

    # Default class constructor
    def __init__(self, stockID, vin, vehicleType, year, make, model, odometer, price, mpg):
        Vehicle.__init__(self,stockID, vin, vehicleType, year, make, model, odometer, price) 
        self.__mpg = mpg

    def showDescription(self):
        #Format the description and display
        output = f"{self.getMake():<10} {self.getModel():<10} {self.getYear():<10} {self.getStockId():<10} {self.getVin():<15} {self.getVehicleType():<10} {self.getOdometer():<10} {self.getPrice():<10} {' ':<10} {self.__mpg}"
        print(output)


def getInput():
    while True:
        try:
            selection = int(input ('Please select from the following options: \n [1] Display Inventory             [2] Add a new vehicle              [3] Update an existing vehicle   [4]Delete an existing vehicle    [5] Exit\n'))
            # Check if the input is valid
            if selection not in range(1,6):
                raise ValueError ('Invalid selection. Please enter a number between 1 and 5.')
            # If the input is valid, break out of the loop
            break
        except ValueError as e:
            #Handle the invalid input by displaying the error message
            print (e)
            continue
    return selection

def addInventory(list):
    make = input ("Please enter the new vehicle's make: ")
    model = input ("Please enter the new vehicle's model: ")
    stockId = input ("Please enter the new vehicle's stock ID: ")
    vehicleType = input ("Please enter the new vehicle's type:")
    VIN = input ("Please enter the new vehicle's VIN: ")
    odometer = input ("Please enter the new vehicle's odometer:")
    year = input ("Please enter the new vehicle's year: ")
    price = input ("Please enter the new vehicle's price: ")
    if vehicleType == 'R': #Create a regular vehicle if the vehicle type entered is 'R'
        new_vehicle = Vehicle (stockId, VIN, vehicleType, year, make, model, odometer, price)
    elif vehicleType == 'H': #Create a hybrid vehicle if the vehicle type entered is 'H'
        mpg = input('Please enter the mpg of this vehicle: ')
        new_vehicle = HybridVehicle (stockId, VIN, vehicleType, year, make, model, odometer, price, mpg)
    if vehicleType == 'E': #Create an electric vehicle if the vehicle type entered is 'E'
        batterySize = input('Please enter the battery size of this vehicle: ')
        new_vehicle = ElectricVehicle (stockId, VIN, vehicleType, year, make, model, odometer, price, batterySize)
    list.append(new_vehicle)
    print ('Vehicle successfully added: ' +" " + new_vehicle.getYear() + ' ' + new_vehicle.getMake() + " " + new_vehicle.getModel())

def dispInventory(list):
    print ('  {                              VEHICLE INVENTORY REPORT                            ')
    print(f"{'Make':<10} {'Model':<10} {'Year':<10} {'stock  ID':<10} {'VIN':<15} {'Type':<10} {'Odometer':<10} {'Price':<10} {'Battery':<10} {'MPG'}")

    for item in list:
        if item.getVehicleType() == 'R':  #Display the details of a regular vehicle if the item is a regular vehicle
            new_vehicle = Vehicle(item.getStockId(), item.getVin(), item.getVehicleType(), item.getYear(), item.getMake(), item.getModel(), item.getOdometer(), item.getPrice())
            new_vehicle.showDescription()
        elif item.getVehicleType() == 'E':  #Display the details of an electric vehicle if the item is an electric vehicle
            new_vehicle = ElectricVehicle(item.getStockId(), item.getVin(), item.getVehicleType(), item.getYear(), item.getMake(), item.getModel(), item.getOdometer(), item.getPrice(), item.getBatterySize())
            new_vehicle.showDescription()
        elif item.getVehicleType() == 'H':  #Display the details of a hybrid vehicle if the item is an hybrid vehicle
            new_vehicle = HybridVehicle(item.getStockId(), item.getVin(), item.getVehicleType(), item.getYear(), item.getMake(), item.getModel(), item.getOdometer(), item.getPrice(), item.getMpg())
            new_vehicle.showDescription()

    print ('------------------------------- END OF INVENTORY REPORT -------------------------------------------')

def updatePrice(list):
    while True:
        try:
            inventory_id = int(input('Please enter the inventory number to update: '))
            #Get all valid inventory numbers
            inventory_numbers = []
            for item in list:
                inventory_numbers.append (item.getStockId())
            if inventory_id not in inventory_numbers:
                raise ValueError ('Invalid inventory number. Please enter a valid inventory number.')
            # If the input is valid, break out of the loop
            break
        except ValueError as e:
            #Handle the invalid input by displaying the error message
            print (e)
            continue
    new_price = input ('Please enter new price for inventory ' + str(inventory_id) + ' :')
    for item in list:
        if item.getStockId() == inventory_id:
            item.setPrice(new_price)
            print('Price of vehicle with inventory number ' + str(inventory_id)  + 'updated successfully!')
        
    
            

def deleteInventory(list):
    while True:
        try:
            inventory_id = int(input('Please enter the inventory number to delete: '))
            inventory_numbers = []
            for item in list:
                inventory_numbers.append (item.getStockId())
            if inventory_id not in inventory_numbers:
                raise ValueError ('Invalid inventory number. Please enter a valid inventory number')
            # If the input is valid, break out of the loop
            break
        except ValueError as e:
            #Handle the invalid input by displaying the error message
            print (e)
            continue
    for item in list:
        if item.getStockId() == int(inventory_id):
            list.remove(item)
            print('Inventory ' + str(inventory_id) + ' removed successfully!')



def main():
    print ("************************************************");
    print ('*\t\tAnicet Akanza                   *');
    print ('* IS826: Application Programming                *');
    print ('* Assignment 6: Vehicle Inventory               *');
    print ('* Date:'+ datetime.datetime.now().strftime('%x') + "                                 *"); #Conversion of the current date to the local format
    print ('* This program manages an inventory of vehicles.*');
    print('*The user can, update or remove vehicles.       *');
    print ('*He can also display all the vehicles available.*');
    print ("************************************************");
    print ()
    print ()
    print('WELCOME TO VEHICLE INVENTORY MANAGEMENT SYSTEM')
    print ()
    
    #Create my inventory list.
    inventory = []
    #Create 2 initial vehicle objects to add to the list. 
    mercedes = Vehicle(105, 'WWE3456AY', 'R', 2000, 'Mercedes', 'C 220', 130000, 9000)
    honda = ElectricVehicle(106,'AFH123238899', 'E', 2004, 'Honda', 'Insight', 120000, 5000, 'Medium' )
    volvo = HybridVehicle(110, 'GH3239QWW56', 'H', 2008, 'Volvo', 'S 60', 153000, 1500, 40)
    inventory.append(mercedes)
    inventory.append(honda)
    inventory.append(volvo)
    # Initialize the selection, and create a loop to prompt the user
    selection = 0;

    while (selection != 5):
        selection = getInput()
        match selection:
            case 1:
                dispInventory(inventory)
            case 2:
                addInventory(inventory)
            case 3:
                updatePrice(inventory)
            case 4:
                deleteInventory(inventory)
            case 5:
                print('Thank you!')
                exit()


if __name__== "__main__":
    main()





        




