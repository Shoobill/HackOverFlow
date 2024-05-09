import csv

class CrimeDataAnalyzer:
    def __init__(self, file_name, address):
        self.file_name = file_name
        self.address = address
    
    def countLocationOccurrences(self):
        count = 0
        with open(self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[1] == self.address:
                    count += 1
        return count
    
    def createDescription(self):
        location_occurrences = self.countLocationOccurrences()
        description_list = []
        description = ""
        with open(self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[1] == self.address:
                    description_list.append(row[0])
        
        hitRunCount = 0
        motorTheftCount = 0
        theftCount = 0
        hateCrimeCount = 0
        stalkingCount = 0
        sexualAssaultCount = 0
        
        for crime in description_list:
            if crime == "Hit and Run":
                hitRunCount += 1
            elif crime == "Motor Vehicle Theft":
                motorTheftCount += 1
            elif crime == "SEXUAL ASSAULT":
                sexualAssaultCount += 1
            elif crime == "Theft":
                theftCount += 1
            elif crime == "Stalking": 
                stalkingCount += 1
            elif crime == "Hate Crime": 
                hateCrimeCount += 1
        
        description_counts = [
            (hitRunCount, "Hit and Run"),
            (motorTheftCount, "Motor Vehicle Theft"),
            (sexualAssaultCount, "SEXUAL ASSAULT"),
            (theftCount, "Theft"),
            (stalkingCount, "Stalking"),
            (hateCrimeCount, "Hate Crime")
        ]
        
        description = ", ".join([f"{crime} ({count})" for count, crime in description_counts if count > 0])
        return description

# Example usage:
'''analyzer = CrimeDataAnalyzer('crime_data.csv', '4395 University Dr, Fairfax, VA 22030')
print(analyzer.createDescription())

analyzer2 = CrimeDataAnalyzer('crime_data.csv', '10399 Senatorial Ln, Fairfax, VA 22030')
print(analyzer2.createDescription())

analyzer3 = CrimeDataAnalyzer('crime_data.csv', '4400 University Dr, Fairfax, VA 22030')
print(analyzer3.createDescription())'''
