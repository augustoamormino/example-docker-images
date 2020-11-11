from datetime import datetime
import time


date = datetime.now()

print('Ola, este é um JOB de exemplo em Python, agora são ', date)
print('O JOB será encerrado daqui 60 segundos')

time.sleep( 60 )

print('Finalizando a Job')

