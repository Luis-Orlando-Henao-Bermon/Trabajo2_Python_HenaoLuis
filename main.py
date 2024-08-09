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


bol=True
system("clear")
while bol==True:
    system("clear")
    opcion=int(input("==========Menu==========\n1. Registrar ventas\n2. Registrar compra\n3. Salir\nEscribe tu opcion\n"))
    system("clear")
    if opcion==1:
        fechaVenta=str(datetime.now())
        print("----------Pacientes----------")
        
        for i in pacientes:
            print("ID:",i["id"],"------ Nombre:",i["nombre"])
            print("------------------------------------------")
        
        idPacienteV=int(input("Ingresa el ID del paciente al que se le realizara la venta\n"))
        system("clear")
        for i in pacientes:
            if i["id"]==idPacienteV:
                pacienteV={"nombre":i["nombre"],"direccion":i["direccion"]}
        
        print("----------Empleados----------")
        for i in empleados:
            print("ID:",i["id"],"------ Nombre:",i["nombre"])
            print("------------------------------------------")
        
        idEmpleadoV=int(input("Ingresa el ID del empleado que realizara la venta\n"))
        for i in empleados:
            if i["id"]==idEmpleadoV:
                empleadoV={"nombre":i["nombre"],"cargo":i["cargo"]}
        
        system("clear")
        print("----------Medicamentos----------")
        for i in medicamentos:
            print("ID:",i["id"],"------ Nombre:",i["nombre"],"------ Precio:",i["precio"],"------ Cantidad en stock:",i["stock"])
            print("------------------------------------------")
        
        idMedicamentoV=int(input("Ingresa el ID del medicamento que se va a vender\n"))
        cantidadMedicamentoV=int(input("Ingresa la cantidad de de medicamento que se va a vender\n"))
        for i in medicamentos:
            if i["id"]==idMedicamentoV:
                medicamentoV={"nombreMedicamento":i["nombre"],"cantidadVendida":cantidadMedicamentoV,"precio":i["precio"]}
                i["stock"]=i["stock"]-cantidadMedicamentoV

        ventas.append({"fechaVenta":fechaVenta,"paciente":pacienteV,"empleado":empleadoV,"medicamentosVendidos":medicamentoV})
        system("clear")
        input("Venta realizada con exito 😀\nPreciona Enter para continuar")

    elif opcion==2:
        fechaCompra=str(datetime.now())
        print("----------Proveedores----------")
        for i in proveedores:
            print("ID:",i["id"],"-------- Nombre:",i["nombre"])

        idProveedor=int(input("Ingresa el id del proveedor al que se le realizara la compra\n"))

        for i in proveedores:
            if i["id"]==idProveedor:
                proveedor={"nombre":i["nombre"],"contacto":i["contacto"]}

        system("clear")
        print("----------Medicamentos----------")
        for i in medicamentos:
            print("ID:",i["id"],"------ Nombre:",i["nombre"],"------ Precio:",i["precio"],"------ Cantidad en stock:",i["stock"])
            print("------------------------------------------")
        
        idMedicamentoC=int(input("Ingresa el ID del medicamento que se va a comprar\n"))
        cantidadMedicamentoC=int(input("Ingresa la cantidad de de medicamento que se va a comprar\n"))
        precioCompra=int(input("Ingrese el precio de compra del medicamento\n"))
        for i in medicamentos:
            if i["id"]==idMedicamentoC:
                medicamentoC={"nombreMedicamento":i["nombre"],"cantidadComprada":cantidadMedicamentoC,"precioCompra":precioCompra}
                i["stock"]=i["stock"]+cantidadMedicamentoC
        
        compras.append({"fechaCompra":fechaCompra,"proveedor":proveedor,"medicamentosComprados":medicamentoC})

        system("clear")
        input("Compra realizada con exito 😀\nPreciona Enter para continuar")

    elif opcion==3:
        print("Gracias por usar el programa ♥")
        bol=False
# hola=str(datetime.now())
# print(hola)



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
