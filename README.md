# Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner. 

Approach:
1. Data extraction: Clone the Github using scripting to fetch the data from the
Phonepe pulse Github repository and store it in a suitable format such as CSV
or JSON.
2. Data transformation: Use a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data. This may
include cleaning the data, handling missing values, and transforming the data
into a format suitable for analysis and visualization.
3. Database insertion: Use the "sqlite3" library in Python to
connect to a database and insert the transformed data using SQL
commands.
4. Dashboard creation: Use the Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions can be used to display the data on a map and Streamlit can be used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.
5. Data retrieval: Use the "sqlite3" library to connect to the database and fetch the data into a Pandas dataframe. Use the data in
the dataframe to update the dashboard dynamically.
6. Deployment: Ensure the solution is secure, efficient, and user-friendly. Test
the solution thoroughly and deploy the dashboard publicly, making it
accessible to users.

The sequence goes like: Saving the data from PhonePe Pulse repository into machine's folder, Extracting indian-geo-map file, Extracting Aggregated, Mapped and Top from Data, After performing cleaning Creating the final combined data excel sheet, Inserting & Fetching from library sqlite3, Showing GUI.
 
Technologies used are: Github Cloning, Python, Pandas, sqlite3, mysql-connector-python, Streamlit, and Plotly. 
Domain: Fintech

