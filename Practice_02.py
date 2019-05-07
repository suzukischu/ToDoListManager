#Header File portion of the program
import datetime
ThisDate = datetime.datetime.now()
ToDoList = []


def create_task_details():

    task_q = input('would you like to add a new task? y/n ')
    num_tasks = int(input('How many task would you like to add? '))

    if (task_q == 'y'):
        for num in range(num_tasks):

            task = []

            job = input('What do you need to do?')
            priority = input('What is the priority of the new task? 0-10 ')
            date = ThisDate.strftime("%Y-%m-%d %H:%M")

            task= {"Task : " :job, 'Priority : ' :priority, 'Date  ': date}

            ToDoList.append(task)

    else:
        print('fine I guess you have some freetime.')

    print(ToDoList)


#def create_List():
    #try
        #f.read(ToDoList)
        # Need to write code here to pull in the file content
        # if (there is no list run this to make the list
        #f = open("To_Do_List.txt", "w")
        #f.write(ToDoList)
    #else #If there is a list
        #read_in_list()
        #f= open(ToDoList)
        #f.write("ToDoList.txt", "a")
        #f.close(ToDoList)



#def read_in_list(): (use this is they say they want to append a list
    #try
        #f.read(ToDoList)
        #Write code here to write the current file to the ToDoList
        #f.close(ToDoList)


#def edit_list():


#Prioritze_List():
    #Write some code here to take the contents of the list and prioritize it
    #by the priority part of the ToDoList dictionary


#Make_Print_out():
    #Make a printable version of the list here



def main():

    option = input('What would you like to do \n Create a new task (1) \n See the current to-do-list (2) \n exit (3) ')

    if (option == '1'):
        create_task_details()

    elif (option == '2'):
        print(ToDoList)

    else:
        print (" Alright don't do anything, have a good day")


main()


