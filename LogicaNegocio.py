import math

class InteresSimple:
    
    def hallar_valor_final(self, interes_porcentual, valor_inicial_deuda, tiempo_deuda, intervalo_tiempo, tiempo_deuda_2, intervalo_tiempo_2):

        tiempo_deuda = self.tiempo_deuda(intervalo_tiempo, tiempo_deuda, tiempo_deuda_2, intervalo_tiempo_2)
        return valor_inicial_deuda * (interes_porcentual / 100) * tiempo_deuda

    
    def hallar_tiempo(self, valor_final, interes_porcentual, valor_inicial_deuda):
        resultado_en_dias = (valor_final / (valor_inicial_deuda * (interes_porcentual / 100))) * 365.25
        anios, meses, dias_restantes = self.convertir_dias_a_anios_meses_dias(resultado_en_dias)
        return (f"{int(anios)} años, {int(meses)} meses y {int(dias_restantes)} días.")

    def hallar_valor_inicial(self, interes_porcentual, valor_final, tiempo_deuda, intervalo_tiempo, tiempo_deuda_2, intervalo_tiempo_2):

        tiempo_deuda = self.tiempo_deuda(intervalo_tiempo, tiempo_deuda, tiempo_deuda_2, intervalo_tiempo_2)
        return valor_final / ((interes_porcentual / 100) * tiempo_deuda)

    def hallar_interes(self, valor_inicial_deuda, valor_final, tiempo_deuda, intervalo_tiempo, tiempo_deuda_2, intervalo_tiempo_2):

        tiempo_deuda = self.tiempo_deuda(intervalo_tiempo, tiempo_deuda, tiempo_deuda_2, intervalo_tiempo_2)
        return ((valor_final / (valor_inicial_deuda * tiempo_deuda)) * 100 )
        

    def tiempo_deuda(self, intervalo_tiempo, tiempo_deuda_1, tiempo_deuda_2, intervalo_tiempo_2):

        if (tiempo_deuda_2 != 0):
            numero_interacciones = 2
        else:
            numero_interacciones = 1

        tiempo_final = 0
        for i in range(numero_interacciones): 
            if (intervalo_tiempo == "dias"):
                tiempo_final = (tiempo_deuda_1 / 365.25) + tiempo_final
            if (intervalo_tiempo == "meses"):
                tiempo_final = (tiempo_deuda_1 / 12) + tiempo_final
            if (intervalo_tiempo == "a\u00f1os"):
                tiempo_final = tiempo_deuda_1 + tiempo_final
            if (intervalo_tiempo == "trimestres"):
                tiempo_final = ((tiempo_deuda_1 * 3) / 12 ) + tiempo_final
            if (intervalo_tiempo == "semestres"):
                tiempo_final = ((tiempo_deuda_1 * 6) / 12) + tiempo_final
            if (intervalo_tiempo == "semanas"):
                tiempo_final = ((tiempo_deuda_1 * 7) / 365.25) + tiempo_final

            intervalo_tiempo = intervalo_tiempo_2
            tiempo_deuda_1 = tiempo_deuda_2
  
        return tiempo_final
    
    def convertir_dias_a_anios_meses_dias(self, dias):
    # Definimos las constantes para el número de días en un año y en un mes promedio
        DIAS_EN_ANIO = 365
        DIAS_EN_MES = 30  # Usaremos un mes promedio de 30 días
        
        # Calculamos el número de años
        anios = dias // DIAS_EN_ANIO
        
        # Calculamos el número de días restantes
        dias_restantes = dias % DIAS_EN_ANIO
        
        # Calculamos el número de meses
        meses = dias_restantes // DIAS_EN_MES
        
        # Calculamos el número de días restantes
        dias_restantes = dias_restantes % DIAS_EN_MES
        
        return anios, meses, dias_restantes
    
