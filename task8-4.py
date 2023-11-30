class TV():
    def __init__(self,brand,price,inches,is_on):
        self.brand=brand
        self.price=price
        self.inches=inches
        self.channel="1"
        self.volume="50"
        self.is_on=is_on
        print("brand:",self.brand,"price:",self.price,"inches:",self.inches,is_on)
    def increasevolume(self,increasevolume):
        v=int(self.volume )+ increasevolume
        if v <= 100:
            v = int(self.volume) + increasevolume 
            print("the volume has been successfully incresed.your current volume",v)
        else:
            print("the attempt to raise the volume level was unsuccessful",self.volume)
    def decreasevolume(self,decreasevolume):
        decrease=int(self.volume)-decreasevolume
        if decrease>=0:
           decrease=int(self.volume)-decreasevolume
           print("the volume has been successfully lowerd.your current volume is",decrease)
        else:
            ("the arrempt to lowerthe volume level unsuccessful",self.volume)
    def setchannal(self,setchannal):
       changechannal=int(self.channel)+setchannal
       if changechannal<50:
           print("You have been switched to channel",setchannal)  
       else:
           print("your channal not found",self.channel)
    def resettv(self):
        print("channal:",self.channel,"volume",self.volume)
class led(TV):
    def __init__(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness=screenthickness
        self.energyusage=energyusage
        self.lifespan=lifespan
        self.refreshrate=refreshrate
        print( "screenthickness:",self.screenthickness,"energy usage:",self.energyusage,"lifespan:",self.lifespan)
    def viewingangle(self):
        print("view angle of a screen should horizontal angle 120 degree and vertical angle120 deree ")
    def backlight(self):
        print("yes")
        
class plasma(TV):
    def __init__(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness=screenthickness
        self.energyusage=energyusage
        self.lifespan=lifespan
        self.refreshrate=refreshrate
        print( "screenthickness:",self.screenthickness,"energy usage:",self.energyusage,"lifespan:",self.lifespan)
    def viewingangle(self):
        print("view angle of a screen should horizontal angle 120 degree and vertical angle 120 deree ")
    def backlight(self):
        print("NO")


m1=TV("panasonic",4200,15.7,True)
m1.increasevolume(5)
m1.setchannal(55)
m1.decreasevolume(1)
m1.resettv()

m2=led(50,"40 hz","6years",60)
m2.viewingangle()
m2.backlight()

m3=plasma(50,"40 hz","6years",60)
m3.viewingangle()
m3.backlight()


