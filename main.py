class Factors():
        
    def __init__(self):
        self.x = int(input('Enter only one factor: '))
        self.y = int(input('Enter only one factor: '))        


class Calculator(Factors):
    
    def addition(self):
        return self.x + self.y


    def subtraction(self):
        return self.x - self.y
        
    
    def division(self):
        return self.x / self.y if self.y != 0 else "Division by zero"
        
    
    def multiplication(self):
        return self.x * self.y


class Result(Calculator):
    
    def show(self):
        x=self.x
        y=self.y
    
        addition = self.addition()
        subtraction = self.subtraction()
        division = self.division()
        multiplication = self.multiplication()
    
        print(f'\n{x} + {y} = {addition}\n')    
        print(f'{x} - {y} = {subtraction}\n')
        print(f'{x} / {y} = {division}\n')
        print(f'{x} * {y} = {multiplication}\n')
    

if __name__ == "__main__":
    Result().show()
   