class InteresCompuesto:
    def hallar_monto_compuesto(self, capital, tasa_interes, frecuencia, tiempo_1, cronograma_1, tiempo_2, cronograma_2, tiempo_capitalizable):
        calculo_tiempo_interes = self.calculo_tiempo_interes(intervalo_tiempo = tiempo_capitalizable, tiempo_deuda_1= tasa_interes, intervalo_tiempo_2 = frecuencia)
        calculo_tiempo_deuda = self.tiempo_deuda(intervalo_tiempo = frecuencia, tiempo_deuda_1 = tiempo_1, tiempo_deuda_2 = tiempo_2, intervalo_tiempo_2 = cronograma_1, intervalo_tiempo_3 = cronograma_2)
        return capital * (((1 + calculo_tiempo_interes)**calculo_tiempo_deuda))
    
    def hallar_monto_compuesto_caso_2(self, capital, tasa_interes, frecuencia, tiempo_1, cronograma_1, tiempo_2, cronograma_2, tiempo_capitalizable):
        tiempo_interes = self.calculo_tiempo_interes(intervalo_tiempo = tiempo_capitalizable, tiempo_deuda_1= tasa_interes, intervalo_tiempo_2 = frecuencia)
        tiempo_deuda = self.tiempo_deuda(intervalo_tiempo = frecuencia, tiempo_deuda_1 = tiempo_1, tiempo_deuda_2 = tiempo_2, intervalo_tiempo_2 = cronograma_1, intervalo_tiempo_3 = cronograma_2)
        return capital * (1 + (tiempo_deuda * tiempo_interes))
    
    def hallar_tiempo(self, monto_compuesto, capital, tasa_interes, frecuencia):
        return (f"{(math.log(monto_compuesto) - math.log(capital)) / math.log(1 + (tasa_interes / 100))} {frecuencia}")
    
    def hallar_tasa_interes(self, capital, monto_compuesto, frecuencia, tiempo_1, cronograma_1, tiempo_2, cronograma_2):
        return ((monto_compuesto / capital) ** (1 / self.tiempo_deuda(intervalo_tiempo = frecuencia
                                                                , tiempo_deuda_1 = tiempo_1
                                                                , tiempo_deuda_2 = tiempo_2
                                                                , intervalo_tiempo_2 = cronograma_1
                                                                , intervalo_tiempo_3 = cronograma_2))) - 1

    def hallar_capital(self, tasa_interes, monto_compuesto, frecuencia, tiempo_1, cronograma_1, tiempo_2, cronograma_2):
        return monto_compuesto / (1 + (tasa_interes / 100)) ** self.tiempo_deuda(intervalo_tiempo = frecuencia
                                                                , tiempo_deuda_1 = tiempo_1
                                                                , tiempo_deuda_2 = tiempo_2
                                                                , intervalo_tiempo_2 = cronograma_1
                                                                , intervalo_tiempo_3 = cronograma_2)
    
    def tiempo_deuda(self, intervalo_tiempo, tiempo_deuda_1, tiempo_deuda_2, intervalo_tiempo_2, intervalo_tiempo_3):
        if (tiempo_deuda_2 != 0):
            numero_interacciones = 2
        else:
            numero_interacciones = 1

        tiempo_final = 0
        for i in range(numero_interacciones): 
            if (intervalo_tiempo == "meses"):
                tiempo_final = self.convercion_meses(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final
            if (intervalo_tiempo == "bimestres"):
                tiempo_final = self.convercion_bimestres(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final
            if (intervalo_tiempo == "a\u00f1os"):
                tiempo_final = self.convercion_anos(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final
            if (intervalo_tiempo == "trimestres"):
                tiempo_final = self.convercion_trimestres(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final
            if (intervalo_tiempo == "semestres"):
                tiempo_final = self.convercion_semestres(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final
            if (intervalo_tiempo == "dias"):
                tiempo_final = self.convercion_dias(tiempo_1 = tiempo_deuda_1, cronograma_1 = intervalo_tiempo_2) + tiempo_final

        
            

            intervalo_tiempo_2 = intervalo_tiempo_3
            tiempo_deuda_1 = tiempo_deuda_2
        print(tiempo_final)

        return tiempo_final
    
    def calculo_tiempo_interes (self, intervalo_tiempo, tiempo_deuda_1, intervalo_tiempo_2):
        tiempo_final = 0
        if (intervalo_tiempo == "meses"):
            tiempo_final = self.convercion_meses(tiempo_1 = (tiempo_deuda_1/100), cronograma_1 = intervalo_tiempo_2) 
        if (intervalo_tiempo == "bimestres"):
            tiempo_final = self.convercion_bimestres(tiempo_1 = (tiempo_deuda_1/100), cronograma_1 = intervalo_tiempo_2)
        if (intervalo_tiempo == "a\u00f1os"):
            tiempo_final = self.convercion_anos(tiempo_1 = (tiempo_deuda_1/100), cronograma_1 = intervalo_tiempo_2)
        if (intervalo_tiempo == "trimestres"):
            tiempo_final = self.convercion_trimestres(tiempo_1 = (tiempo_deuda_1/100), cronograma_1 = intervalo_tiempo_2) 
        if (intervalo_tiempo == "semestres"):
            tiempo_final = self.convercion_semestres(tiempo_1 = (tiempo_deuda_1/100), cronograma_1 = intervalo_tiempo_2)
 
        return tiempo_final
    
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
        if (cronograma_1 == "dias"):
            tiempo_1 = tiempo_1 / 30
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
    
    def convercion_dias(self, tiempo_1, cronograma_1):
        if (cronograma_1 == "meses"):
            tiempo_1 = tiempo_1 / 30
        if (cronograma_1 == "bimestres"):
            tiempo_1 = tiempo_1 / 60
        if (cronograma_1 == "trimestres"):
            tiempo_1 = tiempo_1 / 90
        if (cronograma_1 == "semestres"):
            tiempo_1 = tiempo_1 / 180
        if (cronograma_1 == "a\u00f1os"):
            tiempo_1 = tiempo_1 / 365
        return tiempo_1
    
    def convertir_dias_a_anios_meses_dias(self, dias):
    # Definimos las constantes para el número de días en un año y en un mes promedio
        DIAS_EN_ANIO = 365
        DIAS_EN_MES = 30  # Usaremos un mes promedio de 30 días
        
        # Calculamos el número de años
        anios = dias // DIAS_EN_ANIO
        
        # Calculamos el número de días restantes
        dias_restantes = dias % DIAS_EN_ANIO
        
        # Calculamos el número de meses
        meses = dias_restantes // DIAS_EN_MES
        
        # Calculamos el número de días restantes
        dias_restantes = dias_restantes % DIAS_EN_MES
        
        return anios, meses, dias_restantes
    
    
# clase de la calculadora tir 
    
class CalculadoraTIRVAN:
    def __init__(self, flujos_de_efectivo, taza_interes):
        self.flujos_de_efectivo = flujos_de_efectivo
        self.taza_interes = taza_interes
       
       #calcula el tir del problema 
    def calcular_tir(self):
        from scipy.optimize import newton

        def f(tir):
            return sum([cf / (1 + tir) ** t for t, cf in enumerate(self.flujos_de_efectivo)])

        try:
            tir = newton(f, 0.1)
            return tir
        except RuntimeError:
            return None
      
    #calcula el valor de un año en especifico
    
    def calcular_van_verdadero(self):
        self.van_por_year = []
        i = 0
        self.resultado_van = 0
        for item in self.flujos_de_efectivo:
            if(item < 0):
                self.inversion_incial = item

            if(item > 0 and i == 1):
                self.resultado_van = self.inversion_incial + item/(1+(self.taza_interes/100))
                self.van_por_year.append(self.resultado_van) 

              
            if(i > 1):
                self.resultado_van = self.resultado_van + item/((1+(self.taza_interes/100))**i) 
                self.van_por_year.append(self.resultado_van)              
            
            i = i + 1
        return self.resultado_van, self.van_por_year
            
    
        


class GradienteAritmetico:
    def hayar_anualidad_valor_presente(self, taza_interes, tiempo, primera_cuota, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return primera_cuota*(((1+(taza_interes/100))**tiempo-1)/((taza_interes/100)*(1+(taza_interes/100))**tiempo))
    
    def hayar_gradiente_valor_presente(self, taza_interes, tiempo, aumento, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (aumento/(taza_interes/100))*(((1+(taza_interes/100))**tiempo-1)/((taza_interes/100)*(1+(taza_interes/100))**tiempo)-(tiempo/(1+(taza_interes/100))**tiempo))
    
    def hayar_anualidad_valor_futuro(self, taza_interes, tiempo, primera_cuota, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return primera_cuota*(((1+(taza_interes/100))**tiempo-1)/(taza_interes/100))

    def hayar_gradiente_valor_futuro(self, taza_interes, tiempo, aumento, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (aumento/(taza_interes/100))*((((1+(taza_interes/100))**tiempo-1)/(taza_interes/100))-tiempo)
    
    def hayar_anualidad_presente_valor_infinito(self, primera_cuota, taza_interes, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (primera_cuota/(taza_interes/100))
    
    def hayar_gradiente_presente_valor_infinito(self, taza_interes, aumento, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (aumento/(taza_interes/100)**2)
    
    def tiempo_deuda(self, intervalo_tiempo, tiempo_deuda_1):
        tiempo_final = 0
        
        if (intervalo_tiempo == "dias"):
            tiempo_final = (tiempo_deuda_1 / 365.25) + tiempo_final
        if (intervalo_tiempo == "meses"):
            tiempo_final = (tiempo_deuda_1 / 12) + tiempo_final
        if (intervalo_tiempo == "a\u00f1os"):
            tiempo_final = tiempo_deuda_1 + tiempo_final
        if (intervalo_tiempo == "trimestres"):
            tiempo_final = ((tiempo_deuda_1 * 3) / 12 ) + tiempo_final
        if (intervalo_tiempo == "semestres"):
            tiempo_final = ((tiempo_deuda_1 * 6) / 12) + tiempo_final
        if (intervalo_tiempo == "semanas"):
            tiempo_final = ((tiempo_deuda_1 * 7) / 365.25) + tiempo_final

        return tiempo_final


class GradienteGeometrico:
    def hayar_gradiente_valor_presente_cuando_i_diferente(self, taza_interes, tiempo, primera_cuota, aumento, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (primera_cuota/((aumento/100)-(taza_interes/100)))+((((1+(aumento/100))**tiempo)/((1+(taza_interes/100))**tiempo))-1)
    
    def hayar_gradiente_valor_presente_cuando_i_igual(self, taza_interes, tiempo, primera_cuota, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (tiempo*primera_cuota)/(1+(taza_interes/100))
    
    def hayar_gradiente_valor_futuro_cuando_i_diferente(self, taza_interes, tiempo, primera_cuota, aumento, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return (primera_cuota/((aumento/100)-(taza_interes/100)))+(((1+(aumento/100))**tiempo)-((1+(taza_interes/100))**tiempo))
    
    def hayar_gradiente_valor_futuro_cuando_i_igual(self, taza_interes, tiempo, primera_cuota, intervalo_tiempo):
        taza_interes = self.tiempo_deuda(intervalo_tiempo = intervalo_tiempo, tiempo_deuda_1 = taza_interes)
        return primera_cuota/(1+(taza_interes/100))**-1*(tiempo+1)
    
    def tiempo_deuda(self, intervalo_tiempo, tiempo_deuda_1):
        tiempo_final = 0
        
        if (intervalo_tiempo == "dias"):
            tiempo_final = (tiempo_deuda_1 / 365.25) + tiempo_final
        if (intervalo_tiempo == "meses"):
            tiempo_final = (tiempo_deuda_1 / 12) + tiempo_final
        if (intervalo_tiempo == "a\u00f1os"):
            tiempo_final = tiempo_deuda_1 + tiempo_final
        if (intervalo_tiempo == "trimestres"):
            tiempo_final = ((tiempo_deuda_1 * 3) / 12 ) + tiempo_final
        if (intervalo_tiempo == "semestres"):
            tiempo_final = ((tiempo_deuda_1 * 6) / 12) + tiempo_final
        if (intervalo_tiempo == "semanas"):
            tiempo_final = ((tiempo_deuda_1 * 7) / 365.25) + tiempo_final

        return tiempo_final
    



        

