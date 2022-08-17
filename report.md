# University medical school software development project
## Team Members:
|Teams name| Git Hub credentials |
|----------|---------------------|
|Emily SJ|EthSpJo|
|Jacob S1| facade93coat|
|Anna D|AnnaD2022 |
|Anon Thomas|TorinM321 |

## Team Management
#### Work division
Work was divided evenly between all members of the team based on strengths and prior experience. The fact that some team members were together in person at the time of project commencement and some were not also impacted work division. In person team members worked together to produce the main code components, and those who were virtual adopted the equivalant of a Quality Assurance role, carrying out tests on the code and suggesting improvements with an objective eye as they had not been involved in its production. <br> Documentation such as this report and any linked documents was a team effort, completed by the team members most familiar with a certain section and peer assessed by other team members to ensure quality, clarity and detail were maintained. <br>
|Teams name| Contributions |
|----------|---------------|
|Emily SJ|[Tests plan](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_plans.md) <br> [class_function_descriptors](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/class_function_descriptors.md) <br> [test_check_header (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_header.py) <br> [test_check_ids (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_ids.py) <br> [test_check_readings (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_readings.py)] <br> [test_main_checkDate (main function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_main_checkDate.py) <br> [test_num_columns (validate_files function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_num_columns.py) <br> [test_remove_empty (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_remove_empty.py) <br> [test_row_num (validate_files function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_row_num.py) <br> [test_timestamp (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_timestamp.py) <br> All files in the 'tests' folder <br> documentation|
|Jacob S1| [server.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/server.py) <br> [client.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/client.py) <br> [README.md](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/README.md) <br> documentation|
|Anna D|[validate_data](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py)<br> [README.md](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/README.md) <br> [class_function_descriptors](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/class_function_descriptors.md) <br> documentation|
|Anon Thomas|[main.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br> documentation |

#### Use of version control
- TODO why we chose it - everyone knows how to use it, easy to use, auto resolve conflicts, more streamlined, can rollback versions if needed

#### Meeting organisation
Team meetings were arranged using our group teams chat. These meetings either took the form of all team members being present in the team chat at a dedicated time discussing, in text form, varying aspects of the project; teams calls or, as seen in weeks 1 and 2 of the project, team members getting together in person to examine the current state of the repository and discuss next steps.

#### Choice of programming language
As a team we decided to complete the entire project in python, as all team members have previous experience with the language, and thus felt more confident using it than C or PowerShell.

#### Software development approaches
We decided to use the "Comment Driven Development" approach, in which the entire project is pseudocoded using comments before being written in full python code.  This allowed us to plan the code thoroughly before beginning, reducing the amount of times sections needed to be rewritten due to unforseen requirements, and refining the implementation to be as efficient as possible befoe development began.  A further benefit was that the implementation of different sections could be properly discussed with the entire team before they were implemented, preventing miscommunication and better facilitating the integration of code sections written independently by different team members. <br>
We also implemented our own take on 'feature driven development'. Each team member was given an overarching feature of the project, for example Jacob was assigned the client server connectivity feature of the product. Each team member then identified the smaller features within that overarching feature and implemented them one at a time, within a team agreed time frame, as for example functions. <br>
Linking to this, we adopted informal sprints. Due to the time restrictions on the project, industry standard 2 long sprints could not be facilitated however short sprints lasting between 2-3 days in which each team member aimed to produce a set section of the their portion of the code did occur throughout the project usually after meetings regarding progress and following identification from one team member that another persons function, etc would be needed for them to complete their work. <br>
Paired coding was minorly used by our team as a result of our feature driven approach, however, was enlisted during the testing / review stage when either in pairs or as an entire team we worked together to resolve identified bugs and objectively change working implementations of sections of the code to make them more efficient, etc.

#### Bug fixing
In regards to bugs, obscure errors euch as value errors, were predominantly discovered during the testing portion of the project. When a bug was discovered, a note was made in the code as well as in the test plan for any corresponding test that consequently failed detailing why the failure occured. We then used our group teams chat to collaboratively discuss possible solutions as well as how any subsequent changes would impact other aspects of the code and how that could be done to maintain the integrity of other developers work.<br>
Code that needed to be changed was then commented out in the relevant function with a note indicating why and the new code implemented around it. <br>
We chose to leave the prior code in but commented out as we felt it demonstrates our improvement processes and would help newcomers to the code to understand any deviations in the intial plans for function logic, etc.

#### Problem solving
- TODO emily

#### Cooperation
- TODO anna + others add to
- reached out, keep in loop, etc 

#### Time Management
- TODO anna
- Personal projects, time crunch, made it harder
- Unforseen challenges

#### Team Leadership
- TODO anna
- democratised system

## Code
### Classes
[client.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/client.py) <br>
[server.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/server.py) <br>
[main.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br>
[validate_file.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py) <br>


### Class function Descriptors
[Class function descriptors document:](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/class_function_descriptors.md) 
- TODO - fill these out

### Assumptions
- TODO anna

### Error Code System
- TODO anna

### README
[README document:]()
## Test Plans
**Please note that the unit tests are linked within the test plan document, they and any csv files used can also be found in the tests folder on the following page: [main project repo](https://github.com/AnnaD2022/QA-FTP-Project)** <br>
[Test plan document:](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_plans.md)
