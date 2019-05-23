
import cv2


path = '/home/docker/Jessi/ssd_keras/video-0040-o-4.MPG'
cap = cv2.VideoCapture(path)
# Almacenamos las dimensiones de los frames del video.
alto=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
ancho=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))

# Indicamos las caracteristicas de como se guardara el video
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I','D')

model_path = 'ssd7_400.h5'
# Recorremos todos los frames del video.
while(cap.isOpened()):
    ret,frame =cap.read()
    # Si el frame es correcto detectaremos el objeto de interes
    if ret == True:
        
	
        # Mostramos el video y lo guardamos.
        cv2.imshow('frame', frame)
        out.write(frame)
    else:
        break
    # Si se pulsa la q se sale del video.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
