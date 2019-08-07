class NodoDoble:  
    def __init__(self, nombre):
        self.nombre=nombre
        self.siguiente = None
        self.anterior = None

class usuarios:

	def __init__(self):
		self.primero=None
		self.tamaño=-1

	def estaVacia(self):
		return self.primero==None

	def get_tam(self):
		return self.tamaño

	def insertar(self,nombre):
		nuevo=NodoDoble(nombre)
		self.tamaño = self.tamaño+1
		if (self.estaVacia()):
			self.primero=nuevo
			self.primero.siguiente=self.primero
			self.primero.anterior=self.primero
		else:
			nuevo.siguiente=self.primero
			nuevo.anterior=self.primero.anterior
			self.primero.anterior.siguiente=nuevo
			self.primero.anterior=nuevo
			self.primero=nuevo

	def obtener_pos(self,nombre):
		aux=self.primero
		if self.estaVacia()==False:
			while(aux.nombre!=nombre):
				aux=aux.siguiente
				contar+=1
				pass
			return aux.nombre
			pass
		return ""

	def obtener_iteracion(self,iteracion):
		contar=0
		if self.estaVacia()==False:
			aux=self.primero	
			while(contar<=iteracion):
				aux=aux.siguiente
				contar+=1
				pass
			return aux.nombre
			pass
		return ""
		
		
