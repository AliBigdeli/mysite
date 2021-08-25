#

<p align="center">
  <img src="https://user-images.githubusercontent.com/29748439/130503888-ee2103cc-267f-4cfc-9ae7-b9da19f41a86.png">
  <h1 align="center">
    Django Tutorial Project
  </h1>
<p align="center">The full project for Django fundemental course in maktabkhooneh.org.</p>
</p>

<div align="center">
<a href="https://open.vscode.dev/alibigdeli/mysite.git"><img src="https://open.vscode.dev/badges/open-in-vscode.svg" height="25px"></a>

</div>

## Download & Setup Instructions :

After downloading the project, make sure to create a virtual enviroment and  install [project's requirements.](https://github.com/alibigdeli/mysite/requirements.txt)

Clone the project. This will download the GitHub respository files onto your local machine.

```Shell
git clone https://github.com/alibigdeli/mysite.git
```
installing virtual enviroment and activating:
```Shell
pip install virtualenv
```
Windows setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```

then installing the requirements:

```Shell
pip install -r requirements.txt
```
### Running the Project
in order to run the project you need to use either ways below

default and development settings
```Shell
python manage.py runserver 
#or
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.dev
```
production settings
```Shell
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.prod
```
<strong>Note:</strong> if you want to change the settings permanently to prod you can modify the settings in enviroment varibale inside the manage.py and need to use dokcer or install the mysql directly on your machine
### Project Model Schema :
this is the model schema have been used in this project:
![drawSQL-export-2021-08-23_23_26](https://user-images.githubusercontent.com/29748439/130503854-cefc63a6-1466-4164-825a-9f313d521059.png)

