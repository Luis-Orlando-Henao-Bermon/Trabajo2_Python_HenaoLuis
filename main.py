import json
from os import system
from datetime import datetime

with open ("./Medicamentos.json", encoding="UTF-8") as file:
    medicamentos=json.load(file)
with open ("./Compras.json", encoding="UTF-8") as file:
    compras=json.load(file)
with open ("./Empleados.json", encoding="UTF-8") as file:
    empleados=json.load(file)
with open ("./Pacientes.json", encoding="UTF-8") as file:
    pacientes=json.load(file)
with open ("./Proveedores.json", encoding="UTF-8") as file:
    proveedores=json.load(file)
with open ("./Ventas.json", encoding="UTF-8") as file:
    ventas=json.load(file)

xd=datetime.now()

hola=xd.strptime('2020-4-15 20:50:30', '%Y-%m-%d %H:%M:%S')
print(hola)



jsonMedicamentos=json.dumps(medicamentos)
with open("./Medicamentos.json","w") as file:
    file.write(jsonMedicamentos)
jsonCompras=json.dumps(compras)
with open("./Compras.json","w") as file:
    file.write(jsonCompras)
jsonEmpleados=json.dumps(empleados)
with open("./Empleados.json","w") as file:
    file.write(jsonEmpleados)
jsonPacientes=json.dumps(pacientes)
with open("./Pacientes.json","w") as file:
    file.write(jsonPacientes)
jsonProveedores=json.dumps(proveedores)
with open("./Proveedores.json","w") as file:
    file.write(jsonProveedores)
jsonVentas=json.dumps(ventas)
with open("./Ventas.json","w") as file:
    file.write(jsonVentas)
