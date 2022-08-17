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
Work was divided evenly between all members of the team based on strengths and prior experience. The fact that some team members were together in person at the time of project commencement and some were not also impacted work division. In person team members worked together to produce the main code components, and those who were virtual adopted the equivalant of a Quality Assurance role, carrying out tests on the code and suggesting improvements with an objective eye as they had not been involved in its production. <br> Documentation such as this report and any linked documents was a team effort, completed by the team members most familiar with a certain section and peer assessed by other team members to ensure quality, clarity and detail were maintained. <br><br>
|Teams name| Contributions |
|----------|---------------|
|Emily SJ|[Tests plan](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_plans.md) <br> [class_function_descriptors](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/class_function_descriptors.md) <br> [test_check_header (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_header.py) <br> [test_check_ids (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_ids.py) <br> [test_check_readings (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_check_readings.py)] <br> [test_main_checkDate (main function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_main_checkDate.py) <br> [test_num_columns (validate_files function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_num_columns.py) <br> [test_remove_empty (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_remove_empty.py) <br> [test_row_num (validate_files function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_row_num.py) <br> [test_timestamp (validate_file function)](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_timestamp.py) <br> All files in the 'tests' folder <br> Documentation|
|Jacob S1| [server.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/server.py) <br> [client.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/client.py) <br> [README.md](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/README.md) <br> Documentation|
|Anna D|[validate_file](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/validate_file.py)<br> [README.md](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/README.md) <br> [class_function_descriptors](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/class_function_descriptors.md) <br> File archive <br> Documentation|
|Anon Thomas|[main.py](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/main.py) <br> documentation |


#### Use of version control
- TODO emily
- why we chose it - everyone knows how to use it, easy to use, auto resolve conflicts, more streamlined, can rollback versions if needed 

<br>

#### Meeting organisation
Team meetings were arranged using our group teams chat. These meetings either took the form of all team members being present in the team chat at a dedicated time discussing, in text form, varying aspects of the project; teams calls or, as seen in weeks 1 and 2 of the project, team members getting together in person to examine the current state of the repository and discuss next steps.  Meetings were called on an ad-hoc basis, occuring when a significant decision needed to be made, a large section of the code had been completed, or a member had a query.  We found that this approach was more efficient than having meetings occur on a scheduled basis, as it meant that there was always a specific purpose and goal for each conversation.

<br>

#### Choice of programming language
As a team we decided to complete the entire project in python, as all team members have previous experience with the language, and thus felt more confident using it than C or PowerShell.  Additionally, file handling, data processing and data manipulation, which are all integral parts of the task are, in our opinion, much simpler in python than the other languages permitted.

<br>

#### Software development approaches
We decided to use the "Comment Driven Development" approach, in which the entire project is pseudocoded using comments before being written in full python code.  This allowed us to plan the code thoroughly before beginning, reducing the amount of times sections needed to be rewritten due to unforseen requirements, and refining the implementation to be as efficient as possible before development began.  A further benefit was that the implementation of different sections could be properly discussed with the entire team before they were implemented, preventing miscommunication and better facilitating the integration of code sections written independently by different team members. <br><br>
We also implemented our own take on 'feature driven development'. Each team member was given an overarching feature of the project, for example Jacob was assigned the client-server connectivity feature of the product. Each team member then identified the smaller features (for example, individual functions) within that overarching feature and implemented them one at a time, within an agreed time frame. <br><br>
Linking to this, we adopted informal sprints. Due to the time restrictions on the project, industry standard two week long sprints were not feasible, however short sprints lasting between two and three days in which each team member aimed to produce a set section of the their portion of the code did occur throughout the project.  Such sprints usually took place after meetings regarding progress, following identification from one team member that a currently incomplete section of another person's code would be needed for them to complete their work. <br><br>
Pair programming was not used significantly during initial development as a result of our feature driven approach. However, this approach was utilised during the testing and review stage of the project, in which either in pairs or as an entire team we worked together to resolve identified bugs and change working implementations of sections of the code to improve efficiency, amongst other issues, with an objective eye.

<br>

#### Bug fixing
In regards to bugs, obscure errors such as value errors were predominantly discovered during the testing portion of development. When a bug was discovered, a note was made in the code and the test plan for any corresponding test that consequently failed, detailing why the failure occured. We then used our group teams chat to collaboratively discuss possible solutions as well as how any subsequent changes would impact other aspects of the code and how changes could be implemented whilst maintaining the integrity of other developers work.<br><br>
Code that needed to be changed was then commented out in the relevant function with a note indicating why and the new code implemented around it. <br><br>
We chose to leave prior code in, albeit commented out, as we felt it demonstrated our refinement processes and would help newcomers to the code to understand any deviations from the initial plans for the function logic and other altered plans.

<br>

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
- TODO - fill these out (jacob)

### Assumptions
- TODO anna

### Error Code System
- TODO anna

### README
[README document:]()

## Test Plans
**Please note that the unit tests are linked within the test plan document, they and any csv files used can also be found in the tests folder on the following page: [main project repo](https://github.com/AnnaD2022/QA-FTP-Project)** <br>
[Test plan document:](https://github.com/AnnaD2022/QA-FTP-Project/blob/main/test_plans.md)
