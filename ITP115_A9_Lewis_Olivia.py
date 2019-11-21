# Olivia Lewis
# ITP 115 Fall 2019
# Assignment 9
# olewis@usc.edu
# File Reading
def main():

    # prompt the user to enter a year they would like the data for
    year = input("What year you would like to view the data for? (2008 or 2009) ")
    while year != "2008" and year != "2009":
        print("Invalid input, please try again.")
        year = input("What year would you like to view the data for? (2008 or 2009) ")
    if year == "2008":
        fileIn = open("epadata2008.csv", "r")
    elif year == "2009":
        fileIn = open("epadata2009.csv", "r")
    # create empty list to store data
    validCarList = []
    for line in fileIn:
        # remove whitespace
        line = line.strip()
        # use the split function to create a list
        lineList = line.split(",")
        # make sure that lines containing minivans, vans, and trucks are not included
        if "TRUCKS" not in lineList[0] and "VANS" not in lineList[0] and "MINIVAN" not in lineList[0]:
            # add the lines that do not contain minivan, van or truck to the valid car list defined above
            validCarList.append(lineList)
    # close the file
    fileIn.close()
    # delete the line that has the identifying information
    del validCarList[0]
    # set minimum and maximum original values
    # minimum is the 8th index of the first car in the data set to start
    minimum = int(validCarList[0][8])
    maximum = 0
    # create empty lists for minimums and maximums
    minimumList = []
    maximumList = []
    for carInfo in validCarList:
        # if the city MPG stored at index[8] is less than the minimum, we want to create a new minimum list
        if int(carInfo[8]) < minimum:
            minimum = int(carInfo[8])
            minimumList = [carInfo[1:3]]
        # if the MPG is the same as the current minimum, we want to append it to the original minimum list
        elif int(carInfo[8]) == minimum:
            # create a new list element to add to the minimum list
            minimumList.append(carInfo[1:3])
        # use the same logic to determine if the MPG is a maximum
        if int(carInfo[8]) > maximum:
            maximum = int(carInfo[8])
            maximumList = [carInfo[1:3]]
        elif int(carInfo[8]) == maximum:
            maximumList.append(carInfo[1:3])
    # get user input to name the .txt file
    textFile = input("Enter a file name to save results to: ")
    # create the output file and write the results into it
    textFileName = open(textFile, "w")
    print("EPA City MPG (" + year + ")", file=textFileName)
    print("- - - - - - - - - - - - - - -", file=textFileName)
    print("Maximum Mileage (city): ", maximum, file=textFileName)
    for cars in maximumList:
        print("\t", cars[0], cars[1], file=textFileName)
    print("Minimum Mileage (city): ", minimum, file=textFileName)
    for cars in minimumList:
        print("\t", cars[0], cars[1], file=textFileName)
    textFileName.close()
    # print closing statements
    print("Operation success! Mileage data has been saved to", textFile)
    print("Thank you, have a nice day!")
# call main
main()


