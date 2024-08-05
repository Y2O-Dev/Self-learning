					# Object Oriented Programming Part 1
# class Staff:
    #contents of the class

class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")

    def __str__(self):
        # return "Position = %s, Name = %s, Pay = %d" %(self._position,  self.name, self.pay)
        return f"Position = {self._position}, Name = {self.name}, Pay = {self.pay}"
    @property
    def position(self):
        print("Getter Method")
        return self._position
    
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')
    
    def calculatePay(self):
        # prompt = '\n Enter number of hour worked for %s: ' %(self.name)
        prompt = f'\n Enter number of hour worked for %{self.name}: '
        hours = input(prompt)
        # prompt = "Enter the hourly rate for %s: " %(self.name)
        prompt = f"Enter the hourly rate for {self.name}: " 
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

officeStaff1 = Staff("Basic", 'Seki', 0)

class Staff:
  def __init__ (self, pPosition, pName, pPay):
    self.position = pPosition
    self.name = pName
    self.pay = pPay
    print('Creating Staff object')

  def __str__(self):
    return f"Position = {self.position}, Name = {self.name}, Pay = {self.pay}"
  
  def calculatePay(self):
    prompt = '\nEnter number of hours worked for %s: ' %(self.name)
    hours = input(prompt)
    prompt = 'Enter the hourly rate for %s: ' %(self.name)
    hourlyRate = input(prompt)
    self.pay = int(hours)*int(hourlyRate)
    return self.pay