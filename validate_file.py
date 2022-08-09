import csv
from fileinput import filename
import pandas
import glob
import os
import difflib
import re


# Things to test:
# TODO add taest case with multiple errors e.g. header and something else
# TODO add test case for completely missing data
# TODO add test case for incorrect num rows (too high and too low)
# TODO ask/check if each file msut have 10 rows
# TODO use pandas library for sanitisation + some checks (w3schools data cleaning)
# TODO test with more smaple data (bad)
# TODO double check catches all null values
# TODO - effective error handling to increase robustness of solution and use, by sanitising all user inputs to prevent malicious access or 
# modification of data and/or code - where is this necessary
# TODO can you have a missing header line? if so, code for this
# TODO test case for "too many" header columns with data - does it crash when header is fixed?
# TODO test case for too many values (but correct header)
# TODO test timestamp checker - vslid and invalid

# perform checks to test correctness of file
#TODO if flagged for deletion in one test, do you perform the rest? - no - return if failed
def verify_data(file_data, file_name):
    check_header(file_data, file_name)
    remove_empty(file_data, file_name)
    check_num_rows(file_data, file_name)
    check_num_columns(file_data, file_name)
    check_ids(file_data, file_name)
    check_timestamp(file_data, file_name)
    check_readings(file_data, file_name)
    return #TODO change - delete/accept/fail flag - combine results of calls?

def check_header(file_data, file_name):
    correct_header = """['batch_id' 'timestamp' 'reading1' 'reading2' 'reading3' 'reading4'
 'reading5' 'reading6' 'reading7' 'reading8' 'reading9' 'reading10']"""
    header = str(file_data.columns.values)
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
        
        log_name = file_name.replace(".csv", "")
        #adds error to log file
        with open(log_name +"_log.txt", "a+") as log_file:
            log_file.write("Error 200 - Incorrect Header - Errors:" + diff_string + " . Header was repaired.")

        # overwrite incorrect header with correct string
        file_data.columns = ['batch_id', 'timestamp', 'reading1', 'reading2', 'reading3', 'reading4',
        'reading5', 'reading6', 'reading7', 'reading8','reading9', 'reading10']
        file_data.to_csv(".\\"+ file_name, index = False)
        
    # do not mark to delete as any errors would have been repaired
    return

def remove_empty(file_data, file_name): #TODO rename
    # find "coordinates" of empty fields
    x_coord, y_coord = ((file_data.isnull().sum(x)| file_data.eq('').sum(x)).loc[lambda x: x.gt(0)].index for x in(0,1))
    if y_coord.size > 0:
        error_string = ""
        columns = x_coord.tolist()
        rows = y_coord.tolist()
        for x in range(0, len(columns)):
            error_string += " Column: " + columns[x] + " Row: " + str(rows[x]) + "."
        
        log_name = file_name.replace(".csv", "")
        #add error to log file
        with open(log_name +"_log.txt", "a+") as log_file:
            log_file.write("Error 300 - Missing Values - " + error_string)
        
        #TODO check if should just remove
        return True

    return False

#TODO check if need this
def check_num_rows(file_data, file_name):
    if len(file_data.index) == 10:
        return False
    else:
        log_name = file_name.replace(".csv", "")
        #add error to log file
        with open(log_name +"_log.txt", "a+") as log_file:
            log_file.write("Error 400 - Incorrect Number of Rows - " + str(len(file_data.index)) + " rather than 10.")
        return True

#TODO add test cases for all incorrect id types
def check_ids(file_data, file_name):
    batch_id_set = set()
    # by default do not flag for deletion
    is_invalid = False
    batch_ids = file_data['batch_id'].tolist()
    for id in batch_ids:
    # TODO check if having string batch id will crash this
    #TODO check if id can be 0
        if type(id) == int and id > 0:
            if id in batch_id_set:
                is_invalid = True
                error = "Duplicate ID: " + str(id)
                break #TODO check if want repeat warnings - may not need to break
            else:
                batch_id_set.add(id)
        elif type(id) != int:
            is_invalid = True
            error = "Invalid data type: " + str(type(id))
            break
        else:
            is_invalid = True
            error = "Negative ID: " + str(id)
            break

    if is_invalid:
        log_name = file_name.replace(".csv", "")
        with open(log_name +"_log.txt", "a+") as log_file:
            log_file.write("Error 500 - Invalid Batch ID - " + error)

    return is_invalid

def check_num_columns(file_data, file_name):
    is_invalid = False
    for x in range(10):
        row = file_data.iloc[x]
        if len(row) != 12:
            error = "Error 600 - Too Many Values - " + str(len(row)) + " columns instead of 10 on line " + str(x + 1)
            log_name = file_name.replace(".csv", "")
            with open(log_name +"_log.txt", "a+") as log_file:
                log_file.write(error)
            is_invalid = True
            break
    return is_invalid


def check_timestamp(file_data, file_name):
    is_invalid = False
    for x in range(10):
        time = file_data['timestamp'].values[x]
        pattern = re.compile("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$")
        if pattern.fullmatch(time) is None:
            error = "Error 700 - Incorrect Timestamp - \"" + time + "\" on line " + str(x + 1)
            log_name = file_name.replace(".csv", "")
            with open(log_name +"_log.txt", "a+") as log_file:
                log_file.write(error)
            is_invalid = True
            break
    return is_invalid

def check_readings(file_data, file_name):
    # for row in file (not header)
    # for each reading
    # check if float - can fix if int
    # check formatted up to 3 dp - fix if wrong, report error but dont flag to delete
    # check not less than 0 or greater than 9.9
    # if unfixable error either remove and report or flag for deletion and report
    # different error code for each type of error. also imp will change based on if want to break after one error or keep checking for all errors
    return #TODO change to flag

# main
# take in all csv files that have been requested from the server and not yet verified
path = 'temp' #TODO - ensure file is saved in correct location
# TODO change path to "to check" when all testing  done
files_to_check =  glob.glob(path + '/*.csv')
for file_name in files_to_check: # assume file name is in correct format and file exists as this is handled by the server
     is_invalid = False
     #check file contains data
     if os.stat(file_name).st_size == 0:
        #removes data from file name to create log name
        log_name = file_name.replace(".csv", "")
        #adds error to log file
        with open(log_name +"_log.txt", "a+") as log_file:
            log_file.write("Error 100 - Empty File\n")
        is_invalid = True
     else:
        file_data = pandas.read_csv(file_name)
        verify_data(file_data, file_name)
    # TODO pass error flags to GUI to display - iff passes all tests, can move to permanent archive location (from temp area) - need to
    # create a sensible (calendar based) directory system hierarchy - year, month, day
    # if log files exists, but not flagged to delete, still display warnings on GUI, move file and log both to archive
    # if flagged to delete, pass error flags to GUI and move both file and log to delete
    # TODO could do warnings per file or add file to list that is sent to gui at end, told to check logs for more info e.g. FILENAME has errors
    # but has been repaired - check LOGNAME in archive for details.  FILENAME has errors and cannot be repaired - see LOGNAME in delete for 
    # details
    # TODO add "success code" - every file should have a "help" file - change rather than log
    # TODO make sure that 
    # TODO have calendar structure in rejected directory