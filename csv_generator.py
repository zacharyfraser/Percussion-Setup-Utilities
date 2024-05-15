import csv
import sys

DEFAULT_FILE_NAME = "percussion_parts.csv"

file_names = list()

#Get file names of files passed as arguments
if(len(sys.argv) > 1):
    for i in range(1, len(sys.argv)):
        file_names.append(sys.argv[i])
#If no files passed, use default file name
else:
    file_names.append(DEFAULT_FILE_NAME)

#Repeat for each file in file_names
try:
    for file_name in file_names:
        print(f"Opening <{file_name}>.")
        with open(file_name, 'a+', newline = '') as file:
                #Create CSV Writer
                writer = csv.writer(file)
                print("Press CTRL+C to End")
                #Repeat for each row until CTRL + C
                try:
                    while(True):
                        new_row = list()
                        input_string = input("Please Enter Chart Title: ")
                        new_row.append(input_string)
                        input_string = input("Please Enter Part Name: ")
                        new_row.append(input_string)
                        #Repat for each item until CTRL + C
                        try:
                            while(True):
                                input_string = input("Please Enter Instrument Name: ")
                                new_row.append(input_string)
                        #Break from Row
                        except KeyboardInterrupt as keyboard_interrupt:
                            print(f"\nEnd of row: <{new_row}>.")
                            writer.writerow(new_row)
                #Break from File
                except KeyboardInterrupt as keyboard_interrupt:
                    print(f"\nEnd of entries for <{file_name}>.")
#Break from program
finally:
    print("Terminating Program.")