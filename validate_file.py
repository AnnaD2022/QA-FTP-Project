from fileinput import filename
import pandas
import glob
import os
import difflib
import re
import shutil
import numpy


# perform checks to test correctness of file - returns True if file is invalid and False if file is valid
def verify_data(file_data, file_name):
    #if flagged for deletion in one test, do not perform the rest
    if not (check_header(file_data, file_name)):
        if not (remove_empty(file_data, file_name)):
            if not (check_num_rows(file_data, file_name)):
                if not (check_ids(file_data, file_name)):
                    if not (check_timestamp(file_data, file_name)):
                        return check_readings(file_data, file_name)
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True


def check_header(file_data, file_name):
    correct_header = """['batch_id' 'timestamp' 'reading1' 'reading2' 'reading3' 'reading4'
 'reading5' 'reading6' 'reading7' 'reading8' 'reading9' 'reading10']"""
    header = str(file_data.columns.values)
    #if header is incorrect, generate a string describing what is wrong
    if header != correct_header:
        difference = difflib.SequenceMatcher(None, correct_header, header)
        diff_string = ""
        for change, start1, end1, start2, end2 in difference.get_opcodes():
            if change == 'equal':
                diff_string += correct_header[start1:end1]
            elif change == 'insert':
                diff_string += "(inserted: " + header[start2:end2] + ")"
            elif change == 'delete':
                diff_string += "(deleted: " + correct_header[start1:end1] + ")"
            elif change == 'replace':
                diff_string += "(replaced: " + correct_header[start1:end1] + " with " + header[start2:end2] + ")"
            else:
                diff_string = "unknown format error"
        
        # attempt to overwrite incorrect header with correct string
        try:
            file_data.columns = ['batch_id', 'timestamp', 'reading1', 'reading2', 'reading3', 'reading4',
            'reading5', 'reading6', 'reading7', 'reading8','reading9', 'reading10']
            file_data.to_csv(file_name, index = False)
            info_name = file_name.replace(".csv", "")
            #add error to info file
            with open(info_name +"_info.txt", "a+") as info_file:
                info_file.write("Error 200 - Incorrect Header - Errors:" + diff_string + " . Header was repaired.\n")
            #return False as file has been repaired, so header is no longer invalid
            return False
        #if header cannot be repaired
        except ValueError as ve:
            #record error
            info_name = file_name.replace(".csv", "")
            with open(info_name +"_info.txt", "a+") as info_file:
                info_file.write("Error 201 -  Fatal Incorrect Header - Errors:" + diff_string + " . Header cannot be repaired due to error: " + str(ve) + "\n")
            #return that file is invalud
            return True
    #return False as header is valid
    return False


def remove_empty(file_data, file_name):
    # find "coordinates" of empty fields
    x_coord, y_coord = ((file_data.isnull().sum(x)| file_data.eq('').sum(x)).loc[lambda x: x.gt(0)].index for x in(0,1))
    #if there are any empty fields
    if y_coord.size > 0:
        error_string = ""
        columns = x_coord.tolist()
        rows = y_coord.tolist()
        #generate a string denoting where all the empty fields are
        for x in range(0, len(columns)):
            #the lambda function cannot store rows/columns with multiple missing values, so in this case the user is not told the specific 
            #location of the missing value
            try:
                error_string += " Column: " + columns[x] + " Row: " + str(rows[x]) + "."
            except IndexError:
                error_string +=  " Some columns/rows contain multiple blank values."
        
        info_name = file_name.replace(".csv", "")
        #add error to info file
        with open(info_name +"_info.txt", "a+") as info_file:
            info_file.write("Error 300 - Missing Values - " + error_string + "\n")
        
        #return that file is invalid
        return True

    #if there are no empty fields, return that file has passed this test (is not invalid)
    return False

#this function assumes that there are 10 rows in each file, as that is the case for all of the test files provided.  If the actual requirements
#are different, this can easily be altered or removed
def check_num_rows(file_data, file_name):
    #if there are 10 rows, file is valid
    if len(file_data.index) == 10:
        return False
    # otherwise, file is invalid
    else:
        info_name = file_name.replace(".csv", "")
        #add error to info file
        with open(info_name +"_info.txt", "a+") as info_file:
            info_file.write("Error 400 - Incorrect Number of Rows - " + str(len(file_data.index)) + " rather than 10.\n")
        return True


def check_ids(file_data, file_name):
    #stores all of the batch ids that have already been read so that duplicates can be found
    batch_id_set = set()
    # by default do not flag for deletion
    is_invalid = False
    #gets all the batch ids from the data
    batch_ids = file_data['batch_id'].tolist()
    for id in batch_ids:
        #checks validity of batchids - no duplicates, correct data type and not <0
        if type(id) == int and id >= 0:
            if id in batch_id_set:
                is_invalid = True
                error = "Duplicate ID: " + str(id)
                break #if one id is invalid, do not check the rest
            else:
                batch_id_set.add(id) #add each correct id to the set so that it duplicates can be found
        elif type(id) != int:
            is_invalid = True
            error = "Invalid data type: " + str(type(id))
            break
        else:
            is_invalid = True
            error = "Negative ID: " + str(id)
            break

    #if there is an invalid batch id, add error to file
    if is_invalid:
        info_name = file_name.replace(".csv", "")
        with open(info_name +"_info.txt", "a+") as info_file:
            info_file.write("Error 500 - Invalid Batch ID - " + error + "\n")

    return is_invalid


