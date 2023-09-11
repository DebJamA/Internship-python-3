# Set Up System for Development (py-3-1)  
  
---  
  
## Set up development environment  
  
**1.** About This Mac: macOS Ventura 13.4.1  
  
**2.** Ensure [latest version of Python](https://www.python.org/downloads/) (for Mac) is installed:  
`% python3 --version`  
>Output: Python 3.11.5  
  
**3.** Upgrade pip:  
`% pip3 install --upgrade pip`  
  
`% pip3 -V`  
> Output: pip 23.2.1  
  
**4.** Install [latest version of pipenv](https://pypi.org/project/pipenv/) - a Python virtualenv management tool:  
`% pip3 install --upgrade pipenv`  
  
`% python3 -m pipenv --version`  
> Output: pipenv, version 2023.9.8  
  
**5.** Ensure [current version of Git is installed](https://git-scm.com/download/mac#:~:text=The%20latest%20version%20is%202.42.0.) and configured on Mac (using [Homebrew](https://brew.sh/)):  
`% git --version`  
> Output: git version 2.42.0  
  
**6.** Ensure current version of [PyCharm Community Edition](https://www.jetbrains.com/help/pycharm/update.html) on Mac:  
```
PyCharm > Settings: 
Appearance & Behavior > System Settings > Updates:

Current version: PyCharm 2023.1.2
Check IDE updates for: Stable Releases
Check for Updates...

PyCharm 2023.2.1 is available
Update and Restart

Current version: PyCharm 2023.2.1  
```  
  
___  
  
## Create a repository on GitHub  
  
**1.** Log in to your GitHub account [or create a GitHub account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)    
  
**2.** Create GitHub repo  
- New repository  
- Repository name: ***Internship-python-3***  
- Choose repository visibility: Public  
- Do not initialize the new repository with README, gitignore, or license files  
- Create repository  
- Copy the remote repository HTTPS URL  
  
___  
  
## Create the clock project  
  
**1.** Open PyCharm  
  
**2.** Create a new project in the repository folder `/.../.../.../Internship-python-3`  
  
**3.**  Activate `pipenv shell`  
  
**4.** Clone the Internship-python-3 repository using the HTTPS URL from GitHub  
  
`% git init`  
>Output:  
>`Initialized empty Git repository in /.../.../Internship-python-3/.git/`  
  
`% git clone https://github.com/DebJamA/Internship-python-3.git`  
>Output: 
>`warning: You appear to have cloned an empty repository`  
  
`% git checkout -b Internship-py-3-1`  
>Output:  
>`Switched to a new branch 'Internship-py-3-1'`  
  
  **5.** Set and verify new remote:  
`% git remote add clock https://github.com/DebJamA/Internship-python-3.git`  
  
`% git remote -v`  
>Output:  
>`clock  https://github.com/DebJamA/Internship-python-3.git (fetch)`  
>`clock  https://github.com/DebJamA/Internship-python-3.git (push)`  
  
**6.** Install Python style guide checker:  
`% pipenv install --dev pycodestyle`  
  
---  
  
## Update files  
  
**1.** Delete contents of `main.py`  
  
**2.** Create `.gitignore` file in root directory  
Copy/paste from [mooowooo repo](https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a)  
  
**3.** Create `README.md`  
Set Up System for Development (py-3-1)  
  
___  
  
## Push to GitHub:  
 
`% git add .`  
`% git commit -m "init project added"`  
`% git push clock Internship-py-3-1`  
  
---  
  
## Use Sourcetree  
  
**1.** Update `README.md`  
  
**2.** Download [Sourcetree](https://www.sourcetreeapp.com/)  
- Sourcetree > Settings... > Accounts > Add to add your GitHub account  
  
**3.** Upload `README.md` changes to Github using SourceTree  
- Sourcetree > New > Add Existing Local Repository:  
- Select: `Internship-python-3`  
- Open `Internship-python-3` and click on Branch `Internship-py-3-1`  
- Open `README.md` then click `Uncommitted changes` to view changes to this file  
- Click `Commit` to see staging area  
- Add commit message `updated README.md`, then click `commit`  
 - Select the commit, then click `Push`  
 - Check the box for Branch `Internship-py-3-1` then click `OK`  
 - Enter GitHub password  
  
---  
