# deploy-a-streamlit-app-with-heroku
yet another heroku deployment streamlit application directory...

## My deploiment's version instructions

### 1. Create your environment with Conda

```bash
# go to your directory
cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku/

```


```bash
# create the env for your streamlit app
conda create --name heroku_python_getting_started_3 python=3.9.7
```


```bash
# go into the env
conda activate requirements_1_heroku_python_getting_started_3
```

```bash
# install the packages
pip install streamlit
pip install watchdog
```

```bash
# show what the requirements
pip freeze > requirements_1_heroku_python_getting_started_3.txt
pip freeze > requirements_2_heroku_python_getting_started_3.txt
pip freeze > requirements_3_heroku_python_getting_started_3.txt
```

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install plotly-express
pip install matplotlib
pip install altair
```

```bash
# install the packages required to work with the streamlit app
numpy==1.18.4
pandas==1.0.3
seaborn==0.10.1
matplotlib==3.4.2
plotly-express==0.4.1
altair==4.1.0
```


```bash
# Let's say you create a environment with this version of python (3.8.3) if you need yo update the python version of your env
# upgrade python version in your env heroku_python_getting_started_3a
conda create --name heroku_python_getting_started_3a python=3.8.3
conda install python=3.9.7

# listing the envs
conda info --envs
conda remove --name requirements_1_heroku_python_getting_started_3 --all

# get from the current env
conda deactivate
```

### 2. change the app (tiny-streamlit-dashapp)
The app name is `tiny-streamlit-dashapp`. We will perform 2 actions:

- deploy to heroku
- update in github.com

**2.1 GIT FIRST**
```bash
cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku/

git status
# output the changes in files
git branch
# main 

# commit changes
git add .
git commit -am "update README.md"

# first push to git
git push origin main
```


**2.2 HEROKU SECOND**
- Login the Heroku CLI
```bash
heroku login
```

```bash
git add .
git commit -am "update app and requirements"
# push to heroku
git push heroku main
```


- Login the Heroku CLI
```bash
heroku login
# heroku create  #done
```

- Create a new Git repository

```bash
# go to the dir
cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku/ 
# you have probably installed before Git on your computer
git init 

# push your app with the name given by heroku
heroku git:remote -a tiny-streamlit-dashapp

# for one change... if you make
git add .
# add a commit with a message
git commit -am "remove runtime.txt"



# CAUTION depend if your branch on github is master or main

# push to heroku if your branch on github is master
git push heroku master

# push to github if your branch on github is master
git push origin master


# push to heroku if your branch on github is main
git push heroku main

# push to github if your branch on github is main
git push origin main



# other changes
git commit -am "change indent in app.py"
git commit -am "massive update app.py + runtime.txt back"
git commit -am "update requirements"
git commit -am "remove things to lighten the app"
```



In the file runtime.txt, add the correct version of pyhton you are using.

```
python-3.9.7
```

## The example given by heroku (INSTALL HEROKU-CLI AND DEPLOY PYTHON APP WITH HEROKU)

**(1.1) Install the Heroku CLI**
- requires Git installed
It supposed that Git is already installed on your computer. Check in the console with git --version
If Git is not installed, please do install it whith homebrew

--- You simply do
```bash
brew install git
# To confirm, open a new terminal window/tab and type
git --version
```

In this step you’ll install the Heroku Command Line Interface (CLI). You use the CLI to manage and scale your applications, provision add-ons, view your application logs, and run your application locally.

```bash
brew doctor 
brew update
brew install heroku/brew/heroku
heroku autocomplete
```

Source :: https://docs.brew.sh/Shell-Completion

**(1.2) Testing Heroku CLI**
```bash
heroku --version
heroku login
```

**(1.3) Take the default app**

- clone the project

```bash
git clone https://github.com/heroku/python-getting-started.git heroku-python-getting-started
```

- go to the dir
```bash
cd python-getting-started
```

**(1.4)  create your env with conda**
- Create an Environment with version Python 3.8.3 To create a virtual environment use:
```bash
conda create --name heroku_python_getting_started_1 python=3.8.3
```
- List Environments: You can list all the available environments with:
```bash
conda info --envs
```

- Activate an Environment : Before you can start using the environment you need to activate it:
```bash
source activate heroku_python_getting_started_1
```

- Deactivate an Environment If you are done working with the virtual environment you can deactivate it with:
```bash
conda deactivate
```

- Remove an Environment If you want to remove an environment from Conda use:
```bash
conda remove --name heroku_python_getting_started_1 --all
```

**(1.5)  activate the env with conda**
```bash
conda activate heroku_python_getting_started_1
```
**(1.6)  install the requirements with the requirements.txt**
! be sure to be in the "heroku_python_getting_started_1" env

```bash
pip install -r requirements.txt
```
- update the python in your environnement

```bash
conda install python=3.9
```

**(1.7)  create your app**
- Create an app on Heroku, which prepares Heroku to receive your source code:


```bash
heroku create

# Creating app... done, ⬢ agile-shore-37837
# https://agile-shore-37837.herokuapp.com/ | https://git.heroku.com/agile-shore-37837.git

```

- Heroku generates a random name (in this case agile-shore-37837) for your app, or you can pass a parameter to specify your own app name.

- Now deploy your code:
```bash
git push heroku main
```
- The application is now deployed. Ensure that at least one instance of the app is running:
```bash
heroku ps:scale web=1
```
- Now visit the app at the URL generated by its app name. As a handy shortcut, you can open the website as follows:
```bash
heroku open
```
- View information about your running app using one of the logging commands:
```bash
heroku logs --tail
```

**(1.8)  Define a Procfile**
Use a Procfile, a text file in the root directory of your application, to explicitly declare what command should be executed to start your app.

The Procfile in the example app you deployed looks like this:

```bash
web: gunicorn gettingstarted.wsgi
```

This declares a single process type, web, and the command needed to run it. The name web is important here. It declares that this process type will be attached to the HTTP routing stack of Heroku, and receive web traffic when deployed.

Procfiles can contain additional process types. For example, you might declare one for a background worker process that processes items off of a queue.

**(1.9) Scale the app**
You can check how many dynos are running using the ps command:

- excercice to scale up and down
Scaling an application on Heroku is equivalent to changing the number of dynos that are running. Scale the number of web dynos to zero:

```bash
heroku ps:scale web=0
heroku ps:scale web=1
```

**(1.10) Declare app dependencies (locally)**
```bash
pip install -r requirements.txt
pip list
```

**(1.11) Run the app locally**
! The app is almost ready to start locally. Django uses local assets, so first, you’ll need to run collectstatic:
python manage.py collectstatic

```bash
heroku local web
# Open http://localhost:5000
```


**(1.12) Make an change in the application**
In python-getting-started/hello/templates/index.html
change the H1
```bash
git add .
git commit -m "Change the H1 with a custom text"
git push heroku main
heroku open
```
- to see change locally 
```bash
heroku local web
```

**(1.13) Provision add-ons**
```bash
heroku addons:create papertrail
heroku addons
heroku addons:open papertrail
```
**(1.14) Start a console**
- do not forget to type exit
```bash
heroku run python manage.py shell
```
- To get a real feel for how dynos work, you can create another one-off dyno and run the bash command, which opens up a shell on that dyno.
```bash
heroku run bash
# type "$ exit" to exit from the terminal
```
**(1.14) More command for Heroku CLI Commands**
https://devcenter.heroku.com/articles/heroku-cli-commands

- command to view all apps
```bash
heroku apps --all 
# output
# === bflaven@gmail.com Apps
# agile-shore-37837
```

- command to destroy an app
```bash
heroku apps:destroy -a agile-shore-37837 --confirm agile-shore-37837
```

```bash
# app to run command against
-a, --app=app          
```

! ERROR_1
You may encounter issues, sometimes with the Command Line Tools for Xcode. For instance, I was forced to download Command Line Tools for Xcode 11.3.1
```bash
# remove the CommandLineTools
sudo rm -rf /Library/Developer/CommandLineTools
# reninstall via the .dmg Command Line Tools for Xcode 11.3.1
```

+ (2) DEPLOY A STREAMLIT DASHBOARD WITH HEROKU
Source: deploy-a-streamlit-dashboard-with-heroku
Source : https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku


**Heroku deployment**
```bash
cd /Users/brunoflaven/Documents/02_copy/_packt_copycat_coder/deploy-a-streamlit-dashboard-with-heroku/
```

**Always use a specific env for the dev....**

**1. required libraries for the app**
```bash
pip freeze > requirements_1_heroku_1.txt
```

Expected files for Python
Heroku automatically identifies your app as a Python app if any of the following files are present in its root directory:
```bash
requirements.txt
setup.py
Pipfile
```
If none of these files is present in your app’s root directory, the Python buildpack will fail to identify your application correctly.

You have to name "requirements.txt" if not, heroku will fail to identify your application correctly.

```bash
mv requirements_1_heroku_1.txt requirements.txt 
```

**2. setup.sh and Procfiles**
Instead of a setup.py, we will create a `setup.sh` and a `Procfile` file with these command :

```bash
touch setup.sh
touch Procfile
```
If you want color syntax with Visual Studio when you are editing, you can load this extension: https://marketplace.visualstudio.com/items?itemName=benspaulding.procfile

You need to change the code and make these specific changes:
```bash
# replace the email in setup.sh (NOT REQUIRED)
# replace the <name-of-streamlit-app>.py in Procfile ( REQUIRED)
```
**3.  Creating a Git repository for your application (first_app_heroku_deploy.py)**

I am already using an axisting git directory, so I will put all the files ina subdirectory named "deploy-a-streamlit-app-with-heroku".
So, I will not make a "git init" but a "git remote add ."

```bash
# simple example to create a directory
cd /Users/brunoflaven/Documents/03_git/BlogArticlesExamples/
mkdir deploy-a-streamlit-app-with-heroku

