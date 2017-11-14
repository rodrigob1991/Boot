

filas=input("ingrese numero de filas:")
columnas=input("ingrese numero de columnas:")

while columnas.isnumeric()== False or filas.isnumeric()==False:
	print("Ingrese solo numeros")
	filas=input("ingrese numero de filas:")
	columnas=input("ingrese numero de columnas:")

while int(columnas)<1  or int(filas)<1:
	print("Ingrese numeros mayores que 1")
	filas=input("ingrese numero de filas:")
	columnas=input("ingrese numero de columnas:")

filas=int(filas)
columnas=int(columnas)

num_obstaculos=int(input("ingrese numero de obstaculos:"))
posi_obstaculos=[]

while num_obstaculos >0:
        coordenada_fila=input("ingresar numero fila del obstaculo:")
        coordenada_col=input("ingresar numero columna del obstaculo:")
        posi_obstaculos.append((int(coordenada_fila),int(coordenada_col)))
        num_obstaculos-=1


def interactuar_objeto(x,y,orden,espacio,robot):
        
    guardar=input("¿Guardar objeto?\n")
    if guardar =="si":
            robot.guardar_objeto(espacio.mapa[x][y])
            print("robot tiene ahora una caja con un "+caja.contenido)
    return guardar

def ingresar_orden(limite,robot):

        if limite==True:
            print("\nNo podes pasar \n")

        lista_direccion=["s","n","e","o","se","so","ne","no"]

        if robot.almacenamiento==caja:
                orden=input("Ingresa direccion o soltar caja:")
                                
        else:
                orden=input("Ingrese direccion")
                while orden not in lista_direccion:
                        print("Direccion invalida")
                        orden=input("Ingrese direccion")
         
        
        return orden

def mov_automatico(x,y):

        import time

        direccion="e"
        if y == columnas-1 and x<filas-1:
                direccion="s"
        if x == filas-1 :
                direccion="o"
        if y == 0 and x>0:
                direccion="n"
        time.sleep(1)

        return direccion


class Robot(object):


        def __init__(self,id_robot):

                self.id_robot=id_robot
                self.almacenamiento=None



        def mover(self,espacio):
                
                x=0
                y=0
                espacio.mapa[x][y]=self
                espacio.formatear_imprimir(self,caja)
                espacio.mapa[x][y]=" "
                limite=False
                
                while True:

                        orden = ingresar_orden(limite,self)
                        if orden=="soltar":
                                self.soltar_objeto(self.almacenamiento,x,y,cuarto)
                                continue
                        
                        limite=False
                        
                        if orden=="s":

                                if filas==x+1 or espacio.mapa[x+1][y]==0:
                                        limite=True
                                        continue
                                x=x+1
                                        
                                        
                        elif orden=="n":

                                
                                if x==0 or espacio.mapa[x-1][y]==0:
                                        limite=True
                                        continue
                                x=x-1

                               
                        elif orden=="e":

                                
                                if y == columnas-1 or espacio.mapa[x][y+1]==0:
                                        limite=True
                                        continue
                                y=y+1


                        elif orden=="o":

                                
                                if y==0 or espacio.mapa[x][y-1]==0:
                                        limite=True
                                        continue
                                y=y-1


                        elif orden=="ne":

                                
                                if x==0 or y == columnas-1 or espacio.mapa[x-1][y+1]==0:
                                        limite=True
                                        continue
                                x=x-1
                                y=y+1


                        elif orden=="se":

                                if x==filas-1 or y==columnas-1 or espacio.mapa[x+1][y+1]==0:
                                        limite=True
                                        continue
                                x=x+1
                                y=y+1


                        elif orden=="so":
                               
                                if x==filas-1 or y==0 or espacio.mapa[x+1][y-1]==0:
                                        limite=True
                                        continue
                                x=x+1
                                y=y-1

                               

                        elif orden=="no":
                                
                                if x==0 or y==0 or espacio.mapa[x-1][y-1]==0:
                                        limite=True
                                        continue
                                x=x-1
                                y=y-1

                        if espacio.mapa[x][y]==caja:

                                if interactuar_objeto(x,y,orden,cuarto,self)!="si":
                                        continue                  
                                
                        espacio.mapa[x][y]=self
                        espacio.formatear_imprimir(self,caja)
                        espacio.mapa[x][y]=" "
                        
                        
                                        


        def guardar_objeto(self,objeto):

                self.almacenamiento=objeto

        def soltar_objeto(self,objeto,x,y,espacio):

                espacio.mapa[x][y]=objeto
                self.almacenamiento=None



class Espacio(object):


    def crearMapa(self,filas,columnas):

        mapa=[]
        for fila in range(filas):
            columna=[]
            for col in range(columnas):
                columna.append(" ")
            mapa.append(columna)
        self.mapa=mapa




    def espacio_obstaculos(self,posi_obstaculos):

        obstaculo=0
        for coordenada in posi_obstaculos:
            self.mapa[coordenada[0]][coordenada[1]]=obstaculo

    

    def formatear_imprimir(self,robot,caja):
        
        print("--"*columnas+"-")

        for fila in self.mapa:

            for cas in fila:

                if cas==caja:
                    print("|"+caja.id_caja,end="")
                    continue
                if cas==robot:
                    print("|"+robot.id_robot,end="")
                    continue
                print("|{}".format(cas),end="")
            print("|")  
            print("--"*columnas+"-")


class Caja(object):

        def __init__(self,contenido,peso,id_caja):

            self.contenido=contenido
            self.peso=peso
            self.id_caja=id_caja


cuarto=Espacio()
cuarto.crearMapa(filas,columnas)
cuarto.espacio_obstaculos(posi_obstaculos)
robot =Robot("R")
caja=Caja("monitor",4,"C")
cuarto.mapa[2][2]=caja
robot.mover(cuarto)
