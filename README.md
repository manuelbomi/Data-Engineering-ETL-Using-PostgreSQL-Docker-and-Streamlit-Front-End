## BRIEF OVERVIEW
This Extraction, Transform and Loading (ETL) project automates the ingestion of data from a provided CSV/xlsx file, transform the data and load the data into a PostgreSQL database. 
The loaded data can be viewed through using PostgreSQL’s pgAdmin user interface (UI). In addition, for the convenience of the user, Streamlit (front end) is used to display the result of the transformed data onto a browser on the user’s desktop.
The process has been fully tested on a Windows 10 computer. However, if need be, with some slight tweaks, the whole process is also reproducible on a Linux or MAC based computer system. 
For reproducibility, Docker is used for containerization, along with PostgreSQL database. PostgreSQL is chosen as it can reliably perform as a relational database management system while also featuring some NoSQL abilities by working well with JSON data. Python is used along with some libraries to accomplish the ETL automation tasks. Visual Studio Code is the development environment
### FEATURES
-	Extraction: Data in any csv file that is stored in the same file/directory as the ‘database_etl.py’ file is automatically extracted
-	Transformation: Some aesthetic transformation such as sorting the ‘last_name’ column alphabetically is accomplished. Also executed is a structural transformation process such as combining ‘first_name’ and ‘last_name’ column into a newly created ‘full_name’ column. 
-	Loading: Loading is also automatically accomplished through the ‘database_etl.py’ file. By using the PostgreSQLs pgAdmin UI (with the user’s password), users can view the transformed and data loaded onto the PostgreSQL database. Users can also immediately view the result of the loaded data through the automatically displayed Streamlit browser front end. 
### LIBRARIES & TECHNOLOGIES USED
-	Docker: Containerization technology for managing and deploying the entire project
-	Python: For ETL process, frontend system design and for loading the transformed data into the database system. Needed python libraries include sqlalchemy, pandas, streamlit, psycopg2-binary, streamlit_extras.
-	PostgreSQL: Database for warehousing the transformed data. 
-	Visual Studio Code: Integrated Development Environment (IDE) for developing, debugging, running and testing the project. 
### GETTING STARTED
For Windows based computer systems, install Desktop Docker and Windows Subsystem for Linux (WSL) on your computer. Install needed packages to get Docker running on your machine if you are using Linux and MAC based computer systems. 
The list of needed software and dependencies include:
-	Python 3.x 
-	Use pip install -r requirements.txt to install other needed libraries in your environment. The use of virtual environment is recommended (but not mandatory) for this project.  
-	Visual Studio Code
-	Desktop Docker
-	PostgreSQL database system (versions 16.4 and 17.0 available here:   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads    have been fully tested for this project)
-	
### HOW TO SET UP YOUR PROJECT
1.	Create a virtual environment on your project directory. Use ‘python -m venv filename’ command.

To activate, use ‘filename\Scrirpts\activate’ command. For some Windows system, to activate, it is preferrable to use ‘.\\Scripts\activate’ command. 

(On some newly configured Windows based systems, users may optionally need to set program execution policy via Windows Powershell.  For such systems, open Powershell as Administrator and type:

‘Set-ExecutionPolicy -ExecutionPolicy RemoteSignal -Scope CurrentUser’

If you decide to use a virtual environment for your project, ensure that you activate the environment each time you run your project. 

2.	Clone the project repository on Github (……………………) and extract its content onto your project’s virtual environment.

3.	Start Docker Desktop on your desktop.

The project directory in the project virtual environment is similar to the directory shown below:
