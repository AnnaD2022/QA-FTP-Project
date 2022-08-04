import csv
import pandas
import glob
import os

# Things to test:
# TODO implement/design error system
# TODO code
# TODO use pandas library for sanitisation + some checks (w3schools data cleaning)
# TODO automatically fix certain aspects e.g incorrect header
# TODO - effective error handling to increase robustness of solution and use, by sanitising all user inputs to prevent malicious access or 
# modification of data and/or code - where is this necessary

# perform checks to test correctness of file
#TODO if flagged for deletion in one test, do you perform the rest?
def verify_data(file_data):
    check_header(file_data.head(1))
    remove_empty(file_data)
    #if file still has data after removing empty
    check_num_columns(file_data)
    check_ids(file_data) #TODO if keeping data after removing empty, need to use new data
    check_timestamp(file_data)
    check_readings(file_data)
    return #TODO change - delete/accept/fail flag

def check_header(header):
    #TODO implement
    # compare header to correct string
    # if they are not the same and header line exists partially (even if incorrect)
    # generate string noting difference
    # generate error code
    # save to log file (check if already exists)
    # do not mark to delete
    # overwrite incorrect header with correct string
    # elif they are not the same and header line does not exist
    # insert header line if possible, if not possible mark to delete
    # generate error code & message
    # save to log file (check if already exists)
    # else (header file is correct)
    # do not mark to delete
    return #TODO change to flag

def remove_empty(file_data):
    #TODO implement
    # remove any rows with empty fields (pandas)
    # if rows are removed
    # generate error code + info
    # save to log file (check if already exists)
    # flag for deletion (?) - if not check to see if file is empty, if yes log error flag for deletion, if not do not flag for deletion
    # if rows are not removed, do not flag for deletion
    return #TODO change to flag and possibly modified file if decide to allow rows to be removed

def check_ids(file_data):
    #TODO implement
    # create empty set 
    # by default do not flag for deletion
    # for row in file_data (pandas)
    # batch_id = row[0]
    # if batch_id is positive int
    # if batch_id is in set
    # log error and details
    # flag for removal
    # break or dont depending if want check for repeat warnings
    # else
    # add batch_id to set
    # else
    # log error and message (either for each incorrect row or just once)
    # flag for deletion (and either break or keep going depending on above)
    return #TODO change to flag

def check_num_columns(file_data):
    # for row in file,
    # get num values (count? string parsing? pandas?)
    # should be 12 to a row, no more/less
    # if not 12 flag for deletion, log error and comment
    # break?
    return #TODO change to flag

def check_timestamp(file_data):
    # for row in file (not first one)
    # get second(?) row value
    # check is valid time (use regex or datetime datatype)
    # if invalid, flag for deletion and log error and comment
    # break?
    return #TODO change to flag

def check_readings(file_data):
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
files_to_check =  glob.glob(path + '/*.csv')
for file_name in files_to_check: # assume file name is in correct format and file exists as this is handled by the server
     #check file contains data
     if os.stat(file_name).st.size == 0:
        #TODO make note of error
        #flag to move to delete
        tempstring = "" #TODO remove
     else:
        file_data = pandas.read_csv(file_name)
        verify_data(file_data)
    # TODO pass error flags to GUI to display - iff passes all tests, can move to permanent archive location (from temp area) - need to
    # create a sensible (calendar based) directory system hierarchy - year, month, day
    # if log files exists, but not flagged to delete, still display warnings on GUI, move file and log both to archive
    # if flagged to delete, pass error flags to GUI and move both file and log to delete
    # TODO could do warnings per file or add file to list that is sent to gui at end, told to check logs for more info e.g. FILENAME has errors
    # but has been repaired - check LOGNAME in archive for details.  FILENAME has errors and cannot be repaired - see LOGNAME in delete for 
    # details
    # TODO if not passed but fixable/ not too bad? - go into “failed”?