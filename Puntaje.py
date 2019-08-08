class Nodo:
	def __init__(self, valor, user):
		self.valor=valor
		self.user=user
		self.siguiente=None

class lista:
	def __init__(self):
		self.tamaño=0
		self.primero=None

	def esVacia(self):
		return  self.primero==None

	def get_tam(self):
		return self.tamaño

	def desencolar(self):
		aux=self.primero
		if self.esVacia()==False:
			temp=self.primero.valor
			self.primero=self.primero.siguiente
			return temp
			pass

	def encolar(self,valor,user):
		nuevo=Nodo(valor,user)
		if self.esVacia():
			self.primero=nuevo
		else:
			aux=self.primero
			while aux.siguiente!=None:
				aux=aux.siguiente
				pass
			aux.siguiente=nuevo
			pass
		self.tamaño += 1
		if self.tamaño>10:
			self.desencolar()
			pass
		pass
		
	def mostrar_pos(self,index,tipo):
		aux=self.primero
		if self.esVacia()==False:
			contar=0
			while(contar<=index):
				aux=aux.siguiente
				contar+=1
				pass
			if tipo==1:	
				return str(aux.valor)
			else:
				return (aux.user)
			pass
		return " "

	def mostrar(self):
		aux=self.primero
		while aux!=None:
			print(aux.valor)
			aux=aux.siguiente
			pass
