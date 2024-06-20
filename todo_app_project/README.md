<H2> TODO Web App </H2>
By using this webapp users can add update, delete, mark_as_completed, mark_as_undone tasks.
Also users can create account and view their created and completed tasks.<br>

<ul>
<h4> To run this project locally follow below instruction </h4><br>
<li>
  first clone repo from github with this command
</li><br>
<strong> git clone https://github.com/rakesh835/snakeScript_assignment.git </strong><br>

<b>Note:- Since this project is using django version 5.0.6, so we need to install python version 3.10 or above. So if you already have lower version of python3 then after installation of newer version of python3 then replace python3 with python3.xx in all commands i.e 3.10, 3.11 or 3.12</b>


First go inside snakeScript_assignment directory, then in todo_app_project/
where manage.py is located
<li>
then create virtual environment using this command
</li>
<strong> python3 -m venv vir_env </strong>   # here vir_env is name of virtal environment, it can be anything <br>

<li>
then activate virtual environment using this command
</li>
<strong> source vir_env/Scripts/activate </strong> # here vir_env is name of virtual environment which i have created. Use your virtual environment name <br>

Make sure you are inside directory where manage.py file is located
<li>
then install all required packages from requirements.txt file 
</li>
<strong> python3 -m pip install -r requirements.txt </strong><br>

<li>
and to create database file and apply migrations, run
</li>
<strong> python3 manage.py migrate </strong><br>

<li>
Now to run web app on local server use
</li>
<strong> python3 manage.py runserver </strong>
