def table(file):
    '''
    function creates a table for elephant trip and prints it

    :param file: str of the file name that you want to make a table out of
    :return: nothing, but program prints the table

    pseudo-code:
    create an empty dictionary
    open the file in read mode
    iterate through and get the values into the dictionary
    print the table using formatted output and sorting the dictionary so the stop numbers are in order
    close the file
    '''
    tripDict = {}
    data = open(file,'r')
    print('{0}{1:^11s}{0}{2:^50s}{0}{3:^40s}{0}{4:^20s}{0}{5:^20s}{0}{6:^20}{0}'.format('|','Stop Number','Address','Distance since last stop (km)','Time elapsed','Elephants Watered?','Elephants Fed?'))
    print('-'*170)

    for x in data:
        x = x.split(',')
        x.remove('\n')
        tripDict[x[0]] = x

    for i in sorted(tripDict):
        print('{0}{1:^11s}{0}{2:^50s}{0}{3:^40s}{0}{4:^20s}{0}{5:^20s}{0}{6:^20}{0}'.format('|',tripDict[i][0],tripDict[i][1],tripDict[i][2],tripDict[i][3],tripDict[i][4],tripDict[i][5]))
    data.close()
    return()

def read(file):
    '''
    function reads a file and puts its contents into a dictionary

    :param file: str of the file name that you want to read
    :return: the elements of the file in dictionary formated with the stop number as the key

    pseudo-code:
    open the file in read mode
    create an empty dictionary
    iterate through the file and put the elements into the dictionary
    close the file
    return the dictionary
    '''
    data = open(file,'r')
    tripDict = {}
    for x in data:
        x = x.split(',')
        x.remove('\n')
        tripDict[x[0]] = x
    data.close()
    return(tripDict)

def write(tripDict,wfile):
    '''
    writes specified dictionary into a specified file

    :param tripDict: Dictionary format, the one that you want to write with
    :param wfile: str name of the file you want to write into
    :return: nothing

    pseudo-code:
    open wfile in write mode
    iterate through the dictionary, writing its elements into the file with the proper format
    close the file
    '''
    tripfile = open(wfile,'w')
    for x in tripDict:
        for i in tripDict[x]:
            tripfile.write(str(i)+',')
        tripfile.write('\n')

    tripfile.close()
    return()

def timecalc(starttime,endtime):
    '''
    calcultes the hour and mintute differences of a starting and ending time

    :param starttime: str of the starting time in 24 hour format
    :param endtime: str of the ending time in 24 hour format
    :return: the hour difference and minute difference in int

    pseudo-code:
    split starttime and endtime by the : between the hour and minutes, then assign them to variables
    change all the variables containing the starting/ending hours and mins into int
    the difference in hours is the absolute value difference between the two
    the difference in mins is the absolute value difference between the two
    return hour and min
    '''
    shour, smin = starttime.split(':')
    ehour, emin = endtime.split(':')
    shour, smin, ehour, emin = int(shour), int(smin), int(ehour), int(emin)
    hour = abs(shour - ehour)
    min = abs(smin - emin)

    return(hour,min)

def add(id,address):
    '''
    adds a stop to the elephant trip database

    :param id: str stop number before the one that is going to be added
    :param address: str address of the new stop
    :return: str of the added stop and its contents

    pseudo-code:
    iterate through the data file containing the trip details and turn the elements into a dictionary
    iterate backwards through the keys of the dictionary
    if the key value is less than the id number, replace the key with key+1
    change the stop value of the changed key to key+1 as well
    add the new key into the dictionary with its own values
    write the modified dictionary back into the file
    return the string value of the new stop and its contents
    '''
    tripDict = read('tripdata.csv')
    for keys in range(len(tripDict),1,-1):
        if keys > int(id):
            tripDict[str(int(keys)+1)] = tripDict.pop(str(keys))
            tripDict[str(int(keys)+1)][0] = str(int(keys)+1)

    tripDict[str(int(id)+1)] = [str(int(id)+1),address,'-','-','-','-']
    write(tripDict,'tripdata.csv')
    return(str(tripDict[id]))

