import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
from sqlalchemy import create_engine

# Database configuration
#db_config = {
#    'user': 'specified_username',
#    'password': 'specified_password',
#    'host': 'localhost',
#    'port': '5432',
#    'database': 'database_name'
#}

# Example is shown below

# Database configuration
db_config = {
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
    'database': 'etl_database_1'
}

# CSV file path
#csv_file_path = 'path-to-csv-file'
# Example is shown below
csv_file_path = 'DEM_Challenge_Section1_DATASET.csv'

# Create a connection to the PostgreSQL database
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Extract data from CSV
data = pd.read_csv(csv_file_path)

# Aesthetic transformation applied here. The last name column is sorted in-place alphabetically
data.sort_values(["last_name"],  
                    axis=0, 
                    ascending=[True],  
                    inplace=True) 

# Structural transformation applied here. Combine first name and last name into a new column named: 'Full_name'
data['Full_name'] = data.apply(lambda row: row['first_name'] + ' ' + row['last_name'], axis=1)

# Create a table called etl_database_1 in the PostgresQL database that you had previously installed on your computer. 
# Use pgAdmin to create the table as discuused in the 'ReadMe' document.
# After, the code below will load the tranformed data into the PostgresQL etl_database_1 

data.to_sql('etl_database_1', engine, if_exists='replace', index=False)


print("ETL process using PostgresQL database completed successfully")



st.title("PostgresQL Based ETL Front End_by Emmanuel Oyekanlu")


# optional addition of some cool images
st.sidebar.image("somelogo.png", use_column_width=False)



# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM etl_database_1;', ttl="8m")
st.dataframe(df)

st.subheader("_You can also use pgAdmin_ to view transformed data in your PostgresQL Database :blue[cool] :sunglasses:")






