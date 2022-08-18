# simpliXL

The name of our product for the excel_comp-team 101 is **simpliXL**. This is a platform that helps users compare the content of excel files

## FEATURES

## **User: Unauthenticated**

1. Visit the platform to view basic information about it
2. View and Interact with the documentation
3. Register to view more details
4. No access to use until registered

**User: Authenticated**

1. Full access to the platform
2. Allow upload CSV/excel file
3. Users should get the option to:

- _Highlight duplicates in a single file_
- _Remove duplicates and return a single file_
- _Remove duplicates and return 2 files_
- _Highlight duplicates and return 2 files_

4. Show usage examples to users
5. Allow user to save data and come back to download

## Project links

- **Design link**: [figma](https://www.figma.com/file/UV7dpsrV768tBbfFN8eWsz/simpliXL?node-id=0%3A1)
- **User research**: [Figjam](https://www.figma.com/file/res4sdWmcEBbOehYEF56al/User-research%2Fflow?node-id=0%3A1)
- **Team's Info Board**: [Notion](https://www.notion.so/giftvictor/Project-Team-101-6888931b86284f6c92d2d25acb6e4e37)

## Setup local environment

1. `git clone https://github.com/zuri-training/EXCEL_COMP-Team-101.git` to your local. _Don't fork_
2. `cd EXCEL_COMP-Team-101`
3. Run `git fetch origin` to fetch remote updates
4. Pull latest changes from the main branch. `git pull origin main`

## Create new branch _(branch_name = task_title)_

`git checkout -b (task title)`

- Make all changes in this branch
- Commit the changes and push to the repository
- Allow review on your pull request _(Don't do it yourself)_

## Server Deployment

- Clone github repo
- Create a virtual environment in the root directory
- Activate the virtual environment and install all the required dependencies in the requirements.txt file
- Generate your .env file to to help hide environment variables
- Create a mysql database and oonect
- Navigate into the simplixl folder and run "python manage.py makemigrations" in order to create required sql statements
- Run "python manage.py migrate" in order to create required tables
- Run "python manage.py runserver"

## Contributors/Team Members

- Amarachi Iheakam
- Gift Victor
- David Echendu
- Valerie Osuamkpe
- Ogundairo Abisola
- Olaniran Ibitoye
- Oluwatobiloba Hunkuten
- Chibundum Ehirim
- Benedict Chima Ogbulachi
- Loren Gomez
- Okereke Favour Oluomachi
- Chioma Okeke
- Obey Victoria Ayomide
- Tony Obriku
- Ariyo Olasunkanmi
- Cynthia Nsek
- Bishop Aruoture
- Mbamarah Julia
- David Ayomide Olaniyi
- Joseph Joshua Oluwatobi
- Ayogu Janefrances
- Oluwagbemiga Emmanuel Taiwo
- Hamzat Abdulawwal Olalekan
