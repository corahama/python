class Galleta():
    chocolate = False

    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print('Se a creado una galleta {} y {}'.format(sabor, forma))
        else:
            print('Se acaba de crear una galleta')

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate == True:
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")

una_galleta = Galleta()
una_galleta.tiene_chocolate()
una_galleta.chocolatear()
una_galleta.tiene_chocolate()
