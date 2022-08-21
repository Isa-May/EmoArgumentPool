This is the backend of a basic application providing emotional and non-emotional arguments 
as classified by the best model of my NLP and machine learning project (see...).
The user may e.g. be a speech writer. Please note that the arguments by no means reflect my personal views. They are simply the result of a data collection for scientific purposes, 
from the following sources:


It is possible to choose arguments on the topics of ''.. 
They can be pro and contra, emotional and non-emotional.

Unit tests...

How is the database created? 

Via creating a fixture from a csv file with the emotional argument data. 
Detailed instruction can be found here: ...


1. create a model (models.py)
2. manage.py makemigrations simpleDataViewer  
3. manage.py migrate      
4. manage.py sqlmigrate simpleDataViewer 0001_initial.json    
5. python3 manage.py loaddata emotional_arguments.json    

Sources for the data are:

