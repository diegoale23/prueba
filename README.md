# Monitoreo del Sistema con psutil

Este proyecto contiene un script de Python que monitorea en tiempo real el uso de la CPU, memoria y disco en el sistema. Utiliza la librería `psutil` para obtener las estadísticas del sistema y la librería `time` para controlar los intervalos de monitoreo.

## Requisitos

Para ejecutar este código, necesitas tener instalada la librería `psutil`. Si aún no la tienes instalada, puedes hacerlo utilizando `pip`:

```bash
pip install psutil
Descripción del Código
Este script realiza las siguientes funciones:

Monitoreo del uso de la CPU: Obtiene el porcentaje de uso de la CPU durante 1 segundo.
Monitoreo del uso de la memoria: Obtiene el porcentaje de memoria utilizada en el sistema.
Monitoreo del uso del disco: Obtiene el porcentaje de uso del disco en la partición raíz (/).
El programa ejecuta un ciclo infinito donde se imprimen los valores de uso de CPU, memoria y disco, actualizados cada 4 segundos.

Código
python
Copiar
import psutil
import time

#-----------------------------------------------
# Función de monitoreo objeto cpu
def uso_cpu():
    return psutil.cpu_percent(interval=1)

#----------------------------------------------
# Función de monitoreo objeto memoria
def uso_memoria():
    memory = psutil.virtual_memory()
    return memory.percent

#-----------------------------------------------
# Función de monitoreo objeto disco
def uso_disco():
    disk = psutil.disk_usage('/')
    return disk.percent

#---------------------------------------------
def monitor_system():
    while True:
        cpu_usage = uso_cpu()
        memory_usage = uso_memoria()
        disk_usage = uso_disco()

        print(f"Uso de CPU: {cpu_usage}%")
        print(f"Uso de memoria: {memory_usage}%")
        print(f"Uso de disco: {disk_usage}%")
        print("-" * 30)
        time.sleep(4)

if __name__ == "__main__":
    monitor_system()
Ejecución
Clona o descarga el proyecto.
Instala las dependencias necesarias con el comando pip install psutil.
Ejecuta el script desde la terminal:
bash
Copiar
python monitor_system.py
El programa comenzará a mostrar el uso de la CPU, memoria y disco en tiempo real cada 4 segundos.

Notas
El script continuará ejecutándose de manera indefinida. Para detenerlo, puedes interrumpirlo con Ctrl + C.
Si prefieres modificar el intervalo de monitoreo, ajusta el valor dentro de time.sleep(4) en el script.
Asegúrate de tener permisos adecuados para acceder a las métricas del sistema.

Para más información sobre el proyecto, visita nuestro repositorio en [GitHub](https://github.com/diegoale23/prueba.git).
