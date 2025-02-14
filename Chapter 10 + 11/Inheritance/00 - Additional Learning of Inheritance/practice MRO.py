class Iphone:
    def Feature(self):
        print("Touch Screen")

class Iphone6(Iphone):
    def Feature02(self):
        print('Front Flash')
        super().Feature()

class Iphone_plus(Iphone):
    def Feature03(self):
        print('Wireless Charging')
        super().Feature()

class Iphone7(Iphone6, Iphone_plus):
    def Feature04(self):
        print('Fingerprint Sensor')
        super().Feature02()
        super().Feature03()
         
        

Iphone_1 = Iphone()
Iphone_6 = Iphone6()
Iphone_6_plus = Iphone6()
Iphone_7 = Iphone7()

Iphone_7.Feature04()
print(Iphone7.mro())