class NodoDoble:  
    def __init__(self, nombre):
        self.nombre=nombre
        self.siguiente = None
        self.anterior = None

class usuarios:

	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.tamaño=-1

	def estaVacia(self):
		return self.primero==None

	def insertar_inicio(self,nombre):
		nuevo=NodoDoble(nombre)
		self.tamaño = self.tamaño+1
		if (self.estaVacia()):
			self.primero=nuevo
			self.ultimo=nuevo
			return "insertado al inicio"
		else:
			self.primero.anterior=nuevo
			nuevo.siguiente=self.primero
			self.primero=nuevo
			return "insertado en posicion" + str(self.tamaño)

	def obtener_pos(self,nombre):
		if (index<0 or index>self.indice):
			return "No se econtro la posicion"
		else:
			aux=self.primero
			contar=0
			while(uax.nombre!=nombre):
				aux=aux.siguiente
				contar+=1
				pass
			pass
		return aux.nombre
