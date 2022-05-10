# miR.Gut: THE MIRNA/MICROBIOTA INTERACTION DATABASE

Installation notes:

clone repo to a designated directory on your computer (i.e. in a terminal cd to where you want it)
<p>
  download .zip file into your project directory

## cd to the data dir:
Make sure the postgres.app is running on your machine
## In a terminal/shell window type
'psql' to start the postgres.app


## Connect to the miR.Gut database
\c miR.Gut

## To create the tables use, open up each sql file and follow steps specified,
  usually need to copy and paste sql commands
example## \i C:/Users/Oera/Documents/ACTUALProject/data/Taxonomy.sql
 
## populate table directly from text file
\COPY  FROM 'C:/Users/Oera/Downloads/NCBITaxonomylist.txt' with DELIMITER E'\t';


###Read through sql files to make sure steps are performed correctly to format data table perfectly
  In some cases using pgadmin4 is necessary to fix a couple data issues. For example after the 
  "Interactions" table is made, PGadmin4 is needed to edit disease names to change Crohn.s Disease
  and Alzheimer's Disease into Crohn's Disease and Alzheimer's Disease.


\q to quit

## In the pres_psql directory  (cd to main app directory)
## Edit the app.config line in get_pres.py to reflect your local address to the database

*****************************************
 Connect to your local postgres database 
*****************************************

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_login_name@localhost/president'


## create a new virtual environment in the pres_flask_postgres_template directory
python3 -m venv venv

## activate the virtual environment
source venv/bin/activate

## if you want to deactivate when your finished<p>
type deactivate to exit virtual enviro


## initialize git for this directory
git init

## install any required packages for this app
pip3 install -r requirements.txt

## USE the start.sh script in the pres_psql directory to start the app
in terminal type
./start.sh

## in your browser
## go to the localhost address to access database
http://127.0.0.1:5000/

type control c in terminal window to quit
