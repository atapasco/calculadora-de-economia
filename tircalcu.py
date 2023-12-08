class CalculadoraTIRVAN:
    def __init__(self):
        self.convercion_meses(0.36,"meses")

    def convercion_meses(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1 * 2
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 * 3
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 * 6
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1 * 12
        return tiempo_1

    def convercion_bimestres(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1 / 2
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 * 1.5
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 * 3
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1 * 6
        return tiempo_1
    
    def convercion_trimestres(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1 / 3
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1 / 1.5
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 * 2
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1 * 4
        return tiempo_1
    
    def convercion_semestres(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1 / 6
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1 / 3
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 / 2
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1 * 2
        return tiempo_1
    
    def convercion_anos(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1 / 12
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1 / 6
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 / 4
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 / 2
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1
        return tiempo_1
    
calculadora = CalculadoraTIRVAN()
tiempo_meses = calculadora.convercion_anos(0.36, "meses")
print(tiempo_meses)

