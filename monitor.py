# llamado de libreria psutil y time 
import psutil
import time
#-----------------------------------------------
# Función de monitoreo objeto cpu
def uso_cpu():
    return psutil.cpu_percent(interval=1)
#----------------------------------------------
#Función de monitoreo objeto memoria
def uso_memoria():
    memory = psutil.virtual_memory()
    return memory.percent
#-----------------------------------------------
#Función de monitoreo objeto disco
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