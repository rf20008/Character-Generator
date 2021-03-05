#TODO: test
import ast, random

#data preparation
with open(input('What file? '), 'r') as f:
    data = ast.literal_eval(f.read())
    f.close()
print(data)             #debug
print(type(data))       #debug

#variables
populationsDict = {}
charAttributes = {"region": None,
                  "gender": None,
                  "name": None,
                  "religion": None,
                  "political party": None,
                  "job": None,
                  "age": None}

#custom error types
class NonExistingAttributeError(AttributeError):
    '''An attribute for the character doesn't exist!'''
    pass
class InvalidDataError(Exception):
    '''The data is invalid.'''
    pass

#TODO: move 
##Species (maybe later)
##Region,
##      Percentage of people in this region,
##  
##      Genders (names),
##          GenderName:
##              Percentage with this gender
##              Names,
##                  Name,
##                  Percentage
##        Religions (names),
##          Religion Name, Percentage
##          Percentage with this religion (in this region)
##        Political Parties (names),
##          Party name, Percentage  
##          Percentage with this party (in this region)
##        Jobs,
##          Percentage of people with this job
##        Ages,
##          Percentage of people with this age
##example:
##{
##  "Data_testregion1": {
##    "population": 99.0,
##    "Genders": {
##      "Male": {
##        "population": 50.0, "Names": {
##          "Matthew":20.0, "Andrew": 19.0, "David": 21.0, "Seth": 10.0, "Riley": 10.0, "Luke": 20.0
##        }
##      },
##      "Female": {
##        "population": 49.0, "Names": {
##            "Ophelia": 80.0, "Olivia": 20.0
##          }
##        },
##      "O": {
##        "population": 1.0, "Names": {
##          "O": 100.0
##        }
##      }
##      },
##      "Religions": {
##        "Christian": 100.0,
##      },
##      "Political Parties": {
##        "Democratic": 50.0, "Republican": 50.0
##      },
##      "Jobs": {
##        "Job1": 20.0, "Job2": 80.0
##      },
##      "Ages": {
##        10: 100.0
##      }
##    }
##}

#repeat for each region
regionsList= list(data.keys())
for region in regionsList:
    populationsDict[region] = data[region]["population"]
    

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

#TODO: simplify code
#first for region
n = random.random()
m = 0
i = -1

for region in regionsList:
    i += 1
    if n > m:
        charAttributes["region"] = region
        break
    else:
        m += data[region]["population"]
        if i + 1 == len(regionsList):
            #I will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError
        

#next we do Gender
n = random.random()
gendersList = list(data[charAttributes["region"]]["Genders"].keys())
i = -1
m=0
for gender in gendersList:
    #print(gender)
    
    i += 1
    #print(data[region]["Genders"][gender])
    if n > m:
        charAttributes["gender"] = gender
        break
    else:
        m += data[charAttributes["region"]]["Genders"][gender]["population"]/100 #next one!
        if i + 1 == len(gendersList):
            #I will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError



#now, Names
NamesList = list(data[charAttributes["region"]]["Genders"][charAttributes["gender"]]["Names"].keys())
n = random.random()
i = -1
m=0
for name in NamesList:
    #print(gender)
    
    i += 1
    #print(data[region]["Genders"][gender])
    if n > m:
        charAttributes["name"]=name
        break
    else:
        m += data[charAttributes["region"]]["Genders"][charAttributes["gender"]]["Names"][name]/100 #next one!
        if i + 1 == len(NamesList):
            #we will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError

#fourthly, religion
ReligionsList = list(data[charAttributes["region"]]["Religions"].keys())
n = random.random()
i = -1
m=0
for religion in ReligionsList:
    #print(gender)
    i += 1
    #print(data[region]["Genders"][gender])
    if n > m:
        charAttributes["religion"]=religion
        break
    else:
        m += data[charAttributes["region"]]["Religions"][religion]/100 #next one!
        if i + 1 == len(ReligionsList):
            #we will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError




#fifthly, political party (assuming political party is independent of religion, this is not the case)
PoliticalPartiesList = list(data[charAttributes["region"]]["Political Parties"].keys())
n = random.random()
i = -1
m=0
for party in PoliticalPartiesList:
    #print(gender)
    i += 1
    if n > m: 
        charAttributes["political party"]=party
        break
    else:
        m += data[charAttributes["region"]]["Political Parties"][party]/100 #next one!
        if i + 1 == len(PoliticalPartiesList):
            #we will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError
        

#sixthly, Jobs
JobsList = list(data[charAttributes["region"]]["Jobs"].keys())
n = random.random()
i = -1
m=0
for job in JobsList:
    #print(gender)
    i += 1
    if n > m:
        charAttributes["job"]=job
        break
    else:
        m += data[charAttributes["region"]]["Jobs"][job]/100 #next one!
        if i + 1 == len(JobsList):
            #we will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError


#finally, ages
AgesList = list(data[charAttributes["region"]]["Ages"].keys())
n = random.random()
i = -1
m=0
for age in AgesList:
    #print(gender)
    i += 1
    if n > m:
        charAttributes["age"]=age
        break
    else:
        m += data[charAttributes["region"]]["Ages"][age]/100 #next one!
        if i + 1 == len(AgesList):
            #we will need to implement the gss thing later, for now it is raise an error
            raise InvalidDataError
print(charAttributes)
