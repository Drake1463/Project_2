#This the Meteor class
class MeteorDataEntry:
    def __init__(self,name, id ,nametype,recclass,mass,fall, year,recclat, reclong ,geolocation, states, counties):
        #This is the attributes being read in.
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass= recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.recclat = recclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.states = states
        self.counties = counties
        self.meteorArray =[]
        self.massArray = []
        self.yearArray = []
        self.massDataStr = ''
        self.yearDataStr = ''

    # This is to print the data to the filtered data file
    def massTable(self):
        # Open a file for writing, have to use encoding because the data file has special characters, without this the program will crash.
        f = open("mass_filtered_data.txt", "w", encoding="utf-8")
        #to clear out the mass data string
        self.massDataStr = ""

        # for loop for all the values in the mass array to print out.
        for i in range(0, len(self.massArray)):
            f.write(f"{i+1:<5}{self.massArray[i].name:<24}{self.massArray[i].mass:<20}\n")

            self.massDataStr = self.massDataStr + f'{self.massArray[i].name}\t{self.massArray[i].id}\t{self.massArray[i].nametype}\t{self.massArray[i].recclass}\t{self.massArray[i].mass}\t{self.massArray[i].fall}\t{self.massArray[i].year}\t' \
               f'{self.massArray[i].recclat}\t{self.massArray[i].reclong}\t{self.massArray[i].geolocation}\t{self.massArray[i].states}\t{self.massArray[i].counties}\n'
        f.close()

    # This prints the filtered year data to the year file
    def yearTable(self):
        # Open a file for writing, have to use encoding because the data file has special characters, without this the program will crash.
        f = open("year_filtered_data.txt", "w", encoding="utf-8")

        self.yearDataStr = ""

        # for loop for all the values in the year array to print out.
        for i in range(0, len(self.yearArray)):
            f.write(f"{i+1:<5}{self.yearArray[i].name:<24}{self.yearArray[i].year:<20}\n")
            self.yearDataStr = self.yearDataStr + f'{self.yearArray[i].name}\t{self.yearArray[i].id}\t{self.yearArray[i].nametype}\t{self.yearArray[i].recclass}\t{self.yearArray[i].mass}\t{self.yearArray[i].fall}\t{self.yearArray[i].year}\t' \
                                        f'{self.yearArray[i].recclat}\t{self.yearArray[i].reclong}\t{self.yearArray[i].geolocation}\t{self.yearArray[i].states}\t{self.yearArray[i].counties}\n'
        f.close()

    #this adds the Meteor's into the self.MeteorArray
    def addMeat(self, meteor,yearLimit,massLimit):
        #will put read the meteor and put it into the array
        self.meteorArray.append(meteor)

        #  check the length of the value before trying to use it to prevent error
        #  meteor being sent in is a list of the data.  It is not a MeteorDataEntry that you can reference the attributes of
        if len(meteor.mass) > 1 and len(massLimit) > 0:
           #if the meteor's mass is in the limit entered by the user then add it to massArray
           if float(meteor.mass) >= float(massLimit):
             self.massArray.append(meteor)
        # if the meteor's year is greater than or equal to  the input data and the year limit has a value then add to the yearArray
        if len(meteor.year) > 1 and len(yearLimit) > 0:
           if int(meteor.year) >= int(yearLimit):
             self.yearArray.append(meteor)

    # from task assignment to convert a value from self to a string to print out
    def data_values_to_tab_sep_string(self):
        return f'{self.name}\t{self.id}\t{self.nametype}\t{self.reclass}\t{self.mass}\t{self.fall}\t{self.year}\t' \
               f'{self.reclat}\t{self.reclong}\t{self.GeoLocation}\t{self.States}\t{self.Countries}'