#this function was used to check the number of colums of data in the file was correct.  However, changes to the check_header function has made
#this redundant, so it has been removed
#def check_num_columns(file_data, file_name):
    #is_invalid = False
    #check number of columns in each row of the file.  If there are too many, report location of error and flag file as invalid
    #for x in range(10):
        #row = file_data.iloc[x]
        #if len(row) != 12:
            #error = "Error 600 - Too Many Values - " + str(len(row)) + " columns instead of 10 on line " + str(x + 1) + "\n"
            #log_name = file_name.replace(".csv", "")
            #with open(log_name +"_log.txt", "a+") as log_file:
                #log_file.write(error)
            #is_invalid = True
            #break
    #return is_invalid


def check_timestamp(file_data, file_name):
    is_invalid = False
    #for each row in file
    for x in range(10):
        #get the timestamp from that row and check it matches regex for hh:mm:ss 24hr clock
        time = file_data['timestamp'].values[x]
        pattern = re.compile("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$")
        #if it does not match the regex, report the error, flag as invalid, and do not continue checking
        if pattern.fullmatch(time) is None:
            error = "Error 700 - Incorrect Timestamp - \"" + time + "\" on line " + str(x + 1) + "\n"
            info_name = file_name.replace(".csv", "")
            with open(info_name +"_info.txt", "a+") as info_file:
                info_file.write(error)
            is_invalid = True
            break
    return is_invalid


def check_readings(file_data, file_name):
    #for each reading in each row
    for x in range(10):
        readings = file_data.loc[x, 'reading1':'reading10']
        for y in range(len(readings)):
            value = readings[y]
             # check if correct datatype (float)
            if type(value) != numpy.float64: #line altered by ESJ, floats from csv are read in to have this type, use of float here causes issues
                if type(value) == int:
                    # cast to float
                    file_data.at[x, file_data.columns[y+2]] = format(value, ".2f")
                    #save updated dataframe to file
                    file_data.to_csv(file_name, index = False)
                    info_name = file_name.replace(".csv", "")
                    #add error to info file
                    with open(info_name +"_info.txt", "a+") as info_file:
                        info_file.write("Error 800 - Int, Not Float - Row: " + str(x+1) + " Column: " +  + " . Cast as float.\n")
                else:
                    #cannot fix error, so record and return that the tests failed
                    info_name = file_name.replace(".csv", "")
                    #add error to info file
                    with open(info_name +"_info.txt", "a+") as info_file:
                        info_file.write("Error 801 - Incorrect Data Type - " + str(type(value)) + " Row: " + str(x+1) + " Column: " + file_data.columns[y+2] + "\n")
                    return True

            #get all numbers after decimal point
            decimal_places = str(value).split(".")[1]
            #if there are more than 3 decimal places
            if len(decimal_places) > 3:
                #round the value and save amended data to file
                file_data.at[x, file_data.columns[y+2]] = round(value, 3)
                file_data.to_csv(file_name, index = False)
                info_name = file_name.replace(".csv", "")
                #do not need to return invalid as error has been fixed
                with open(info_name +"_info.txt", "a+") as info_file:
                        info_file.write("Error 802 - Incorrect Rounding - " + str(value) + " Row: " + str(x+1) + " Column: " + file_data.columns[y+2] + ". Fixed rounding.\n")

            #check values are in range
            if not (0 < value < 10):
                info_name = file_name.replace(".csv", "")
                with open(info_name +"_info.txt", "a+") as info_file:
                        info_file.write("Error 803 - Value Out of Range - " + str(value) + " Row: " + str(x+1) + " Column: " + file_data.columns[y+2] + "\n")
                return True
    #if all values pass all tests, return that the file is not invalid
    return False


# main
# take in all csv files that have been requested from the server and not yet verified
def main():
    path = 'files/to_check'
    files_to_check =  glob.glob(path + '/*.csv')
    for file_name in files_to_check: # assume file name is in correct format and file exists as this is handled by the server
        is_invalid = False
        #if file is empty
        if os.stat(file_name).st_size == 0:
            #removes data from file name to create info file name
            info_name = file_name.replace(".csv", "")
            #adds error to info file
            with open(info_name +"_info.txt", "a+") as info_file:
                info_file.write("Error 100 - Empty File\n")
            is_invalid = True
        else:
            #get file data and perform validity checks on it
            file_data = pandas.read_csv(file_name)
            with open(file_name) as file:
                has_data = file.readline and file.readline
            if has_data:
                is_invalid = verify_data(file_data, file_name)
            else:
                info_name = file_name.replace(".csv", "")
                #adds error to info file
                with open(info_name +"_info.txt", "a+") as info_file:
                    info_file.write("Error 101 - Header Only\n")
                is_invalid = True
        
        #get data from filename to use in directory system
        year = file_name[24:28]
        month = file_name[28:30]
        day = file_name[30:32]
        #create path name to save to based on validity of file
        if is_invalid:
            desired_path = 'files/rejected/' + year + '/' + month + '/' + day
        else:
            desired_path = 'files/successful/' + year + '/' + month + '/' + day
            #create info file denoting a valid file
            info_name = file_name.replace(".csv", "")
            with open(info_name +"_info.txt", "a+") as info_file:
                info_file.write("000 - Valid File\n")

        #if the correct location in the file system does not exist, create it
        if not (os.path.exists(desired_path)):
            os.makedirs(desired_path)

        desired_path += '/'

        #move file and info file to correct directory
        shutil.move(file_name, desired_path + file_name.replace("files/to_check\\", ""))
        info_name = file_name.replace(".csv", "") + "_info.txt"
        shutil.move(info_name, desired_path + info_name.replace("files/to_check\\", ""))
             
    return