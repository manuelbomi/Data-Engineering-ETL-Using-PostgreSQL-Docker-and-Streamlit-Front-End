#README
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













The ‘Postgres_based_ETL’ file in the directory above is created inside the project’s virtual environment. The project’s Github repository is cloned and extracted inside ‘Postgres_based_ETL’ file. 

The project’s repository files and other included documents (such as ETL test data ‘DEM_Challenge_Section1_DATASET.csv’, some crudely designed logo for the frontend, the .streamlit file which includes Streamlit’s ‘secrets.toml’ file for rendering the Stremlit’s front end are also included in the ‘Postgres_based_ETL’ file. Example of the content of ‘Postgres_based_ETL’ file is shown below:


 










4.	Install additional python requirements by using ‘pip install -r requirements.txt’

5.	Use the command ‘docker-compose up -d’ to compile the entire project inside the Docker container. 


6.	From your VSCode terminal, run the ‘database_etl.py’ script using the command:
                                                    ‘streamlit run database_etl.py’

Examples of how to configure your PostgreSQL password, ports and server are given in the ‘database_etl.py’, ‘docker-compose.yml’ and the ‘secrets.toml’ files.
Before running your project using ‘streamlit run database_etl.py’, configure your tables and databases through the pgAdmin UI in PostgreSQL as shown in the series of figures below. For a hypothetical table named ‘etl_database_1’, create the table in your PostreSQL database as shown below:

 

 

7.	After setting up a named database in your PostgreSQL database, you can now run your script via your VSCode terminal ( ‘streamlit run database_etl.py’) to complete the ETL automation process. 
8.	After your project run successfully, you can view your transformed and loaded data in your PostgreSQL database by using the SELECT * FROM databasefilename command as shown in the figures below. In the figures below, the database filename is ‘etl_database_1’. 


 




The original file that was used to provide the example shown above is ‘DEM_Challenge_Section1_DATASET.csv’ file. It is also included in the project file. A cross section of the original data is shown below:



After transformation and loading in the database, users may readily observe that the data has been transformed as specified in the ‘database_etl.py’’ script. As shown in the pgAdmin UI, the last_name column has been sorted alphabetically. Also, a new column (‘full_name’), which is a combination of ‘first_name’ and ‘last_name’ has been added to the original file. 

 

Streamlit is also used to provide an automatically rendered front end for the project. The transformed data can be downloaded as a .csv file using either the Streamlit front end or the pgAdmin UI. The transformed data can be enlarged (zoomed in/out) as shown in the Streamlit front end below:
 

 

 

As shown in the Streamlit rendering, the crudely designed logo (‘somelogo.png’) also available in the project repository is also rendered as specified by the Streamlit front end.  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


