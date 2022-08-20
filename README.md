How is the database created? 

Via creating a fixture from a csv file with the emotional argument data. 
Detailed instruction can be found here: ...


1. create a model (models.py)
2. manage.py makemigrations simpleDataViewer  
3. manage.py migrate      
4. manage.py sqlmigrate simpleDataViewer 0001_initial.json    
5. python3 manage.py loaddata emotional_arguments.json    