```

```bash
git status
cd deploy-a-streamlit-app-with-heroku
touch readme.md
# add the line # deploy-a-streamlit-app-with-heroku
cd ..
```

```bash
# no need pass this command if you have already the directory monitored by Git
git init 

# add a simple directory
git status
git add .
git commit -m "add directory deploy-a-streamlit-app-with-heroku"
git push

git commit -m "add change requirements.txt deploy-a-streamlit-app-with-heroku"
git commit -m "change pyhton version for deploy-a-streamlit-app-with-heroku"
git commit -m "change app structure"


# add the files
git status
git add .
git commit -m "add files to deploy-a-streamlit-app-with-heroku"
git push
```

- **how to remove a directory or a subdirectory**
```bash
# This deletes from filesystem
git rm -r one-of-the-directories
# Make the commit
git commit . -m "Remove duplicated directory"
# Git push (typically 'master', but not always)
git push origin <your-git-branch> 
```

- **simple example to delete a directory**

```bash
rm -r deploy-a-streamlit-app-with-Heroku
git add .
git commit -m "add deploy-a-streamlit-app-with-Heroku"
git commit -m "add files"
git push
```

```bash
git repo clone bflaven/deploy-a-streamlit-app-with-heroku
https://github.com/bflaven/deploy-a-streamlit-app-with-heroku.git
```

```bash
$ git checkout master
$ git branch main
$ git checkout main

# ...develop some code...

git add .
git commit –m "some commit"
git push

cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku
git remote add .
git commit -m "correcting spelling mistakes in readme and add files"
git remote push


git remote add origin https://github.com/Career-Karma-Tutorials/demo-repository

git remote add origin https://github.com/bflaven/deploy-a-streamlit-app-with-heroku

git push origin your-branch
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```

```bash
$ git add .
# Adds the file to your local repository and stages it for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
```

```bash
$ git commit -m "Add existing file"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
```

```bash
$ git push origin main
# Pushes the changes in your local repository up to the remote repository you specified as the origin
# git push  <REMOTENAME> <BRANCHNAME> 
# git push origin main
```

```bash
git commit -m "Add all files for streamlit app"
git commit -m "change streamlit version"
```

- to check the remote branch
```bash
git branch
# output
# * main
```



- Existing Git repository
For existing repositories, simply add the heroku remote

```bash
heroku git:remote -a tiny-streamlit-dashapp

# git@github.com:bflaven/BlogArticlesExamples.git
# https://github.com/bflaven/BlogArticlesExamples

git remote add origin https://github.com/bflaven/deploy-a-streamlit-app-with-heroku.git

git push --set-upstream origin master
git commit -m "add deploy-a-streamlit-app-with-heroku"

```



**4. Installing the Heroku Command Line Interface (CLI)**

In my case this is done.... so let's start using Heroku Command Line Interface
+ (1.2) Testing Heroku CLI
```bash
heroku --version
heroku login
# you should be login
```
- do not forget to be in your directory
```bash
cd deploy-a-streamlit-app-with-heroku/
```
- launch the creation
```bash
heroku create
```

- see the stuff
```bash
# https://nameless-woodland-72201.herokuapp.com/ | https://git.heroku.com/nameless-woodland-72201.git
```

```bash
clone https://github.com/<UserName>/mohrs_circle.git
cd mohrs_circle
```



- Create a new Git repository
Initialize a git repository in a new or existing directory
```bash
cd deploy-a-streamlit-app-with-heroku/
# no need to do that
# git init
git status
heroku git:remote -a nameless-woodland-72201
```

- Specify a Buildpack Version
```bash
heroku buildpacks:set heroku/python
```


- Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.
```bash
# push your app
git add .
git commit -am "made it or not with heroku and git 4"
git push heroku master
#git push heroku develop:master
#git push heroku main
#git push heroku develop:master
git commit -am "remove from main dir"
git push
```

- Existing Git repository
For existing repositories, simply add the heroku remote


```bash
heroku git:remote -a nameless-woodland-72201
```

- check the application
https://nameless-woodland-72201.herokuapp.com/



**ERROR_1**
``` bash
-----> Building on the Heroku-20 stack
-----> Determining which buildpack to use for this app
 !     No default language could be detected for this app.
			HINT: This occurs when Heroku cannot detect the buildpack to use for this application automatically.
			See https://devcenter.heroku.com/articles/buildpacks
 !     Push failed
```

**ERROR_2**
``` bash
-----> Building on the Heroku-20 stack
-----> Using buildpack: heroku/python
-----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
       More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
 !     Push failed
```

``` bash
heroku login
heroku git:remote -a <heroku-project-name>
git push heroku master
```

# RESSOURCES
https://www.jquery-az.com/list-branches-git/
https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository


https://tiny-streamlit-dashapp.herokuapp.com/


https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
https://pythonforundergradengineers.com/streamlit-app-with-bokeh.html
https://dash.plotly.com/deployment


https://devcenter.heroku.com/articles/git#deploying-code


https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python


https://github.com/TannerGilbert/Tutorials/tree/master/Streamlit/Deploy-Application-with-Heroku




