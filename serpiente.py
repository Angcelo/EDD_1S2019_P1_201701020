import os

class NodoDoble:  
    def __init__(self, datox,datoy):
        self.x = datox
        self.y= datoy
        self.siguiente = None
        self.anterior = None

class ListaDoble:
	"""docstring for ClassName"""
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.indice=-1
		self.nograficos=0;

	def estaVacia(self):
		return self.primero==None

	def insertar_final(self,valorx,valory):
		nuevo=NodoDoble(valorx,valory)
		self.indice = self.indice+1
		if self.estaVacia():
			self.primero=nuevo
			self.ultimo=nuevo
			return "insertado al inicio"
		else:
			self.ultimo.siguiente=nuevo
			nuevo.anterior=self.ultimo
			self.ultimo=nuevo
			return "insertado en posicion" + str(self.indice)
			
	def insertar_inicio(self,valorx,valory):
		nuevo=NodoDoble(valorx,valory)
		self.indice = self.indice+1
		if (self.estaVacia()):
			self.primero=nuevo
			self.ultimo=nuevo
			return "insertado al inicio"
		else:
			self.primero.anterior=nuevo
			nuevo.siguiente=self.primero
			self.primero=nuevo
			return "insertado en posicion" + str(self.indice)
		

	def eliminar(self,index):
		if (index<0 or index>self.indice):
			return "No se econtro la posicion"
		else:
			aux=self.primero
			contar=0
			while(contar<index):
				aux=aux.siguiente
				contar+=1
				pass
			pass
		if index==0:
			self.primero=self.primero.siguiente
			self.primero.anterior=None
		else: 
			if index==self.indice:
				self.ultimo=self.ultimo.anterior
				self.ultimo.siguiente=None
			else:	
				aux.anterior.siguiente=aux.siguiente
				aux.siguiente.anterior=aux.anterior
				pass
		pass
		self.indice -= 1

	def graficar(self):
		f=open("nuevo"+str(self.nograficos)+".dot","w")
		f.write("digraph listadobleenlzada{\n")
		f.write("rankdir=\"LR\"")
		f.write("node [shape=\"square\"];\n")
		aux=self.primero
		while aux!=None:
			if(aux.anterior is not None):
				f.write("\""+str(aux.item)+"\"  -> \""+str(aux.anterior.item)+"\";\n")
				pass
			if(aux.siguiente is not None):
				f.write("\""+str(aux.item)+"\"  -> \""+str(aux.siguiente.item)+"\";\n")
				pass
			aux=aux.siguiente	
			pass
		f.write("}")
		f.close()
		os.system("dot -Tjpg nuevo"+str(self.nograficos)+".dot -o imagen"+str(self.nograficos)+".jpg")
		os.system("imagen"+str(self.nograficos)+".jpg")
		os.system("timeout 5")
		self.nograficos+=1
		pass
