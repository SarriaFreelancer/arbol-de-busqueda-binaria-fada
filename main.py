#####===============================================================================
#####==============PROYECTO FINAL FUNDAMENTOS DE ANÁLISIS Y DESARROLLO DE ALGORITMOS
# AUTOR: JUAN DAVID CUERO SARRIA


import random       # Importamos la funcion Randon para generar numeros aleatorios

def principal():

    opcion = True
    while opcion:
        opc = int(input('''
                        *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
                        *=*=*=* =*=*=*=* Menú De Operaciones En Arbol Binario *=*=*=*=*=*=*=*=*
                        *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
                        *=*=*=*=*=                                                  *=*=*=*=*=*
                        *=*=*=*=*= Elija la operacion que desee realizar:           *=*=*=*=*=*
                        *=*=*=*=*=                                                  *=*=*=*=*=*
                        *=*=*=*=*= 1._  Generar Numeros e Insertar en TXT           *=*=*=*=*=*
                        *=*=*=*=*= 2._  Crear Árbol y cargar numeros                *=*=*=*=*=*
                        *=*=*=*=*= 3._  Calcular la Áltura del Arbol                *=*=*=*=*=*
                        *=*=*=*=*= 4._  Realizar Recorrido de elementos en el Árbol *=*=*=*=*=*
                        *=*=*=*=*= 5._  Buscar un dato en el Árbol                  *=*=*=*=*=*
                        *=*=*=*=*= 6._  Mostrar Clave Minima                        *=*=*=*=*=*
                        *=*=*=*=*= 7._  Mostrar Clave Maxima                        *=*=*=*=*=*
                        *=*=*=*=*= 8._  Borrar Un dato del ArbolBinario             *=*=*=*=*=*
                        *=*=*=*=*= 9._  Ingresar Un nuevo dato al Árbol             *=*=*=*=*=*
                        *=*=*=*=*= 10._ Mostrar el Predecesor de un dato            *=*=*=*=*=*
                        *=*=*=*=*= 11._ Mostrar el Sucesor de un dato               *=*=*=*=*=*
                        *=*=*=*=*= 12._ Salir                                       *=*=*=*=*=*
                        *=*=*=*=*=*                                                 *=*=*=*=*=*
                        *=*=*=*=*=* Ingrese la opcion: '''))
        
        if opc == 1:
            generarNumerosAle()  # Genera y guarda los numeros en el txt
        elif opc == 2:
            print(insertarValores())   #Obtiene lista de datos e inserta al Árbol
        elif opc == 3:
            print(imprimirAltura())
        elif opc == 4:
            print(recorridoArbol())
        elif opc == 5:
            print(buscarDato())
        elif opc == 6:
            print(claveMinima())
        elif opc == 7:
            print(claveMaxima())
        elif opc == 8:
            print(borrarValores())
        elif opc == 9:
            print(insertarValoresManual())
        elif opc == 10:
            mostraPredecesor()
        elif opc == 11:
            mostrarSucesor()
        elif opc == 12:
            opcion = False
        else:
            print('Opcion errada no se encuentra en el rango de operaciones')
            print('Por favor ingrese una opcion válida')

def recorridoArbol():

    opcion2 = True
    while opcion2:
        opc2 = int(input('''
                        *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
                        *=*=*=* =*=*=*= Menún Para Realizar Recorrido en Árbol =*=*=*=*=*=*=*=*
                        *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
                        *=*=*=*=*=                                                  *=*=*=*=*=*
                        *=*=*=*=*=      Elija el recorrido a realizar:              *=*=*=*=*=*
                        *=*=*=*=*=                                                  *=*=*=*=*=*
                        *=*=*=*=*= 1._  Recorrido en Inorden                        *=*=*=*=*=*
                        *=*=*=*=*= 2._  Recorrido en Preorden                       *=*=*=*=*=*
                        *=*=*=*=*= 3._  Recorrido en Postorden                      *=*=*=*=*=*
                        *=*=*=*=*= 4._  Regresar al menu Principal.                 *=*=*=*=*=*
                        *=*=*=*=*=*                                                 *=*=*=*=*=*
                        *=*=*=*=*=* Ingrese la opcion: '''))
        
        if opc2 == 1:
            t.inorden()  # Genera y guarda los numeros en el txt
        elif opc2 == 2:
            t.preorden()   #
        elif opc2 == 3:
            t.postorden()
        elif opc2 == 4:
            opcion2 = False
        else:
            print('Opcion Errada, no está en el rango, digite un valor correcto')



