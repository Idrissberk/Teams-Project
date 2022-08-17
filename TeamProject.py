import sqlite3
class Team():
    def __init__(self,name):
        self.name = name
        self.state = True
        self.connectDatabase()
    
    def run(self):
        self.menu()
        choice = self.choice()
        
        if choice == 1:
            self.add()

        if choice == 2:
            self.delete()

        if choice == 3:
            self.update()

        if choice == 4:
            while True:
                try:
                    orderby = int(input("1) All\n2) Position\n3) Category\n4) Number\n5) Status\nSelect: "))
                    if orderby not in(1,2,3,4,5):
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            self.show(orderby)

        if choice == 5:
            self.exit()

    def menu(self):
        print("\n***** {} Manager Settings *****".format(self.name))
        print("""
1. Add Player
2. Delete Player
3. Update Player
4. Show Players
5. Exit
""")

    def choice(self):
        while True:
            try:
                process = int(input("Select: "))
                if process not in(1,2,3,4,5):
                    print("Process is must be between 1-5. Please select correct number!")
                    continue
                break
            except ValueError:
                print("Process is must be integer number. Please write correct type!")
        return process

    def add(self):
        print("**** Player Information ****")
        name = input("Player's Name: ").lower().capitalize()
        surname = input("Player's Surname: ").lower().capitalize()
        position = input("Player's Position: ").lower().capitalize()
        division = input("Player's Category(A team or youths): ").lower().capitalize()
        while True:
            try:
                plnumber = input("Player's Number: ")
                break
            except ValueError:
                print("Number must be integer!")
        status = "Active"

        self.cursor.execute("INSERT INTO players VALUES('{}','{}','{}','{}',{},'{}')".format(name,surname,position,division,plnumber,status))
        self.connect.commit()
        print(f"The player name {name} {surname} successfully added")

    def delete(self):
        self.cursor.execute("SELECT * FROM players")
        allPlayers = self.cursor.fetchall()
        convertAllStr = lambda a:[str(b) for b in a]
        for i,j in enumerate(allPlayers,1):
            print("{}) {} ".format(i," ".join(convertAllStr(j))))

        while True:
            try:
                select = int(input("Select the student to be deleted: "))
                if select < 1 or select > len(allPlayers):
                    continue
                break
            except ValueError:
                print("Please write correct type (integer)!")
        self.cursor.execute("DELETE FROM players WHERE rowid={}".format(select))
        self.connect.commit()
        print("\n\tStudent successfully deleted!")

    def update(self):
        self.cursor.execute("SELECT * FROM players")
        allPlayers = self.cursor.fetchall()
        convertAllStr = lambda a:[str(b) for b in a]
        for i,j in enumerate(allPlayers,1):
            print("{}) {} ".format(i," ".join(convertAllStr(j))))
        
        while True:
            try:
                select = int(input("\nSelect the player to be update: "))
                if select < 1 or select > len(allPlayers):
                    continue
                break
            except ValueError:
                print("Please write correct type (integer)")
        
        while True:
            try:
                updateSelect = int(input("1-Name\n2-Surname\n3-Position\n4-Category\n5-Number\n6-Status\nEnter the value to update: "))
                if updateSelect not in(1,2,3,4,5,6):
                    continue
                break
            except ValueError:
                print("it must be integer!")
        
        operations = ["name","surname","position","category","number","status"]
        
        if updateSelect == 5:
            while True:
                try:
                    newValue = int(input("Enter the new value: "))
                    if newValue < 1 or newValue > 99:
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            self.cursor.execute("UPDATE players SET number={} WHERE rowid={}".format(newValue,select))
        else:
            newValue = input("Enter the new value: ")
            self.cursor.execute("UPDATE players SET {}='{}' WHERE rowid={}".format(operations[updateSelect-1],newValue,select))

        self.connect.commit()

        print("Update Success!")

    def show(self,by):
        if by == 1:
            self.cursor.execute("SELECT * FROM players")
        allPlayers = self.cursor.fetchall()
        convertAllStr = lambda a:[str(b) for b in a]
        for i,j in enumerate(allPlayers,1):
            print("{}) {} ".format(i," ".join(convertAllStr(j))))
        
        if by == 2:
            self.cursor.execute("SELECT position FROM players")
            positions = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in positions:
                print("{}) {} ".format(i,j[0]))
            
            while True:
                try:
                    select = int(input("\nSelect: "))
                    if select < 1 or select > len(positions):
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            
            self.cursor.execute("SELECT * FROM players WHERE position='{}'".format(positions[select-1][1][0]))
            
            allPlayers = self.cursor.fetchall()
            convertAllStr = lambda a:[str(b) for b in a]
            for i,j in enumerate(allPlayers,1):
                print("{}) {} ".format(i," ".join(convertAllStr(j))))

        if by == 3:
            self.cursor.execute("SELECT category FROM players")
            categories = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in categories:
                print("{}) {} ".format(i,j[0]))
            
            while True:
                try:
                    select = int(input("\nSelect: "))
                    if select < 1 or select > len(categories):
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            
            self.cursor.execute("SELECT * FROM players WHERE category='{}'".format(categories[select-1][1][0]))
           
            allPlayers = self.cursor.fetchall()
            convertAllStr = lambda a:[str(b) for b in a]
            for i,j in enumerate(allPlayers,1):
                print("{}) {} ".format(i," ".join(convertAllStr(j))))

        if by == 4:
            self.cursor.execute("SELECT number FROM players")
            numbers = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in numbers:
                print("{}) {} ".format(i,j[0]))
            
            while True:
                try:
                    select = int(input("\nSelect: "))
                    if select < 1 or select > len(numbers):
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            
            self.cursor.execute("SELECT * FROM players WHERE number={}".format(numbers[select-1][1][0]))
           
            allPlayers = self.cursor.fetchall()
            convertAllStr = lambda a:[str(b) for b in a]
            for i,j in enumerate(allPlayers,1):
                print("{}) {} ".format(i," ".join(convertAllStr(j))))

        if by == 5:
            self.cursor.execute("SELECT status FROM players")
            state = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in state:
                print("{}) {} ".format(i,j[0]))
            
            while True:
                try:
                    select = int(input("\nSelect: "))
                    if select < 1 or select > len(state):
                        continue
                    break
                except ValueError:
                    print("Please, it must be integer!")
            
            self.cursor.execute("SELECT * FROM players WHERE status='{}'".format(state[select-1][1][0]))
           
            allPlayers = self.cursor.fetchall()
            convertAllStr = lambda a:[str(b) for b in a]
            for i,j in enumerate(allPlayers,1):
                print("{}) {} ".format(i," ".join(convertAllStr(j))))

    def exit(self):
        self.state = False

    def connectDatabase(self):
        with sqlite3.connect("Teams.db") as self.connect:
            self.cursor = self.connect.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS players(name TEXT, surname TEXT, position TEXT, category TEXT, number INT, status TEXT)")
            self.connect.commit()


team = Team("Liverpool F.C.")
while team.state:
    team.run()