entirety = False
GenderList = {}
ReligionsList = {}
PoliticalPartiesList = {}
AgesList = {}
JobsList = {}


def i(j):
    return input(j)

countryName = i("Country Name?\n")
Percentage = i("Percentage of people in the region?\n")
Genders = int(i("How many genders are there going to be in this country?"))
for gender in range(Genders):
    genderName = i("What's the name of this gender?")
    GenderList[genderName] = {}
    genderPopulation = float(i("What's the percentage of people with this gender?"))
    GenderList[genderName]["population"] = genderPopulation
    genderNames = int(i("How many names are there in this gender?"))
    GenderList[genderName]["Names"] = {}
    for name in range(genderNames):
        NameName = i("What's this name?")
        NamePopulation = i("What's the population of this name?")
        GenderList[genderName]["Names"][NameName] = NamePopulation

NumReligions = int(i("How many religions are there in this country?"))
for religion in range(NumReligions):
    ReligionName = i("Name of this religion?")
    ReligionPopulation = float(i("Population of this religion?"))
    ReligionsList[ReligionName] = ReligionPopulation

NumPolParties = int(i("How many religions are there in this country?"))
for polParty in range(NumPolParties):
    PartyName = i("Name of this religion?")
    PartyPopulation = float(i("Population of this religion?"))
    PoliticalPartiesList[PartyName] = PartyPopulation

NumAges = int(i("How many ages in this country?"))
for Age in range(NumAges):
    AgeName = i("Name of this age?")
    AgePopulation = float(i("Population of this age?"))
    AgesList[AgeName] = AgePopulation

NumJobs = int(i("How many jobs are in this country?")
              )
for Job in range(NumJobs):
    JobName = i("Name of this job?")
    JobPopulation = float(i("Population of this job?"))
    JobsList[JobName] = JobPopulation

finalThing = {}
#copy paste this into the big json. If this is the end, remove the comma at the end
finalThing = {"population": Percentage, "Genders": GenderList, "Political Parties": PoliticalPartiesList, "Ages": AgesList, "Jobs": JobsList}

print(' "' + countryName + '":', str(finalThing) +",")
