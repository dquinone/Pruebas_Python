import random
 
class operaciones_algebraicas:
  __sumatoria_enteros = 0 
  __sumatoria_fraccion = 0
  __multiplicacion_enteros = 1 
  __multiplicacion_fraccion = 1
  __contador_exponente = 0
  __bandera = True
  
  def _matriz(self, n =3,m = 3):
    matriz = []
    for i in range(n):
      matriz.append([])
      for j in range(m):
        matriz[i].append(random.randint(-100, 100))
    return matriz
 
  def _ejecutar(self, x):
    if str(x).isnumeric():
        self.__sumatoria_enteros = self.__sumatoria_enteros + int(x)
        self.__multiplicacion_fraccion = self.__multiplicacion_enteros * self.__multiplicacion_fraccion * int(x)
    else:
        self.__contador_exponente = self.__contador_exponente + 1
        if x.index('x') == 0:
            self.__sumatoria_fraccion = self.__sumatoria_fraccion + 1
            self.__multiplicacion_fraccion = self.__multiplicacion_fraccion * self.__multiplicacion_enteros * 1
        else:
          self.__sumatoria_fraccion = self.__sumatoria_fraccion + int(x[:x.index('x')])
          self.__multiplicacion_fraccion = self.__multiplicacion_fraccion * self.__multiplicacion_enteros * int(x[:x.index('x')])
 
  def operaciones_polinomios(self, *argv):
    self.__sumatoria_enteros = 0 
    self.__sumatoria_fraccion = 0
    self.__multiplicacion_enteros = 1 
    self.__multiplicacion_fraccion = 1
    self.__contador_exponente = 0
    valor = 0
    if len(argv) == 1:
      for index in argv:
        print('Ingrese un polinomio Valido' , str(index))
    else:
        for argumento in argv:
            self._ejecutar(argumento)
 
        var1 = str('' if self.__sumatoria_enteros == 0 else self.__sumatoria_enteros)
        var2 = '' if self.__sumatoria_enteros == 0 else '+'
        var3 = str('' if self.__sumatoria_fraccion <= 1 else self.__sumatoria_fraccion) + 'x'
        print('Suma y Resta de Polinomios: \n'+ var1 + var2 + var3 )
      
        var4 = self.__multiplicacion_fraccion #if self.__multiplicacion_enteros == 1 else self.__multiplicacion_enteros)
        var5 = ('x' if var4 <= 1 else str(var4) + 'x') + str('' if self.__contador_exponente <= 1 else '**' + str(self.__contador_exponente))
        print('Multiplicacion de Polinomios: \n' + var5)
        
 
        x = int(input("Ingrese el valor de x para validar la exprsion: "))
 
        ecuasion = var1 + var2 + var3, var5
 
        polinomio = []
        print(eval(ecuasion[0].replace('x', '*' + str(x))))
        polinomio.insert(0 , '(')
        polinomio.insert(1, ecuasion[1].replace('x','*' + str(x) + ')'))
        print(eval(polinomio[0] + polinomio[1]))
        print(valor)
  
  def mul_escalar(self, n, m, k):
    matriz = self._matriz(n, m)
    
    print('Matriz Inicial')
    for index in matriz:
      print(index)
    
    for i in range(n):
      for j in range(m):
        matriz[i][j] =  matriz[i][j] * k
    print("\nConstate k = " + str(k))
        
    print('\nMatriz x Escalar ')
    for index in matriz:
      print(index)
   
  
a = operaciones_algebraicas()
 
a.operaciones_polinomios('-2x', 4,'-2x',2, '2x')
a.mul_escalar(3,5,4)