# [WildfiresAI](https://wildfires.ml/)

## Awards

* First place at Epsilon Hacks II
* Best execution at OwlHack 2021

## About

![Screen Shot 2021-06-26 at 7 49 40 PM](https://user-images.githubusercontent.com/56781484/123531219-a6c1a580-d6b7-11eb-984c-4d4d00a09088.png)

Using Machine Learning to Help Prepare for Wildfires 

Learn More: https://devpost.com/software/wildfiresai

## Hosted Website
You can view the hosted version of our website here: [wildfires.ml](https://wildfires.ml/). Please note that some functions may not be fully operational due to memory allocation and storage issues.

## To Run Locally

### Dependencies
In order to install all dependencies, run `pip install -r requirements.txt` in your terminal or command prompt. 

### Running
To run the code, open a terminal and navigate to the root directory of this repository. Then, run the following commands:

#### For MacOS
```bash
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

#### For Windows
```bash
set FLASK_ENV=development
set FLASK_APP=app.py
flask run
```

As import errors arise, you may need to install more modules by using `pip install MODULE_NAME_HERE`.

Finally, once the program runs without errors, navigate to `http://127.0.0.1:5000/` in your browser.
