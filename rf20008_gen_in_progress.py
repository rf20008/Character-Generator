#TODO: test
GUI = False
import ast, random

#returning - preparing for GUI-ification (although I haven't figured how to make this return anything)
def JSONify(chardatas = [{"exists": "false"}], success="true",
            errorCause = "No Error", debugInfo = "Debug information not avaliable"
            , extraInfo = {"exists": "false"}):
    if not success == "true":
        
        return {"success": success, "characters": chardatas, "cause": errorCause, "debug": debugInfo, "extraInfo":extraInfo}
    else:
        return {"success": success, "characters":  chardatas, "debug": debugInfom "extraInfo": extraInfo}
#for gui-ification
if GUI:
            import requests





#data preparation
with open(input('What file? '), 'r') as f:
    data = ast.literal_eval(f.read())
    f.close()

#variables
populationsDict = {}
charAttributes = {"exists": "true"
    "region": None,
                  "gender": None,
                  "name": None,
                  "religion": None,
                  "political party": None,
                  "job": None,
                  "age": None}

#custom error types
#TODO: eliminate or make more pythonic
class NonExistingAttributeError(AttributeError):
    '''An attribute for the character doesn't exist!'''
    pass
class InvalidDataError(Exception):
    '''The data is invalid.'''
    pass

#selects from categorical distribution as represented in dictionary
#code credit to StackOverflow user "Boojum"
#https://stackoverflow.com/questions/3655430/selection-based-on-percentage-weighting
def select(values):
    '''Selects randomly from a categorical distribution.
    {any : numeric} -> any'''
    variate = random.random() * sum( values.values() )
    cumulative = 0.0
    for item, weight in values.items():
        cumulative += weight
        if variate < cumulative:
            return item
    return item # Shouldn't get here, but just in case of rounding...

#TODO: implement random trait selection for all traits

#first for region
region = select({region: data[region]["population"] for region in data.keys()})
print(f'region = {region}') #debug
charAttributes["region"] = region
#gender?
gender = select({gender: data[region]["Genders"][gender]["population"] for gender in data[region]["Genders"].keys()})
print(f'gender = {gender}') #debug
charAttrributes["gender"]=gender



##########-------------------------------------------#########
#Old code burial
#########---------------------------------------------########
#burial starts under this line
############-----------------------------------------#########
###next we do Gender
##gendersList = list(data[charAttributes["region"]]["Genders"].keys())
##print(f'gendersList = {gendersList}') #debug
###now, Names
##NamesList = list(data[charAttributes["region"]]["Genders"][charAttributes["gender"]]["Names"].keys)
##print(f'NamesList = {NamesList}') #debug
###fourthly, religion
##ReligionsList = list(data[charAttributes["region"]]["Religions"].keys())
##print(f'ReligionsList = {ReligionsList}') #debug
###fifthly, political party
###assuming political party is independent of religion
##PoliticalPartiesList = list(data[charAttributes["region"]]["Political Parties"].keys())
##print(f'PoliticalPartiesList = {PoliticalPartiesList}') #debug
###sixthly, Jobs
##JobsList = list(data[charAttributes["region"]]["Jobs"].keys())
##print(f'JobsList = {JobsList}') #debug
###finally, ages
##AgesList = list(data[charAttributes["region"]]["Ages"].keys())
##print(f'AgesList = {AgesList}') #debug
