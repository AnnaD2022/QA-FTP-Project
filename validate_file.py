# Things to test:
# Duplicated batch_ids - this value should be unique(though unsorted) in each.csv file; duplications would indicate a faulty .csv file and should
# be logged and excluded
# Missing headers or misspelt/incorrect headers, e.g. "batch" rather than "batch_id" - could fix this - add missing field, repair typo
# Missing columns on a row
# Invalid entries, e.g.reading values of 10 or greater
# Each batch has 10 associated readings. - ensure no more/less
# multiple entries for the same timestamp are not considered unusual.
# All 10 readings should be represented as floating point numbers formatted up to three decimal places with no value exceeding 9.9, or less than
# 0
# (this would be considered invalid data).
# Empty files (there are no "nil" returns)
# Incorrectly formatted filenames.
# Filenames for trial data exports are created using the following naming convention: MED_DATA_YYYYMMDDHHMMSS.csv
# Files which contain these issues must be identified and logged using an appropriate technique
# execution, i.e.using effective error handling to increase robustness of solution and use, by sanitising all user inputsto prevent malicious 
# access or modificationof data and/or code.

# pseudocode (overview)
# take in one csv file (from server)
# perform checks to test correctness of file - use pandas library for sanitisation + some checks (w3schools data cleaning)
# automatically fix certain aspects e.g incorrect header
# determine certain error flags based on what is (not) wrong with file
# pass error flags to GUI/CLI to display - iff passes all tests, can move to permanent archive location (from temp area) - need to create a 
# sensible (calendar based) directory system hierarchy
# add filename to some kind of log if fails tests (unless automatically/manually fixed?)