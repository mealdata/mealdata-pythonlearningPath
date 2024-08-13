# To check python version

python --version 

# To install virtual environment 

pip install virtualenv

# To create virtual environment

python -m venv myenv # The name of venv is myenv 


# Activate venv for window 
myenv\Scripts\activate

# Activate window for MacOS
source myenv/bin/activate

# Then now Intall django 
pip install django

# To checking the version and installation 

django-admin --version
python -m django --version 

# now reday to create django admin project 
django-admin startproject myproject # where the project name is myproject

# Navigate the created project 
cd myproject
# now reday to create run the development server
python manage.py runserver

# to deactive 

deactivate



