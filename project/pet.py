class Pet:
    def __init__(self, name, hunger= 50 , energy = 50  ,happiness = 15 , instincts = None):
        self._name = name
        self._hunger = 0
        self._energy = 0
        self._happiness = 0
        self._instincts = list(instincts) if instincts is not None else []

        self.hunger = hunger
        self.enegry = energy
        self.happiness = happiness

    @property
    def name(self):
            return self._name
        
    @property
    def hunger(self):
            return self._hunger
        
    @hunger.setter
    def hunger(self, value):
            self._hunger = self._validate_0_100(value, field = "hunger")
        
    @property
    def energy(self):
            return self._energy
        
    @energy.setter
    def energy(self,value):
            self._energy = self._validate_0_100(value, field = "energy")
        
    @property
    def happiness(self):
            return self._happiness
    
    @happiness.setter
    def happiness(self, value):
          self._happiness = self._validate_0_100(value, field = "happiness")
        
    @property
    def instincts(self):
            return list(self._instincts)

    def feed(self):
        self.hunger = max(0, self.hunger -10)
    
    def play (self): 
        self.energy = max(0, self.energy - 10)
        self.happiness = max(0,self.happiness + 10)
    
    def sleep(self):
        self.energy = max(0, self.energy + 10)

    def __str__(self):
        instincts_formatted = ", ".join(self.instincts)
        return (f"Pet : {self.name}\n"
               f"Hunger: {self.hunger}\n"
               f"Energy: {self.energy}\n"
               f"Happiness: {self.happiness}\n"
               f"Instincts: {instincts_formatted}")
    
    def _validate_0_100 (self, value, field="value"):
        if not isinstance(value,(int,float)):
              raise TypeError(f"{field} must be a number")
        if value != value:
              raise ValueError(f"{field} cant be NaN.")
        
        if value < 0:
              return 0
        if value > 100:
              return 100
        return int(value)