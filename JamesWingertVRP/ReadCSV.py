#James Wingert #001424955
import csv
from HashTable import HashTable

with open('WGUData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # Calls the HashTable class to create an object of HashTable
    insert_into_hash_table = HashTable()
    # list that represents the first truck delivery
    truck_one = []
    # list that represents the second truck delivery
    truck_two = []
    # list that represents the final truck delivery
    truck_one_trip_two = []

    # Read in values from CSV file and insert them into key / value pairs
    # these values are what makes up the nested dictionary inside of the Hash table
    # Space-time complexity is O(N)
    for row in readCSV:
        package_ID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        special_note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        hash_value = [package_ID, address_location, address, city, state,
                      zip, delivery, size, special_note, delivery_start,
                      delivery_status]

        key = package_ID
        value = hash_value

        # The following statements creates nested lists given certain constraints to load the trucks up.


        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                truck_one.append(value) # this is a list that represents the first truck
        if 'Can only be' in value[8]:
            truck_two.append(value)
        if 'Delayed' in value[8]:
            truck_two.append(value)
        # change the wrong address package to the correct address
        if '84104' in value[5] and '10:30' not in value[6]:
            truck_one_trip_two.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            truck_one_trip_two.append(value)
        if value[0] == '2':
            truck_one.append(value)

        if value not in truck_one and value not in truck_two and value not in truck_one_trip_two:
            if len(truck_two) > len(truck_one_trip_two):
                truck_one_trip_two.append(value)
            else:
                truck_two.append(value)

        insert_into_hash_table.insert(key, value)  # adds all values in csv file to to a hash table


    # function used to get the full list of values at start of day
    # Space-time complexity is O(1)
    def get_hash_map():
        return insert_into_hash_table


    # function used to grab the packages that are loaded into the first truck
    # Space-time complexity is O(1)
    def check_truck_one():
        return truck_one


    # function used to grab the packages that are loaded into the second truck
    # Space-time complexity is O(1)
    def check_truck_two():
        return truck_two


    # function used to grab the packages that are loaded into the first truck last
    # Space-time complexity is O(1)
    def check_truck_one_trip_two():
        return truck_one_trip_two
