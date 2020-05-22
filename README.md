This project entails the use of machine learning in predicting prices of Fairly Used Cars. This Project helps users get semi-accurate prediction of the prices of proposed cars or advice them to make price adjustments for existing ones.

##To try this project. 

fork this repository and follow the steps below

Download the weight of the model from https://drive.google.com/drive/folders/18keCSBZiV3WlCnsMPdL9pDt0e8grNiCV?usp=sharing

and create a folder named "model" inside the flaskapi folder. Put the downloaded model inside this folder.

open anaconda prompt on your pc (this is to avoid you creating a virtual environment from scratch)

run the command below.

cd into the flaskapi folder and run *python app.py*

Here is the Link to the API :  http://9e3bf3c1.ngrok.io -> http://localhost:2000 

Here is a Sample.json format for prediction which I used with Postman.

[ 
  {"vehicleType": "kleinuagen",  "yearOfRegistration": 2015, "gearbox": "manuell", "powerPS": 1400, "model": "transporter",
  "kilometer": 2000, "monthOfRegistration": 3, "fuelType": "benzin", "brand": "volkswagen", "abtest":"control" ,
  "Weekday_Created": 4, "Year_Created":2015, "Month_Created":12, "notRepairedDamage":"yes"}

]