def delete(id):
    '''
    deletes a stop from the elephant trip database

    :param id: str stop number of the stop that is to be deleted
    :return: nothing

    pseudo-code:
    iterate through the file and put its contents into a dictionary
    iterate through the dictionary starting range from 1
    if the loop control variable is > the id, replace the corresponding key in the dictionary with itself -1
    replace its stop number with itself - 1 as well
    write the modified dictionary into the file

    '''
    tripDict = read('tripdata.csv')
    for keys in range(1,len(tripDict)+1):
        if keys > int(id):
            tripDict[str(int(keys)-1)] = tripDict.pop(str(keys))
            tripDict[str(int(keys)-1)][0] = str(int(keys)-1)
    write(tripDict,'tripdata.csv')
    return()


#these lists are used to make printing out options of the user easier with enumerate
action_list = ['Begin Tracking','Modify Trip information','Add or delete stops','Produce report','Close the program']
field_list = ['water','food','distance','time','address']
'''
Jason Zhang
Mar 30 2017
Submitted to Mr.Cope ICS3U1-03

ElephantTripv4.py
a menu that tracks a truck driver's journey to deliver elephants from one place to another
utilises file io techniques to save changes to a csv file on drive

improved organization of code, better way of outputting options in the menu with enumerate, a "travel mode" that makes it
easier for user to input data as they continue the trip that replaced the view trip progress option (since it was terrible)
added a time calculator that gets the difference between inputted 24 hour clock times, making it easier for drivers to input
time elapsed during travel mode. modification mode is now used if user made a mistake and wants to change it. Finally
another option for creating and displaying a report is added.

input: user inputs options the menu prompts them with usually str
output: various outputs depending on user choice, usually str

pseudo-code:
While loop creates a repeating menu until user quits
use enumerate and lists to give user options
print a table of the current data so user is always informed
if user option is 1
    ask user which stop they are starting from, and using that int value for the beginning range of a for loop
    this loop will continue until they reach the last stop or when they enter m when prompted
    tell them their stop number
    if they arent at the begining, start them 1 stop after where they left off
    open the file where the trip info will be stored and put its contents into a dictionary
    ask the user to input values for water, distance, time and feed
    write the new dictionary data back into the file
    close the file
    ask user if they want to return to menu, if not, the loop continues
    when loop reaches the end, tell user that they have completed the trip

if user option is 2
    ask user for the stop number that they wish to modify info for
    give them their options to modify: address, food, water, distance and time
    iterate through the data file and put its contents into a dictionary
    modify the dictionary based on user input
    write the contents of the dictionary back into the data file
    close the file

if user option is 3
    ask them if they want to add or delete
    if they want to add:
        print the table version of the current data
        ask user for address, stop number and estimated distance (to make sure the route is appropriate)
        if distance is acceptable, add the new stop with the add function

    if they want to delete:
        print the table version of the current data
        issue a warning to the user for deleting stops
        ask for stop number
        delete the stop with the delete function

if user option is 4
    ask user if they want to create the final report in cvs format or just want to see a preview
    if they want to create the final report:
        write current data into a new file called tripreport with appropriate csv format
    if they want to see the preview
        print the table
        print the total distance and time

if user option is 5
    quits the menu
'''
while True:
    print()
    print()
    table('tripdata.csv')
    print()
    print('Welcome to Elephant Trip planner')
    print()
    print('Here are your choices:')
    for number, action in enumerate(action_list,1):
        print(str(number)+'.', action)
    print()
    userinp = str(input('Please enter your choice here (1-5): '))
    if userinp == '1':
        print()
        begining = int(input('Please input the stop number from where you left off, or 1 to begin the trip: '))
        tripDict = read('tripdata.csv')
        if begining != 1:
            begining += 1
        for i in range(begining,len(tripDict)+1):
            print('you are at stop number:{0}'.format(i))
            print()
            distance = str(input('Please input the distance since the last stop (0 if you just started): '))
            tripDict[str(i)][2] = distance
            if distance >= '700':

                print('< You should probably water the elephants. >')
            water = str(input('Please input wether you have watered the elephants (yes or no): '))
            tripDict[str(i)][4] = water

            if i == '3' or i == '6':
                print('You should feed the elephants')
            feed = str(input('Please input wether you fed the elephants (yes or no): '))
            tripDict[str(i)][5] = feed

            if i != 1:
                endtime = str(input('Please input the current time in 24 hour format (hr:min): '))
                starttime = str(input('Please input the time you left the last stop in 24 hour format (hr:min): '))
                hour,min = timecalc(starttime,endtime)
                tripDict[str(i)][3] = '{0} h {1} min'.format(hour,min)

            else:
                tripDict[str(i)][3] = '0 h 0 min'

            write(tripDict,'tripdata.csv')
            leave = str(input('Input m to return to main menu and modify info (changing stops), if not, press any key: '))

            if leave == 'm':
                print('returning to main menu')
                break
        print()
        print('You have completed the Trip!')

    elif userinp == '2':

        tripDict = read('tripdata.csv')
        print()
        table('tripdata.csv')
        print()
        stopnum = str(input('Please input the stop number you are changing: '))
        editnum = int(input('Please input the number of fields you wish to modify (1-5): '))
        for x in range(0,editnum):
            print('Here are your options for modification')
            for number, field in enumerate(field_list,1):
                print(str(number)+'.',field)
            print()
            option = str(input('Please input your option: '))
            if option == '1':
                waterinp = str(input('input yes if you watered the elephants, and no if you did not: '))
                tripDict[stopnum][4] = waterinp

            elif option == '2':
                foodinp = str(input('input yes or no: '))
                tripDict[stopnum][5] = foodinp
            elif option == '3':
                distanceinp = str(input('Please input the distance since the last stop: '))
                tripDict[stopnum][2] = distanceinp

            elif option == '4':
                timeinp = str(input('Please input the time elapsed since the last stop (e.g 2 h 30 min): '))
                tripDict[stopnum][3] = timeinp

            elif option == '5':
                addressinp = str(input('Please input the new address: '))
                distancecheck = str(input('Please input the estimated distance between the current stop and the new address: '))
                if distancecheck > '800':
                    print('Sorry, but the distance is too far for the elephants, please reconsider and try again.')
                else:
                    tripDict[stopnum][1] = addressinp
            else:
                print('invalid input, try again')

        write(tripDict,'tripdata.csv')

        table('tripdata.csv')

    elif userinp == '3':
        print()
        choice = str(input('Would you like to Add or Delete? Input 1 to add and 2 to delete: '))
        if choice == '1':
            print('Please keep in mind that you cannot change the start and destination.')
            print()
            table('tripdata.csv')
            print()
            id = str(input('Please input the stop number of the stop before the stop you want to add (if you want to add a stop after 3, input 3): '))
            address = str(input('Input the address of the new stop: '))
            distancecheck = str(input('Please input the estimated distance between the new stop and its previous stop: '))
            if distancecheck > '800':
                print('Sorry, but the distance is too far for the elephants, please reconsider and try again.')
            else:
                print('You added: '.format(add(id,address)))

        if choice == '2':
            print()
            table('tripdata.csv')
            print()
            print('If you have less than 7 stops total, make sure to plan the trip properly so that the elephants will have a comfortable trip.')
            print('Remember that the distance between each stop should be 800km max.')
            id = str(input('Please input the stop number of the stop you want to delete: '))
            delete(id)
            print('The stop {0} has been deleted'.format(id))

    elif userinp == '4':
        print()
        confirm = str(input('If you are at the destination and all data has been correctly recorded, input 1, if you want just a preview, input 2: '))
        if confirm == '1':

            tripDict = read('tripdata.csv')
            tripfile = open('tripreport.csv','w')
            tripfile.write('Stop Number,Address,Distance since last stop (km),Time elapsed,Elephants Watered?,Elephants Fed?\n')
            for x in tripDict:
                for i in tripDict[x]:
                    tripfile.write(str(i)+',')
                tripfile.write('\n')

            tripfile.close()

            totalDistance = 0
            totalh = 0
            totalm = 0
            for x in tripDict:
                totalDistance += int(tripDict[x][2])
                timelist = tripDict[x][3].split()
                totalh += int(timelist[0])
                totalm += int(timelist[2])

            tripfile = open('tripreport.csv','a+')
            tripfile.write('The total time of the trip was: {0} h and {1} mins\n'.format(totalh,totalm))
            tripfile.write('The total distance traveled was: {0} km'.format(totalDistance))
            tripfile.close()
            print('The report has been created under the file name: tripreport.csv')

        if confirm == '2':
            print()
            table('tripdata.csv')
            print()
            tripDict = read('tripdata.csv')
            totalDistance = 0
            totalh = 0
            totalm = 0
            for x in tripDict:
                totalDistance += int(tripDict[x][2])
                timelist = tripDict[x][3].split()
                totalh += int(timelist[0])
                totalm += int(timelist[2])

            print('The total time of the trip was: {0} h and {1} mins'.format(totalh, totalm))
            print('The total distance traveled was: {0} km'.format(totalDistance))
            print()
            print('-'*170)

    elif userinp == '5':
        print('Goodbye')
        break


