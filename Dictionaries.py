#month conversion using dictionaries in python
monthConversion ={
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "My":"May",
        "Jn":"June",
        "jul":"jully",
        "aug":"augest",
        "sep": "september",
        "oct": "octomber",
        "nov": "november ",
        "dec": "December"
    }

print(monthConversion["Jan"])
print(monthConversion['Feb'])
print(monthConversion['sep'])

#Accesing by using get function

print(monthConversion.get("Jan"))

#get function will return default value None if not prsent in the dictionaries
print(monthConversion.get('lov'))
