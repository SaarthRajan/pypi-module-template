# Template for Creating a Python Package and Publishing it to PyPI

This template helps you quickly set up your Python package and automate the publishing process to [PyPI](https://pypi.org/). Follow the steps below to use this template for your own Python package.

## Show Your Support

If you find this template useful, please consider giving it a ⭐ on GitHub! It helps others discover this project and lets me know you’re interested.

[Star this repository](https://github.com/SaarthRajan/pypi-module-template)


## Prerequisites

Before you start, make sure you have:
- A GitHub account and repository.
- A PyPI account (you can create one [here](https://pypi.org/account/register/)).
- Python 3.6 or higher installed.

### **Create a New Repository Using this Template**

To use this template:

1. Click the green **"Use this template"** button in the top right of this repository.
2. Name your repository and choose whether it will be public or private.

## Configure the Template Files

### Update `setup.py`
Ensure that the `setup.py` file is properly configured with your package's metadata. 
A template of setup.py is provided, make the appropriate changes there. 
Add all the requirements inside `install_requires` in `setup.py`. 

### Change `README.md` 
A template for the same is provided at the end of this document. Feel free to refer it.

### Add `LICENSE`
I would recommend adding MIT license. Change the License type in setup.py if using any other license.

### Add Source Code
Change the name of the `package_name/` and `package_name.py`. Add source code in `package_name.py` and `__init__.py`
Make sure the name of the package is not taken already by searching it up on PyPi. 
`__init__.py` is used for importing from `package_name.py` so that you can import it directly instead of navigating. 

### Change .gitignore
Add directories/files you want to ignore while pushing to Github. This can include env, .pyc files etc.

## Here is what the file structure should look like (you can add `tests/` and `utils.py` but they are optional)

```graphql
my_package/
├── my_package/                  # Main package directory
│   ├── __init__.py              # Package initialization file (can be empty or contain version info)
│   ├── module1.py               # A Python module (you can have many modules)
│   ├── module2.py               # Another Python module
│   └── utils.py                 # Utility functions (optional)
│
├── tests/                       # Tests directory (for unit tests)
│   ├── __init__.py              # Tests package initialization file
│   ├── test_module1.py          # Tests for module1.py
│   ├── test_module2.py          # Tests for module2.py
│   └── test_utils.py            # Tests for utils.py (optional)
│
├── setup.py                     # Package setup script
├── README.md                    # Project README (use Markdown)
├── LICENSE                      # License file (e.g., MIT, GPL)
└── .gitignore                   # Git ignore file (e.g., to ignore .pyc files, env, etc.)
```

## Follow the steps below to successfully publish your Python package to PyPI.

### Step 1: Configure `setup.py`
Ensure that your `setup.py` file is properly configured with all the necessary metadata, such as the package name, version, author, and other details.

### Step 2: Connect to PyPI
1. Visit [PyPI Account Management - Publishing](https://pypi.org/manage/account/publishing/).

### Step 3: Fill in Required Details
1. Select **Github** to link your GitHub repository to PyPI.
2. Enter the following information:
- **Name**: The name of your package. Make sure the name of the package is not taken already. 
- **Owner**: Your GitHub username.
- **Repository Name**: The name of your GitHub repository.
- **Workflow Name**: The name of your GitHub Actions workflow file, typically `python-publish.yml`.

### Step 4: Create a GitHub Release
1. Go to your GitHub repository.
2. Navigate to the **Releases** section and click on **Draft a New Release**.

### Step 5: Tag the Release
- Create a new tag (e.g., `v0.0.1` or your desired version number).
- Give the release a name that corresponds to the tag.

### Step 6: Generate Release Notes
- Click **Generate Release Notes** to automatically create notes for the release.

### Step 7: Make the Release Public
- Click on **Publish Release** to make the release public.

### Step 8: Monitor the Workflow
- Go to the **Actions** tab in your GitHub repository to monitor the progress of the workflow as it builds and publishes your package to PyPI.

Once the workflow completes successfully, your package will be available on PyPI!



# README.md template
## package_name

### What is package_name?
Here is info about the package name. 

### Features
These are the features provided by package name:
1. Feature 1
2. Feature 2

### How to install and setup package_name?

```python
import package_name as pkg
from package_name import element
```

### Usage Examples

#### Case 1
This is case 1

```python
import package_name as pkg
from package_name import element

# write code here

```

#### Case 2
This is case 2

```python
import package_name as pkg
from package_name import element

# write code here

```

### Development
Feel free to fork the project, contribute, or create an issue for any bugs or new features you'd like to see. If you're interested in collaborating, please follow the standard GitHub contribution workflow: fork, clone, create a branch, and submit a pull request.

### License
package_name is licensed under the MIT License. See the License file for more details.
