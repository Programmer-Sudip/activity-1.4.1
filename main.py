class Employee:
    # Intializing (Constructor)
    def __init__(self):
        print("Employee created.")


    # Deleting (Destructor)
    def __del__(self):
        print("Destructor called, employee deleted.")




obj = Employee()
del obj     