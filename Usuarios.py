import os

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

	def obtener_iteracion(self,iteracion):
		contar=0
		if self.estaVacia()==False:
			aux=self.primero	
			while(contar<=iteracion):
				aux=aux.siguiente
				contar+=1
				pass
			while (contar>=iteracion):
				aux=aux.anterior
				contar-=1
				pass
			return aux.nombre
			pass
		return ""

	def mostrar(self):
		contar=0
		if self.estaVacia()==False:
			aux=self.primero
			while(contar<=self.tamaño):
				print(aux.nombre)
				aux=aux.siguiente
				contar+=1
			pass
		return ""

	def graficar(self):
		f=open("usuarios.dot","w")
		f.write("digraph listacirulardoble{\n")
		f.write("rankdir=\"LR\";\n")
		f.write("ratio=0.3")
		f.write("node [shape=\"record\"];\n")
		aux=self.primero
		contar=0
		while contar<=self.tamaño:
			f.write(aux.nombre+" [ label = \"{|("+aux.nombre+")|\\l}\"];\n")
			aux=aux.siguiente
			contar+=1
			pass
		aux=self.primero
		contar=0
		while(contar<=self.tamaño):
			f.write(aux.nombre +"->"+ aux.anterior.nombre+"\n")
			print("iteracion :"+str(contar))
			f.write(aux.nombre + "->" +aux.siguiente.nombre+"\n")
			aux=aux.siguiente	
			contar+=1
			pass
		f.write("}")
		f.close()
		os.system("dot -Tjpg usuarios.dot -o imagenusuarios.jpg")
		pass
		
		