# Declaramos la clase 'Nodo'
class Nodo:

    def __init__(self, clave, padre=None, hijoIzq=None, hijoDer=None):
        self.clave = clave
        self.padre = padre
        self.hijoIzq = hijoIzq
        self.hijoDer = hijoDer
       

    # Métodos para asignar nodos

    # Obtener Clave
    def getClave(self):
        return self.clave
    # Asignar Clave
    def setClave(self, clave):
        self.clave = clave
    # Obtener Hijo Izquierdo
    def getHijoIzq(self):
        return self.hijoIzq
    # Asignar Hijo Izquierdo
    def setHijoIzq(self, hijoIzq):
        self.hijoIzq = hijoIzq
    # Obtener Hijo Derecho
    def getHijoDer(self):
        return self.hijoDer
    # Asignar Hijo derecho
    def setHijoDer(self, hijoDer):
        self.hijoDer = hijoDer
    # Obtener Nodo Padre
    def getPadre(self):
        return self.padre
    #Asignar Padre
    def setPadre(self, padre):
        self.padre = padre


#Creamos el arbol de Busqueda Binaria
class BinarySearchTree:

    #Funciones Privadas
    # Metodo Init para inicializar la Raiz del Arbol
    def __init__(self, raiz = None):
        self.raiz = raiz

    # Funcion para insertar un nuevo dato
    # Le pasamos el dato como clave
    def insert(self, clave):
        nuevo_Nodo = Nodo(clave, None) # Creamos un nuevo nodo con la clave dada

        if self.empty():               # Si el árbol esta vacio
            self.raiz = nuevo_Nodo     # La raiz sera igual al nuevo nodo con su clave.
        else:                          # Si el árbol no esta vacio
            nodo_Actual = self.raiz    #Crear nodoActual para asiganarle la Raiz
            while nodo_Actual is not None:  # Mientras Nodo_Actual no sea vacío
                padre_nodo = nodo_Actual    # Crear padre asignando el nodo actual que seria la raiz cada vez que se asigne un valor
                if nuevo_Nodo.getClave() < nodo_Actual.getClave(): # Si el valor del nuevo nodo es meno al nodo Actual Raiz
                    nodo_Actual = nodo_Actual.getHijoIzq() 
                else:
                    nodo_Actual = nodo_Actual.getHijoDer()
            if nuevo_Nodo.getClave() < padre_nodo.getClave():
                padre_nodo.setHijoIzq(nuevo_Nodo)
            else:
                padre_nodo.setHijoDer(nuevo_Nodo)
            nuevo_Nodo.setPadre(padre_nodo)    
    #Organizar Arbol

    #Funciones de Recorrido

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.hijoIzq)
            print(nodo.clave, end=", ")
            self.__inorden_recursivo(nodo.hijoDer)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.clave, end=", ")
            self.__preorden_recursivo(nodo.hijoIzq)
            self.__preorden_recursivo(nodo.hijoDer)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.hijoIzq)
            self.__postorden_recursivo(nodo.hijoDer)
            print(nodo.clave, end=", ")

    #Funcion para buscar un clave
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.raiz == busqueda:
            return nodo
        if busqueda < nodo.raiz:
            return self.__buscar(nodo.hijoIzq, busqueda)
        else:
            return self.__buscar(nodo.hijoDer, busqueda)

    # Funciones públicas

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscarN(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    # Función de borrado de un arbol
    def borrar(self, clave):        # Ingresamos el valor a eliminar
        if (not self.empty()):      # Si no es vacío
            nodo = self.getNodo(clave)
            if(nodo is not None):
                if(nodo.getHijoIzq() is None and nodo.getHijoDer() is None):
                    self.__reasignNodos(nodo, None)
                    nodo = None
                elif(nodo.getHijoIzq() is None and nodo.getHijoDer() is not None):
                    self.__reasignNodos(nodo, nodo.getHijoDer())
                elif(nodo.getHijoIzq() is not None and nodo.getHijoDer() is None):
                    self.__reasignNodos(nodo, nodo.getHijoIzq())
                else:
                    tmpNodo = self.getMax(nodo.getHijoIzq())
                    self.borrar(tmpNodo.getClave())
                    nodo.setClave(tmpNodo.getClave())
    # Obtener  Nodo 
    def getNodo(self, clave):
        nodo_Actual = None
        if(not self.empty()):
            nodo_Actual = self.getRaiz()
            while nodo_Actual is not None and nodo_Actual.getClave() is not clave:
                if clave < nodo_Actual.getClave():
                    nodo_Actual = nodo_Actual.getHijoIzq()
                else:
                    nodo_Actual = nodo_Actual.getHijoDer()
        return nodo_Actual
 #---------------------------------------------CLAVES MÁXIMAS Y MÍNIMAS----------------------------------------------------   
    #Funcion para hayar la clave maxima
    def getMax(self, raiz = None):
        if(raiz is not None):  # Si la raiz no es None se le asiga que esta enel nodo actual
            nodo_Actual = raiz
        else:
            nodo_Actual = self.getRaiz()    # En caso contrario se obtiene la Raiz que hay en el arbol
        if(not self.empty()):               # si no es vacío
            while(nodo_Actual.getHijoDer() is not None):   # Mientras el hijo derecho del nodo actual no sea None
                nodo_Actual = nodo_Actual.getHijoDer()     # Se lo asigna al nodo Actual
        return nodo_Actual

    #Funcion para hayar la clave minima
    def getMin(self, raiz = None):    # Con esta funcion pasa lo mismo que con la anterior solo con el hijo Izquierdo
        if(raiz is not None):
            nodo_Actual = raiz
        else:
            nodo_Actual = self.getRaiz()
        if(not self.empty()):
            nodo_Actual = self.getRaiz()
            while(nodo_Actual.getHijoIzq() is not None):
                nodo_Actual = nodo_Actual.getHijoIzq()
        return nodo_Actual

    def empty(self):
        if self.raiz is None:
            return True
        return False
#-------------------------------------------Recorrido de Arbol en Inorden-------------------------------------
    def __InOrderTraversal(self, nodo_Actual):
        listaNodo = []
        if nodo_Actual is not None:
            listaNodo.insert(0, nodo_Actual)
            listaNodo = listaNodo + self.__InOrderTraversal(nodo_Actual.getHijoIzq())
            listaNodo = listaNodo + self.__InOrderTraversal(nodo_Actual.getHijoDer())
        return listaNodo

    # Devuelve la Raiz
    def getRaiz(self):
        return self.raiz
#---------------------------------REASIGNACION DE NODOS DESPUES DE BORRADOS---------------------------------------
    #Funcion para encontrar hijo derecho 
    # Funcion que se usara para luego reabsignar nodos cuando se borra un padre
    def __ishijoDerChildren(self, nodo):
        if(nodo == nodo.getPadre().getHijoDer()):
            return True
        return False

    #Funcion para reasignar nodos despues de eliminar
    def __reasignNodos(self, nodo, nuevoHijo):
        if(nuevoHijo is not None):
            nuevoHijo.setPadre(nodo.getPadre())
        if(nodo.getPadre() is not None):
            if(self.__ishijoDerChildren(nodo)):  # Busca el hijo derecho para asignar nodos si existe
                nodo.getPadre().setHijoDer(nuevoHijo)   # Si existe asigana hijo derecho
            else:
                nodo.getPadre().setHijoIzq(nuevoHijo)   # Si no ya hay hijo derecho le asigana uno izquierdo
#-----------------------------------RECORRIDO Y MUESTRA DE ARBOL EN INORDEN EN PANTALLA-------------------------------------
    #Funcion  para recorrer y obtener los valores ordenados del arbol
    #en inorden Tranversal
    def __str__(self):
        list = self.__InOrderTraversal(self.raiz)
        str = ''
        for x in list:
            str = str + ' ' + x.getClave().__str__()
        return str

#----------------------------CAMPO DE ALGUNAS MUESTRAS Y CREACION DE FUNCIONES PUBLICAS---------------------------------

# Instancia del árbol binario de búsqueda
# Creamos un objeto de la clase ARBOL BINARIO DE BUSQUEDA
t = BinarySearchTree()


#----------------------------------------------GENERANDO NUMEROS ALEATORIOS-----------------------------------------------
#OPERACION #1
#Funcion Para Generar 100000 Numeros Aleatorios diferentes
#Misma  Funcion Para agregarlos al txt
def generarNumerosAle():
    nuGenerar = int(input('Por favor Digite la cantidad de numeros a generar: '))
    mitad = int(nuGenerar/2)    #dividimo
    #por ejemplo si deseamos 15 numeros la mitad entera sera 7
    # Creamos una lista donde los almacenamos primero               # Por lo que sumamos 15+7 = 22 en tal caso genera 15 numeros aleatorios 
    aleatorios = random.sample(range(1,nuGenerar+mitad), nuGenerar) # entre 1 y 22 asi no se ira a un rango tan elevado
    try:
        archivo = open('numeros.txt','w')
        archivo.writelines("%s," % place for place in aleatorios)   # Los agregamos al txt separados por ,
        print(f' {len(aleatorios)} Numeros Generados e ingresados al TXT con éxito')
    except Exception as e:
        print(e)
    finally:
        archivo.close()
#OPERACION #2
# Funcion para devolver datos del txt en un una lista
def devolverDatos():
    with open("numeros.txt", "r") as ar:
        listaTxt = ar.read().split(",")     # Con la funcion read() leemos y separamos por , los datos
    lista = []                              # Lista Para almacenar cada valor del txt como string
    for valor in listaTxt:                  # Opteniendo El valor de cada posicion en la lista
        if valor != "":                     # Verificamos que no hayan valores vacíos a ingresar 
            lista.append(valor)             # Agregamos cada valor a la lista, los agrega como string

    nuevaList = [ int(x) for x in lista]   #Creamos una nueva lista convirtiendo los valores a enteros
    return nuevaList                   #Retornamos la nueva lista


#------------------------------------------INSERTANDO VALORES AL ARBOL-------------------------------------------------
#OPERACION #2
# Funcion para Insertar Valores al Arbol
def insertarValores():
    # Insertamos los elementos al arbol
    lista = devolverDatos()             # Llamamos a la funcion que retorna la lista del txt 
                                        # Le asignamos a la variable lista la nueva lista 
    for i in lista:
        t.insert(i)
    return t.__str__()   #Retorna los valores insertados


#Funcion para insertar un valor Manualmente
def insertarValoresManual():
    cantidad = int(input('Cuantos valores desea ingresar?: '))
    cont = 1
    while cont <= cantidad:# Solo se insertan la cantidad escrita 
        valor = int(input(f'Ingrese el valor {cont}: '))
        t.insert(valor)
        cont += 1
    return t.__str__()   # REtorna los Valore insertados

#-----------------------REUTILIZACION DE ALGUNAS FUNCIONES PARA GENERAR MENOS COSTO EN EL LLAMADO---------------------------
# Funcion para retornar la clave Maximaria
def claveMaxima():
    if(not t.empty()):
        return f'La Clave Máxima Es: {t.getMax().getClave()}'
        
# Funcion para retornar la clave Minima
def claveMinima():
    if(not t.empty()):
        return f'La Clave Mínima Es: {t.getMin().getClave()}'

# Funcion para borrar un nodo especifico
def borrarValores():

    nuBorrar = int(input('cuantos datos desea eliminar: '))
    if nuBorrar <= 0:
        print('Valor ingresado es menor o igual a 0')
    #Poner si es mayor a la clave maxima
    #Si no existe
    else:
        cont = 1
        while cont <= nuBorrar:
            valor = int(input(f'Ingrese el numero {cont} a borrar: '))
            t.borrar(valor) # LLamamos a la funcion de borrado y le pasamos el valor 
            cont += 1
    return t.__str__()

#Funcion para buscar un dato en el arbol
def buscarDato():
    dato = int(input('Por favor ingrese el dato a buscar: '))
    if(t.getNodo(dato) is not None): # con getNodo devuelve un objeto del arbol si existe
        print(f'El elemento {dato} existe')
    else:
        print(f'El elemento {dato} no existe')
    return t.__str__()
#------------------------------------------ALTURA DEL ARBOL--------------------------------------------------------------------
#Funcion para calcular la altura del arbol
#se calcula pasando el nodo raiz i el nivel -1
def altura(nodo, nivel):
    if(nodo==None):
        return nivel
    else:
        return max(altura(nodo.hijoIzq, nivel + 1), altura(nodo.hijoDer, nivel + 1))
#Funcion Para imprimir la Altura
def imprimirAltura():
    return f'La Altura del Arbol es: {altura(t.raiz,-1)}'

#----------------------------------------------ENCONTRAR HIJOS------------------------------------------------------------------------
# funcion para encontrar hijoIzquierdo en el arbol
def encontrarHijoIzq(nodo):
    while (nodo != None and nodo.hijoIzq != None):  # Si el nodo no None y el nodo izquierdo no es Vacio
        nodo = nodo.hijoIzq                         # entonces se ha encontrado el nodo izquierdo
    return nodo
 
# funcion para encontrar hijoDerecho en el arbol
def encontrarHijoDer(nodo):
    while (nodo != None and nodo.hijoDer != None): # Si el nodo no None y el nodo Hizquierdo no es Vacio
        nodo = nodo.hijoDer                        # entonces se ha encontrado el nodo derecho
    return nodo
 
#------------------------------------------SUCESOR Y PREDECESOR---------------------------------------------------------------
# Funcion Recursiva para encontrar el Sucesor Inorden 
# Cuando el hijo del nodo es None recursivamente debe 
# Encontrar un predecesor
def encontrarSucesorR(raiz, x ):
 
    if (not raiz):
        return None
    if (raiz == x or (encontrarSucesorR(raiz.hijoIzq, x)) or
                     (encontrarSucesorR(raiz.hijoDer, x))):
        if encontrarSucesorR(raiz.hijoDer, x):
            temp=encontrarSucesorR(raiz.hijoDer, x)
        else:
            temp=encontrarSucesorR(raiz.hijoIzq, x)
        if (temp):
         
            if (raiz.hijoIzq == temp):
             
                print("El Sucesor en Inorden de", x.clave, end = "")
                print(" es", raiz.clave)
                return None   
        return raiz
# Cuando el hijo del nodo es None recursivamente debe encontrar un predecesor
def encontrarPrede(raiz, x ):
 
    if (not raiz):
        return None
    if (raiz == x or (encontrarPrede(raiz.hijoDer, x)) or
                     (encontrarPrede(raiz.hijoIzq, x))):
        if encontrarPrede(raiz.hijoIzq, x):
            temp=encontrarPrede(raiz.hijoIzq, x)
        else:
            temp=encontrarPrede(raiz.hijoDer, x)
        if (temp):
         
            if (raiz.hijoDer == temp):
             
                print("El Predecesor en inorden de ",x.clave, end = "")
                print(" es", raiz.clave)
                return None   
        return raiz
    return None
 
# funcion para encontrar el sucesor en inorden 
# de un nodo cuando si tiene hijos
def inorderSuccessor(raiz, x):
     
    if (x.hijoDer != None) :
        inorderSucc = encontrarHijoIzq(x.hijoDer)
        print("El sucesor en inorden de", x.clave, "es", end = " ")
        print(inorderSucc.clave)
         
    if (x.hijoDer == None):
        f = 0
        hijoDerMost = encontrarHijoDer(raiz)
 
        # caso3: Si x es el hijoDer mas nodo
        if (hijoDerMost == x):
            print("Sin sucesor en inorden!",x.clave, "sin nodo Derecho.")
        else:
            encontrarSucesorR(raiz, x)

#Funcion para encontrar el predecesor de un nodo
#Cuando el nodo si tiene hijos
def inorderPredecessor(raiz, x):
 
    if (x.hijoIzq != None) :
        inorderSucc = encontrarHijoDer(x.hijoIzq)
        print("Inorden Predecesor de", x.clave, "es", end = " ")
        print(inorderSucc.clave)

    if (x.hijoIzq == None):
        f = 0
        hijoIzqMost = encontrarHijoIzq(raiz)
 
        if (hijoIzqMost == x):
            print("Sin Predecesor en inorden!",x.clave, "sin nodo Izquierdo.")
        else:
            encontrarPrede(raiz, x)

#Funcion Para Mostrar el predecesor de un nodo
def mostraPredecesor():
    dato = int(input('Por favor ingrese el dato a buscar: '))
    if(t.getNodo(dato) is not None):
        print(f'El nodo {dato} existe')
        inorderPredecessor(t.raiz, t.getNodo(dato))
    else:
        print(f'El nodo {dato} no existe')

#Funcion Para Mostrar el sucesor de un nodo
def mostrarSucesor():
    dato = int(input('Por favor ingrese el dato a buscar: '))
    if(t.getNodo(dato) is not None):
        print(f'El nodo {dato} existe')
        inorderSuccessor(t.raiz, t.getNodo(dato))
    else:
        print(f'El nodo {dato} no existe')
    

# PRUEBAS ===========================================================
# Llamado A Funcion Principal
print('==================================')
if __name__ == '__main__':
    print(principal())
 


    
    
    
    
    

    
