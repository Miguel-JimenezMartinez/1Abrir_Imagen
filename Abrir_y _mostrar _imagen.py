import cv2                                #Importando OpenCv

imagen=cv2.imread('logopy.png')           #creando variable que almacenará la imagen, dentro del parentesis colocamos el mombre y extension de la imagen
                                          #En este caso se hace solo así ya que la imagen esta en la misma carpeta, si estuviera en otra carpeta se pone la ruta.
cv2.imshow('Hola soy una imagen', imagen) #con esta función mostramos la imagen, los parametros son: el nombre de la ventana y la variable donde esta la imagen.                                

cv2.waitKey(0)                            #Esta funcion mostrará la imagen cierto tiempo o en este caso hasta que digitemos algo en el teclado.

cv2.destroyAllWindows()                   #Cierra las ventanas creadas.
