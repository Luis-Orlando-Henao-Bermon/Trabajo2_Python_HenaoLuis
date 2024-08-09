import json #como se trabaja con archivos json hay que imortar la libreria  de json
from os import system #se importa sytem para poder limpiar pantalla en git bash
from datetime import datetime #se importa datetime para poder saber la hora en que se hacen los registros 


#seccion para importar los archivos de json y poder trabajar con ellos 
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
while bol==True: #se usa un bucle while para que se repita el menu hasta que sellecione la opcion 3 que termina el bucle
    system("clear")# con esto se limpia consola en git bash
    opcion=int(input("==========Menu==========\n1. Registrar ventas\n2. Registrar compra\n3. Salir\nEscribe tu opcion\n"))
    system("clear")
    if opcion==1:
        fechaVenta=str(datetime.now()) #se usa un str para poder leer el datetime.now() como entero y no tenga problemas al momento de exportarlo en el json
        print("----------Pacientes----------")
        
        for i in pacientes: #se usa un bucle for para que mire todos los pacientes y muestre los nombres con sus id
            print("ID:",i["id"],"------ Nombre:",i["nombre"])
            print("------------------------------------------")
        
        idPacienteV=int(input("Ingresa el ID del paciente al que se le realizara la venta\n"))
        system("clear")
        
        for i in pacientes:#despues de saber el id del paciente al que se le quiere hacer la venta se usa un bucle if para comprararlo con los id que hay en el json pacientes 
            if i["id"]==idPacienteV: #si un paciente tiene el id ingresado por el usuario a la variable pacienteV se le agrega en un diccionario el nombre y direccion
                pacienteV={"nombre":i["nombre"],"direccion":i["direccion"]}
        
        print("----------Empleados----------")
        for i in empleados:# se usa un bucle for para que mire todos los empleados y muestre sus nombres y sus id
            print("ID:",i["id"],"------ Nombre:",i["nombre"])
            print("------------------------------------------")
        
        idEmpleadoV=int(input("Ingresa el ID del empleado que realizara la venta\n"))
        
        for i in empleados: # despues de saber el id del empleado se usa un bucle for para mirar en el json de empleados y ver si un empleado tiene ese id 
            if i["id"]==idEmpleadoV:#si un empleado tiene ese id a la variable empleadoV se le agrega en un diccionario el nombre y el cargo de ese empleado
                empleadoV={"nombre":i["nombre"],"cargo":i["cargo"]}
        
        system("clear")
        print("----------Medicamentos----------")
        
        for i in medicamentos: # se usa un bucle for para mirar en el json de medicamentos y motrar los nombres, precios y cantidad en stock 
            print("ID:",i["id"],"------ Nombre:",i["nombre"],"------ Precio:",i["precio"],"------ Cantidad en stock:",i["stock"])
            print("------------------------------------------")
        
        idMedicamentoV=int(input("Ingresa el ID del medicamento que se va a vender\n"))
        cantidadMedicamentoV=int(input("Ingresa la cantidad de de medicamento que se va a vender\n"))
        
        for i in medicamentos:# se usa un bucle for para mirar si algun medicamento tiene el id ingresado por el usuario
            if i["id"]==idMedicamentoV:# si n medicamento tiene el mismo id ingresado por el usuario a la variable medicamentoV se le agrega en un diccionario el nombre de ese medicamento, la cantidad vendida y el precio de ese medicamento
                medicamentoV={"nombreMedicamento":i["nombre"],"cantidadVendida":cantidadMedicamentoV,"precio":i["precio"]}
                i["stock"]=i["stock"]-cantidadMedicamentoV # al json de medicamentos se le resta la cantidad de medicamento vendida
        
        #despues de saber los datos de la fecha en que se realiza la venta, paciente, empleado y medicamento se le agrega el json de ventas usando un .append a la variable que contiene el json de ventas
        ventas.append({"fechaVenta":fechaVenta,"paciente":pacienteV,"empleado":empleadoV,"medicamentosVendidos":medicamentoV})
        system("clear")
        input("Venta realizada con exito 😀\nPreciona Enter para continuar")

    elif opcion==2:

        fechaCompra=str(datetime.now())#se usa un str para poder leer el datetime.now() como entero y no tenga problemas al momento de exportarlo en el json

        print("----------Proveedores----------")
        for i in proveedores:# se usa un bucle for para mirar en el json de proveedores y mostrar el id y nombre 
            print("ID:",i["id"],"-------- Nombre:",i["nombre"])

        idProveedor=int(input("Ingresa el id del proveedor al que se le realizara la compra\n"))

        for i in proveedores:#se usa un bucle for para mirar si algun proveedor tiene ese id 
            if i["id"]==idProveedor: #si algun proveedor tiene ese id a la variable proveedor se le agrega en un diccionario el nombre y contacto de ese proveedor
                proveedor={"nombre":i["nombre"],"contacto":i["contacto"]}

        system("clear")
        print("----------Medicamentos----------")
        for i in medicamentos:# se usa un bucle for para mirar en el json de medicamentos y motrar los nombres, precios y cantidad en stock 
            print("ID:",i["id"],"------ Nombre:",i["nombre"],"------ Precio:",i["precio"],"------ Cantidad en stock:",i["stock"])
            print("------------------------------------------")
        
        idMedicamentoC=int(input("Ingresa el ID del medicamento que se va a comprar\n"))
        cantidadMedicamentoC=int(input("Ingresa la cantidad de de medicamento que se va a comprar\n"))
        precioCompra=int(input("Ingrese el precio de compra del medicamento\n"))
        for i in medicamentos:# se usa un bucle for para mirar si algun medicamento tiene el id ingresado por el usuario
            if i["id"]==idMedicamentoC:# si n medicamento tiene el mismo id ingresado por el usuario a la variable medicamentoV se le agrega en un diccionario el nombre de ese medicamento, la cantidad comprada y el precio de compra de ese medicamento
                medicamentoC={"nombreMedicamento":i["nombre"],"cantidadComprada":cantidadMedicamentoC,"precioCompra":precioCompra}
                i["stock"]=i["stock"]+cantidadMedicamentoC #al json de medicamentos se le suma la cantidad de medicamento comprada 
        
        # al json de compras se le agregas los datos obtenidos anteriormente de la fecha de compra, proveedor y medicamnto comprado
        compras.append({"fechaCompra":fechaCompra,"proveedor":proveedor,"medicamentosComprados":medicamentoC})

        system("clear")
        input("Compra realizada con exito 😀\nPreciona Enter para continuar")

    elif opcion==3:
        print("Gracias por usar el programa ♥")
        bol=False

# seccion de exportacion de archivos json con esto se guardan todos los cambios en los archivos json
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

# Desarrollado por Luis Henao