# ------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating how Pickling and Structured error handling work
# ChangeLog: (Who, When, What)
# Jessica Chen, 11/26/2022, Created Script
# ------------------------------------------------- #

import pickle

# -- Data -- #
file_name_str = 'HomeInventory.dat'  # The name of the data file
table_lst = []  # A list that acts as a "table" of rows


# -- Processing -- #
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, 'ab')
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    file = open(file_name, 'rb')
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data


# -- Presentation -- #
# Get Item Name and Value from user, then store the data in a list object
print('Please type in a Name and Value for your household item.')
name = str(input('Enter a Name: '))

# try/except
try:
    value = float(input('Enter its Value: '))
except ValueError:
    print('Please enter only numbers for Value!')  # Display error message to user

value = float(input('Please re-enter the value: '))  # For user to confirm the value / input in a correct format
table_lst = [name, value]


# Store the list object into a binary file
save_data_to_file(file_name_str, table_lst)

# Read the data from the file into a new list object and display the contents
print(read_data_from_file(file_name_str))
