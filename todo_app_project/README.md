<H2> TODO Web App </H2>
By using this webapp users can add update, delete, mark_as_completed, mark_as_undone tasks.
Also users can create account and view their created and completed tasks.

### To run this project locally follow below instruction

first clone repo from github using this command
#### git clone https://github.com/rakesh835/snakeScript_assignment.git

<b>Note:- Since this project is using django version 5.0.6, so we need to install python version 3.10 or above. So if you already have lower version of python3 then after installation of newer version of python3 then replace python3 with python3.xx in all commands i.e 3.10, 3.11 or 3.12</b>
  
First go inside snakeScript_assignment directory where manage.py located

then create virtual environment using this command
#### python3 -m venv vir_env   # here vir_env is name of virtal environment, it can be anything

then activate virtual environment using this command
#### source vir_env/Scripts/activate

then install all required packages to run the app from requirements.txt file
#### pip3 install -r requirements.txt 

to apply migration and create default tables in database run
#### python3 manage.py migrate

Now to run web app on local server use
#### python3 manage.py runserver
