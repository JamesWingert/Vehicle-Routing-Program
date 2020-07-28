#James Wingert #001424955
import csv
import datetime

# Read in csv file that is the mapping of distances between locations
with open('WGUDistance.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = list(readCSV)

# Read in csv file that is the names of all possible delivery locations
with open('WGUDistanceInfo.csv') as csv_name_file:
    name_readCSV = csv.reader(csv_name_file, delimiter=',')
    name_readCSV = list(name_readCSV)

    # Function finds the distance by comparing row and column at the point in which they meet
    # Space-time complexity is O(1)
    def check_distance(row_value, column_value, sum_of_distance):
        distance = readCSV[row_value][column_value]
        if distance == '':
            distance = readCSV[column_value][row_value]

        sum_of_distance += float(distance)
        return sum_of_distance

    # this function is very similar to the function above but returns a current distance
    # Space-time complexity is O(1)
    def check_current_distance(row_value, column_value):
        distance = readCSV[row_value][column_value]
        if distance == '':
            distance = readCSV[column_value][row_value]
        return float(distance)
    # this is the time that the first truck leaves the hub
    first_time_list = ['8:00:00']
    second_time_list = ['9:10:00']
    third_time_list = ['11:00:00']

    # The default MPH is 18. Dividing distance / 18 it creates total time. Divmod is common to help create time
    # structure, this string is then used with timedelta
    #
    # that object is then added to sum which represents total distance for a particular truck
    # runtime of function is O(N)
    def check_time_first_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        first_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in first_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Repeated function for second truck
    def check_time_second_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        second_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in second_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Repeated function for the third truck
    def check_time_third_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        third_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in third_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    # this function returns the time objects to use in the Packages.py file
    # Space-time complexity is O(1)
    def check_address():
        return name_readCSV


    # The following is my automated optimizing sorting algorithm utilizing a greedy approach. There are 3 parameters:
    # 1. List of not-yet-optimized packages on the truck
    # 2. Truck number
    # 3. Current location which is constantly updated once the truck is moving.
    # The first if statement sets the base case to end the recursion if the list = 0
    # By starting with the lowest value of 20, it constantly checks the current distance against every other possible
    # location. If a lower value is found, it continues to iterate through the list to match that new lowest value. Once
    # the list is completely iterated through, it then adds the package object and associated index to the new lists.
    # The lowest values are taken out of the default list, truck_distance_list, and added to the respective
    # trucks optimization list. The function can then be called recursively and update current location.
    # The function call will end once the list is empty.

    #  The 2 for loops and the constant look up functions cause this to have:
    #  Space-time complexity of O(N^2).

    # these lists represent the sorted trucks that are put in order of efficiency in the function below
    truck_one_optimized = []
    truck_one_optimized_index_list = []
    truck_two_optimized = []
    truck_two_optimized_index_list = []
    truck_three_optimized = []
    truck_three_optimized_index_list = []


    def calculate_shortest_distance(truck_distance_list, truck_number, current_location):  # section 1
        if len(truck_distance_list) == 0:  # section 2
            return truck_distance_list
        else:  #
            try:
                lowest_value = 20.0
                new_location = 0
                for index in truck_distance_list:
                    if check_current_distance(current_location, int(index[1])) <= lowest_value:
                        lowest_value = check_current_distance(current_location, int(index[1]))  # section 3
                        new_location = int(index[1])
                for index in truck_distance_list:  # section 4
                    if check_current_distance(current_location, int(index[1])) == lowest_value:
                        if truck_number == 1:
                            truck_one_optimized.append(index)
                            truck_one_optimized_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 1, current_location)
                        elif truck_number == 2:
                            truck_two_optimized.append(index)
                            truck_two_optimized_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 2, current_location)
                        elif truck_number == 3:
                            truck_three_optimized.append(index)
                            truck_three_optimized_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 3, current_location)
            except IndexError:
                pass

    truck_one_optimized_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def truck_one_optimized_index():
        return truck_one_optimized_index_list

    # Space-time complexity is O(1)
    def truck_one_optimized_list():
        return truck_one_optimized

    truck_two_optimized_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def truck_two_optimized_index():
        return truck_two_optimized_index_list

    # Space-time complexity is O(1)
    def truck_two_optimized_list():
        return truck_two_optimized

    truck_three_optimized_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def truck_three_optimized_index():
        return truck_three_optimized_index_list

    # Space-time complexity is O(1)
    def truck_three_optimized_list():
        return truck_three_optimized
