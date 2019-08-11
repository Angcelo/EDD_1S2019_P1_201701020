import os

class NodoDoble:  
    def __init__(self, datox,datoy,indice):
        self.x = datox
        self.y= datoy
        self.indice=indice+1
        self.siguiente = None
        self.anterior = None

class ListaDoble:
	"""docstring for ClassName"""
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.indice=-1

	def get_indice(self):
		return self.indice

	def estaVacia(self):
		return self.primero==None

	def insertar_final(self,valorx,valory):
		nuevo=NodoDoble(valorx,valory,self.indice)
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
		nuevo=NodoDoble(valorx,valory,self.indice)
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

	def editar_ultimo(self,datox,datoy):
		self.ultimo.x=datox
		self.ultimo.y=datoy

	def cambiar_posicion(self):
		aux=self.primero
		while(aux.siguiente!=None) :
			aux.x=aux.siguiente.x
			aux.y=aux.siguiente.y
			aux=aux.siguiente
			pass

	def obtener_pos(self,index,dato):
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
		if(dato==1):
			return int(aux.x)
		elif(dato==2):
			return int(aux.y)

	def eliminar(self,index):
		if (index<0 or index>self.indice or self.indice<=2):
			return 
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
		f=open("serpiente.dot","w")
		f.write("digraph listadobleenlzada{\n")
		f.write("rankdir=\"LR\";\n")
		f.write("node [shape=\"record\"];\n")
		aux=self.primero
		while aux!=None:
			f.write(str(aux.x)+str(aux.y)+str(aux.indice)+" [ label = \"{|("+str(aux.x)+","+str(aux.y)+")|\\l}\"];\n")
			aux=aux.siguiente
			pass
		aux=self.primero
		while aux!=None:
			if(aux.anterior is not None):
				f.write(str(aux.x)+str(aux.y)+str(aux.indice) +"->"+ str(aux.anterior.x)+str(aux.anterior.y)+str(aux.anterior.indice)+"\n")
			elif(aux.anterior is None):
				f.write(str(aux.x)+str(aux.y)+str(aux.indice)+"  -> \"(Null_I)\";\n")
				pass
			if(aux.siguiente is not None):
				f.write(str(aux.x)+str(aux.y)+str(aux.indice) + "->" +str(aux.siguiente.x)+str(aux.siguiente.y)+str(aux.siguiente.indice)+"\n")
			elif(aux.siguiente is None):
				f.write(str(aux.x)+str(aux.y)+str(aux.indice)+"  -> \"(Null_D)\";\n")
				pass
			aux=aux.siguiente	
			pass
		f.write("}")
		f.close()
		os.system("dot -Tjpg serpiente.dot -o imagenserpiente.jpg")
		pass

	def mostrar(self):
		aux=self.primero
		while aux!=None:
			print(str(aux.x)+"-"+str(aux.y))
			aux=aux.siguiente
			pass	