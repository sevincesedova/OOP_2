class sahmat_das():
    def __init__(self):
        print("sahmat daslari")

    def hereket(self):
       pass

class piyada(sahmat_das):
    def __init__(self):
        super().__init__()
        print("piyada:")

    def hereket(self):
       print ("ireli hereket")
    
class top(sahmat_das):
    def __init__(self):
        super().__init__()
        print("top:")

    def hereket(self):
        print ("ufiqi ve saquli istiqametde duz hereket")
    
class at(sahmat_das):
    def __init__(self):
        super().__init__()
        print("at:")

    def hereket(self):
        print ("2 addim ireli 1 addim saqa ve ya sola hereket")

class fil(sahmat_das):
    def __init__(self):
        super().__init__()
        print("fil:")

    def hereket(self):
        print ("diaqonal hereket")

class vezir(sahmat_das):
    def __init__(self):
        super().__init__()
        print("vezir:")

    def hereket(self):
        print ("ufiqi, saquli ve ya diaqonal hereket")

class sah(sahmat_das):
    def __init__(self):
        super().__init__()
        print("sah:")

    def hereket(self):
        print ("ufiqi, saquli ve ya diaqonal istiqametde 1 addim")
  
piyada_das = piyada()
piyada_das.hereket()
top_das = top()
top_das.hereket()
at_das = at()
at_das.hereket()
fil_das = fil()
fil_das.hereket()
vezir_das = vezir()
vezir_das.hereket()
sah_das = sah()
sah_das.hereket()
