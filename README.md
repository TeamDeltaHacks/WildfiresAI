
# [WildfiresAI](https://wildfires.ml/)

Using Machine Learning to Help Prepare for Wildfires

Learn More: https://devpost.com/software/wildfiresai

Demo: https://youtu.be/JjXK1m8niyg

## Awards
4x hackathon award winner.

* 4th Place 2021 Congressional App Challenge
* First Place Overall at Epsilon Hacks II
* Best Execution at OwlHack 2021
* Best Environment Hack at Citro Hacks

## About

![Screen Shot 2021-06-26 at 7 49 40 PM](https://user-images.githubusercontent.com/56781484/123531219-a6c1a580-d6b7-11eb-984c-4d4d00a09088.png)

Unlike other natural disasters such as hurricanes and floods, wildfires are not constrained to a certain time period during the year, making them unpredictable and unfortunately harder to combat. This is largely because 80% of wildfires are created by human error, such as through unattended campfires and discarded cigarettes. Because of the vast expanse of most forests, firefighters are often unaware of wildfires in their early stages. Due to the lack of fire department personnel, the demand for automated software to prevent wildfires from fatally progressing is increasing. While there are many existing applications that alert civilians about the presence of a wildfire, most lack the ability to provide assistance to governmental authorities in charge of wildfire management.

## Hosted Website
You can view the hosted version of our website here: [wildfires.ml](https://wildfires.ml/). Please note that some functions may not be fully operational due to memory allocation and storage issues.

## To Run Locally

### Clone
Clone the repo to your system by running the following command:

```bash
git clone https://github.com/CMEONE/WildfiresAI.git
cd WildfiresAI
```

### Dependencies
In order to install all dependencies, run `pip install -r requirements.txt` in your terminal or command prompt. 

### Running
To run the code, open a terminal and navigate to the root directory of this repository. Then, run the following bash commands:

```bash
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

As import errors arise, you may need to install more modules by using `pip install MODULE_NAME_HERE`.

Finally, once the program runs without errors, navigate to `http://127.0.0.1:5000/` in your browser.
