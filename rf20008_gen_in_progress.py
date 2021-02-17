import ast, random
data = input("input data\n")
data = ast.literal_eval(data)
print(data)
print(type(data))
populationsDict = {}
charAttributes = {"region": None, "gender": None, "name": None,
                  "Religion": None, "political party": None, "job": None,
                  "age": None}
ExtrapolationData = {}
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
    

##later I need to implement that of the data doesn't exist,
#we extrapolate data from the GSS or other similar


#first for region
n = random.random()
m = 0
i = -1

for region in regionsList:
    i += 1
    if n < m + data[region]["population"]:
        charAttributes["region"] = region
    else:
        m += data[region]["population"]
        if i + 1 == len(regionsList):
            #we will need to implement the gss thing later, for now it is pass
            pass
        #data[region]["population"] is the percentage of people in this region

#next we do Gender
gendersList = list(data[charAttributes["region"]]["Genders"].keys())
i = -1
for gender in gendersList:
    #print(gender)
    
    i += 1
    #print(data[region]["Genders"][gender])
    if n < m + data[charAttributes["region"]]["Genders"][gender]["population"]/100:
        charAttributes["gender"] = region
    else:
        m += data[charAttributes["region"]]["Genders"][gender]["population"]/100 #next one!
        if i + 1 == len(gendersList):
            #we will need to implement the gss thing later, for now it is pass
            pass
        #data[region]["population"] is the percentage of people in this region



#now, Names
NamesList = list(data[charAttributes["region"]]["Genders"][charAttributes["gender"]]["Names"].keys())
i = -1
for gender in gendersList:
    #print(gender)
    
    i += 1
    #print(data[region]["Genders"][gender])
    if n < m + data[region]["Genders"][gender]["population"]/100:
        charAttributes["gender"] = region
    else:
        m += data[region]["Genders"][gender]["population"]/100 #next one!
        if i + 1 == len(gendersList):
            #we will need to implement the gss thing later, for now it is pass
            pass
        #data[region]["population"] is the percentage of people in this region
