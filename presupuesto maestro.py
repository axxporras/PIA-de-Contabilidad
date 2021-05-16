respuesta = ''

while respuesta != 12:
    print("\nPresupuesto Maestro *Ferretería Santa Lucía* \n")
    print("[1] Presupuesto de Ventas")
    print("[2] Determinar Saldo de Clientes y Flujo de Entradas")
    print("[3] Presupuesto de Producción")
    print("[4] Presupuesto de Requerimiento de Materiales")
    print("[5] Presupuesto de Compra de Materiales")
    print("[6] Determinación del saldo de Proveedores y Flujo de Salidas")
    print("[7] Presupuesto de Mano de Obra Directa")
    print("[8] Presupuesto de Gastos Indirectos de Fabricación")
    print("[9] Presupuesto de Gastos de Operación")
    print("[10] Determinación del Costo Unitario de Productos Terminados")
    print("[11] Valuación de Inventarios Finales")
    print("[12] Salir")
    respuesta = int(input("\n"))
    
    if respuesta== 1:
        print('[Presupuesto de Ventas]')
        print('\n~Primer semestre')
        print('\nProducto CL')
        unitCL1 = int(input('Unidades vendidas: '))
        precioCL1 = int(input('Precio de venta: '))
        print('\nProducto CE')
        unitCE1 = int(input('Unidades vendidas: '))
        precioCE1 = int(input('Precio de venta: '))
        print('\nProducto CR')
        unitCR1 = int(input('Unidades vendidas: '))
        precioCR1 = int(input('Precio de venta: '))
        
        print('\n~Segundo semestre')
        print('\nProducto CL')
        unitCL2 = int(input('Unidades vendidas: '))
        precioCL2 = int(input('Precio de venta: '))
        print('\nProducto CE')
        unitCE2 = int(input('Unidades vendidas: '))
        precioCE2 = int(input('Precio de venta: '))
        print('\nProducto CR')
        unitCR2 = int(input('Unidades vendidas: '))
        precioCR2 = int(input('Precio de venta: '))
        
        importecl1= unitCL1*precioCL1
        importecl2= unitCL2*precioCL2
        importecltotal= importecl1+importecl2
        
        importece1= unitCE1*precioCE1
        importece2= unitCE2*precioCE2
        importecetotal= importece1+importece2
        
        importecr1= unitCR1*precioCR1
        importecr2= unitCR2*precioCR2
        importecrtotal= importecr1+importecr2
        totalporsemestre1= importecl1+importece1+importecr1
        totalporsemestre2= importecl2+importece2+importecr2
        totalanual= importecltotal+importecetotal+importecrtotal
        
        print('\nImporte de Venta (Producto CL)')
        print(f'Primer semestre: {importecl1}')
        print(f'Segundo semestre: {importecl2}')
        print(f'Importe anual: {importecltotal}')
        
        print('\nImporte de Venta (Producto CE)')
        print(f'Primer semestre: {importece1}')
        print(f'Segundo semestre: {importece2}')
        print(f'Importe anual: {importecetotal}')
        
        print('\nImporte de Venta (Producto CR)')
        print(f'Primer semestre: {importecr1}')
        print(f'Segundo semestre: {importecr2}')
        print(f'Importe anual: {importecrtotal}')
        
        print('\nTotal de Ventas por Semestre')
        print(f'Primer semestre: {totalporsemestre1}')
        print(f'Segundo semestre: {totalporsemestre2}')
        print(f'Importe anual: {totalanual}')
        
        print('\nDevuelta al menu')

    elif respuesta== 2:
        print('[Determinar Saldo de Clientes y Flujo de Entradas]')
        clientes= int(input('Saldo de clientes [2020]: '))
        ventas= int(input('Ventas [2021]: '))
        totalclientes= clientes+ventas
        print(f'Total de Clientes 2021: {totalclientes}')
        
        cobranza= ventas*0.8
        entradas= cobranza+clientes
        print('\n~Entradas por efectivo')
        print(f'Por Cobranza del 2020: {clientes}')
        print(f'Por Cobranza del 2021: {cobranza}')
        print(f'Total de entradas 2021: {entradas}')
        
        saldo= totalclientes+entradas
        print(f'\nSaldo de clientes del 2021: {saldo}')
        
        print('\nDevuelta al menu')
    
    elif respuesta== 3:
        print("[Presupuesto de Producción]")
        print("[1] CL")
        print("[2] CE")
        print("[3] CR")
        producto= int(input('\n'))
        
        if producto== 1:
            print('[Producto CL]')
            print('~Primer Semestre \n')
            unidades1= int(input('Unidades a vender: '))
            invfinal1= int(input('Inventario final: '))
            totalunit1= unidades1+invfinal1
            print(f'Total de unidades: {totalunit1}')
            print(f'Inventorio inicial {invfinal1}')
            producir1= totalunit1-invfinal1
            print(f'Unidades a Producir: {producir1}')
            
            print('\n~Segundo Semestre \n')
            unidades2= int(input('Unidades a vender: '))
            invfinal2= int(input('Inventario final: '))
            totalunit2= unidades2+invfinal2
            print(f'Total de unidades: {totalunit2}')
            print(f'Inventario inicial: {invfinal1}')
            producir2= totalunit2-invfinal1
            print(f'Unidades a Producir: {producir2}')
            
            print('\n~Total Anual \n')
            unidades3= unidades1+unidades2
            totalunit3= unidades3+invfinal2
            producir3= producir1+producir2
            print(f'Unidades a vender: {unidades3}')
            print(f'Inventario final: {invfinal2}')
            print(f'Total de unidades: {totalunit3}')
            print(f'Inventario inicial: {invfinal1}')
            print(f'Unidades a Producir: {producir3}')
            
            print('\nDevuelta al menu')
            
        
        elif producto== 2:
            print('[Producto CE]')
            print('~Primer Semestre \n')
            unidades1= int(input('Unidades a vender: '))
            invfinal1= int(input('Inventario final: '))
            totalunit1= unidades1+invfinal1
            print(f'Total de unidades: {totalunit1}')
            print(f'Inventorio inicial {invfinal1}')
            producir1= totalunit1-invfinal1
            print(f'Unidades a Producir: {producir1}')
            
            print('\n~Segundo Semestre \n')
            unidades2= int(input('Unidades a vender: '))
            invfinal2= int(input('Inventario final: '))
            totalunit2= unidades2+invfinal2
            print(f'Total de unidades: {totalunit2}')
            print(f'Inventario inicial: {invfinal1}')
            producir2= totalunit2-invfinal1
            print(f'Unidades a Producir: {producir2}')
            
            print('\n~Total Anual \n')
            unidades3= unidades1+unidades2
            totalunit3= unidades3+invfinal2
            producir3= producir1+producir2
            print(f'Unidades a vender: {unidades3}')
            print(f'Inventario final: {invfinal2}')
            print(f'Total de unidades: {totalunit3}')
            print(f'Inventario inicial: {invfinal1}')
            print(f'Unidades a Producir: {producir3}')
            
            print('\nDevuelta al menu')
        
        elif producto== 3:
            print('[Producto CR]')
            print('~Primer Semestre \n')
            unidades1= int(input('Unidades a vender: '))
            invfinal1= int(input('Inventario final: '))
            totalunit1= unidades1+invfinal1
            print(f'Total de unidades: {totalunit1}')
            print(f'Inventorio inicial {invfinal1}')
            producir1= totalunit1-invfinal1
            print(f'Unidades a Producir: {producir1}')
            
            print('\n~Segundo Semestre \n')
            unidades2= int(input('Unidades a vender: '))
            invfinal2= int(input('Inventario final: '))
            totalunit2= unidades2+invfinal2
            print(f'Total de unidades: {totalunit2}')
            print(f'Inventario inicial: {invfinal1}')
            producir2= totalunit2-invfinal1
            print(f'Unidades a Producir: {producir2}')
            
            print('\n~Total Anual \n')
            unidades3= unidades1+unidades2
            totalunit3= unidades3+invfinal2
            producir3= producir1+producir2
            print(f'Unidades a vender: {unidades3}')
            print(f'Inventario final: {invfinal2}')
            print(f'Total de unidades: {totalunit3}')
            print(f'Inventario inicial: {invfinal1}')
            print(f'Unidades a Producir: {producir3}')
            
            print('\nDevuelta al menu')
        
        else:
            print('\nDevuelta al menu')
        
    
    elif respuesta== 4:
        print('[Presupuesto de Requerimiento de Materiales]')
        print('\n~Producto CL')        
        unidadescl1= int(input('Unidades a producir (Primer Semestre): '))
        unidadescl2= int(input('Unidades a producir (Segundo Semestre): '))
        unidadescl3= unidadescl1+unidadescl2
        print(f'Unidades a producir (Total): {unidadescl3}')
        
        print('\nMaterial A')
        materialcla= float(input('Requerimiento de material: '))
        totalacl1= unidadescl1*materialcla
        totalacl2= unidadescl2*materialcla
        totalacl3= totalacl1+totalacl2
        print(f'Total de Material A requerido: {totalacl1}, {totalacl2}, {totalacl3}')
        
        print('\nMaterial B')
        materialclb= float(input('Requerimiento de material: '))
        totalbcl1= unidadescl1*materialclb
        totalbcl2= unidadescl2*materialclb
        totalbcl3= totalbcl1+totalbcl2
        print(f'Total de Material B requerido: {totalbcl1}, {totalbcl2}, {totalbcl3}')
        
        print('\nMaterial C')
        materialclc= float(input('Requerimiento de material: '))
        totalccl1= unidadescl1*materialclc
        totalccl2= unidadescl2*materialclc
        totalccl3= totalccl1+totalccl2
        print(f'Total de Material C requerido: {totalccl1}, {totalccl2}, {totalccl3}')
        
        
        print('\n\n~Producto CE')        
        unidadesce1= int(input('Unidades a producir (Primer Semestre): '))
        unidadesce2= int(input('Unidades a producir (Segundo Semestre): '))
        unidadesce3= unidadesce1+unidadesce2
        print(f'Unidades a producir (Total): {unidadesce3}')
        
        print('\nMaterial A')
        materialcea= float(input('Requerimiento de material: '))
        totalace1= unidadesce1*materialcea
        totalace2= unidadesce2*materialcea
        totalace3= totalace1+totalace2
        print(f'Total de Material A requerido: {totalace1}, {totalace2}, {totalace3}')
        
        print('\nMaterial B')
        materialceb= float(input('Requerimiento de material: '))
        totalbce1= unidadesce1*materialceb
        totalbce2= unidadesce2*materialceb
        totalbce3= totalbce1+totalbce2
        print(f'Total de Material B requerido: {totalbce1}, {totalbce2}, {totalbce3}')
        
        print('\nMaterial C')
        materialcec= float(input('Requerimiento de material: '))
        totalcce1= unidadesce1*materialcec
        totalcce2= unidadesce2*materialcec
        totalcce3= totalcce1+totalcce2
        print(f'Total de Material C requerido: {totalcce1}, {totalcce2}, {totalcce3}')
        
        
        print('\n\n~Producto CR')        
        unidadescr1= int(input('Unidades a producir (Primer Semestre): '))
        unidadescr2= int(input('Unidades a producir (Segundo Semestre): '))
        unidadescr3= unidadescr1+unidadescr2
        print(f'Unidades a producir (Total): {unidadescr3}')
        
        print('\nMaterial A')
        materialcra= float(input('Requerimiento de material: '))
        totalacr1= unidadescr1*materialcra
        totalacr2= unidadescr2*materialcra
        totalacr3= totalacr1+totalacr2
        print(f'Total de Material A requerido: {totalacr1}, {totalacr2}, {totalacr3}')
        
        print('\nMaterial B')
        materialcrb= float(input('Requerimiento de material: '))
        totalbcr1= unidadescr1*materialcrb
        totalbcr2= unidadescr2*materialcrb
        totalbcr3= totalbcr1+totalbcr2
        print(f'Total de Material B requerido: {totalbcr1}, {totalbcr2}, {totalbcr3}')
        
        print('\nMaterial C')
        materialcrc= float(input('Requerimiento de material: '))
        totalccr1= unidadescr1*materialcrc
        totalccr2= unidadescr2*materialcrc
        totalccr3= totalccr1+totalccr2
        print(f'Total de Material C requerido: {totalccr1}, {totalccr2}, {totalccr3}')
        
        
        print('\n\nTotal de Requerimientos')
        totaldea1= totalacl1+totalace1+totalacr1
        totaldea2= totalacl2+totalace2+totalacr2
        totaldea3= totalacl3+totalace3+totalacr3
        totaldeb1= totalbcl1+totalbce1+totalbcr1
        totaldeb2= totalbcl2+totalbce2+totalbcr2
        totaldeb3= totalbcl3+totalbce3+totalbcr3
        totaldec1= totalccl1+totalcce1+totalccr1
        totaldec2= totalccl2+totalcce2+totalccr2
        totaldec3= totalccl3+totalcce3+totalccr3
        print(f'Material A Metros: {totaldea1}, {totaldea2}, {totaldea3}')
        print(f'Material B Metros: {totaldeb1}, {totaldeb2}, {totaldeb3}')
        print(f'Material C Metros: {totaldec1}, {totaldec2}, {totaldec3}')
        
        print('\nDevuelta al menu')
        
        
   
    elif respuesta== 5:
        print('[Presupuesto de Compra de Materiales]')
        print('\n~Material A')
        materiala1= int(input('Requerimiento de Materiales (Primer semestre): '))
        invfinala1= int(input('Inventario Final: '))
        totalmaterialesa1= materiala1+invfinala1
        print(f'Total de materiales: {totalmaterialesa1}')
        print(f'Inventario inicial: {invfinala1}')
        materialcomprara1= totalmaterialesa1-invfinala1
        print(f'Material a comprar: {materialcomprara1}')
        precioa1= int(input('Precio de compra: '))
        totala1= materialcomprara1*precioa1
        print(f'Total de Materia A en $ (Primer semestre): {totala1}')
        
        materiala2= int(input('\nRequerimiento de Materiales (Segundo semestre): '))
        invfinala2= int(input('Inventario Final: '))
        totalmaterialesa2= materiala2+invfinala2
        print(f'Total de materiales: {totalmaterialesa2}')
        print(f'Inventario inicial: {invfinala1}')
        materialcomprara2= totalmaterialesa2-invfinala1
        print(f'Material a comprar: {materialcomprara2}')
        precioa2= int(input('Precio de compra: '))
        totala2= materialcomprara2*precioa2
        print(f'Total de Materia A en $ (Segundo semestre): {totala2}')
        
        materiala3= materiala1+materiala2
        totalmaterialesa3= materiala3+invfinala2
        materialcomprara3= materialcomprara1+materialcomprara2
        totala3= totala1+totala2
        print(f'\nRequerimiento de Materiales (Total): {materiala3}')
        print(f'Inventario Final: {invfinala2}')
        print(f'Total de materiales: {totalmaterialesa3}')
        print(f'Inventario inicial: {invfinala1}')
        print(f'Material a comprar: {materialcomprara3}')
        print(f'Total de Material A en $ (Total): {totala3}')
        
        
        print('\n\n~Material B')
        materialb1= int(input('Requerimiento de Materiales (Primer semestre): '))
        invfinalb1= int(input('Inventario Final: '))
        totalmaterialesb1= materialb1+invfinalb1
        print(f'Total de materiales: {totalmaterialesb1}')
        print(f'Inventario inicial: {invfinalb1}')
        materialcomprarb1= totalmaterialesb1-invfinalb1
        print(f'Material a comprar: {materialcomprarb1}')
        preciob1= int(input('Precio de compra: '))
        totalb1= materialcomprarb1*preciob1
        print(f'Total de Materia B en $ (Primer semestre): {totalb1}')
        
        materialb2= int(input('\nRequerimiento de Materiales (Segundo semestre): '))
        invfinalb2= int(input('Inventario Final: '))
        totalmaterialesb2= materialb2+invfinalb2
        print(f'Total de materiales: {totalmaterialesb2}')
        print(f'Inventario inicial: {invfinalb1}')
        materialcomprarb2= totalmaterialesb2-invfinalb1
        print(f'Material a comprar: {materialcomprarb2}')
        preciob2= int(input('Precio de compra: '))
        totalb2= materialcomprarb2*preciob2
        print(f'Total de Materia B en $ (Segundo semestre): {totalb2}')
        
        materialb3= materialb1+materialb2
        totalmaterialesb3= materialb3+invfinalb2
        materialcomprarb3= materialcomprarb1+materialcomprarb2
        totalb3= totalb1+totalb2
        print(f'\nRequerimiento de Materiales (Total): {materialb3}')
        print(f'Inventario Final: {invfinalb2}')
        print(f'Total de materiales: {totalmaterialesb3}')
        print(f'Inventario inicial: {invfinalb1}')
        print(f'Material a comprar: {materialcomprarb3}')
        print(f'Total de Material B en $ (Total): {totalb3}')
        
        
        
        print('\n\n~Material C')
        materialc1= int(input('Requerimiento de Materiales (Primer semestre): '))
        invfinalc1= int(input('Inventario Final: '))
        totalmaterialesc1= materialc1+invfinalc1
        print(f'Total de materiales: {totalmaterialesc1}')
        print(f'Inventario inicial: {invfinalc1}')
        materialcomprarc1= totalmaterialesc1-invfinalc1
        print(f'Material a comprar: {materialcomprarc1}')
        precioc1= int(input('Precio de compra: '))
        totalc1= materialcomprarc1*precioc1
        print(f'Total de Materia C en $ (Primer semestre): {totalc1}')
        
        materialc2= int(input('\nRequerimiento de Materiales (Segundo semestre): '))
        invfinalc2= int(input('Inventario Final: '))
        totalmaterialesc2= materialc2+invfinalc2
        print(f'Total de materiales: {totalmaterialesc2}')
        print(f'Inventario inicial: {invfinalc1}')
        materialcomprarc2= totalmaterialesc2-invfinalc1
        print(f'Material a comprar: {materialcomprarc2}')
        precioc2= int(input('Precio de compra: '))
        totalc2= materialcomprarc2*precioc2
        print(f'Total de Materia C en $ (Segundo semestre): {totalc2}')
        
        materialc3= materialc1+materialc2
        totalmaterialesc3= materialc3+invfinalc2
        materialcomprarc3= materialcomprarc1+materialcomprarc2
        totalc3= totalc1+totalc2
        print(f'\nRequerimiento de Materiales (Total): {materialc3}')
        print(f'Inventario Final: {invfinalc2}')
        print(f'Total de materiales: {totalmaterialesc3}')
        print(f'Inventario inicial: {invfinalc1}')
        print(f'Material a comprar: {materialcomprarc3}')
        print(f'Total de Material C en $ (Total): {totalc3}')
        
        semestre1= totala1+totalb1+totalc1
        semestre2= totala2+totalb2+totalc2
        total= totala3+totalb3+totalc3
        print(f'\n\nCompras totales: {semestre1}, {semestre2}, {total}')
        
        print('\nDevuelta al menu')
    
    elif respuesta== 6:
        print('[Determinación del saldo de Proveedores y Flujo de Salidas]')
        proveedores= int(input('Saldo de Proveedores [2020]: '))
        ventas= int(input('Compras [2021]: '))
        totalproveedores= proveedores+ventas
        print(f'Total de Proveedores 2021: {totalproveedores}')
        
        cobranza= ventas*0.5
        salidas= cobranza+proveedores
        print('\n~Salidas de Efectivo')
        print(f'Por Proveedores del 2020: {proveedores}')
        print(f'Por Proveedores del 2021: {cobranza}')
        print(f'Total de Salidas 2021: {salidas}')
        
        saldo= totalproveedores - salidas
        print(f'\nSaldo de Proveedores del 2021: {saldo}')
        
        print('\nDevuelta al menu')
    
    elif respuesta== 7:
        print('[Presupuesto de Mano de Obra Directa]')
        print('\n~Producto CL')
        unidadesa1= int(input('Unidades a Producir (Primer semestre): '))
        horasa1= float(input('Horas requeridas por unidad: '))
        totalhorasa1= unidadesa1*horasa1
        print(f'Total de horas requeridas: {totalhorasa1}')
        cuotaa1= float(input('Cuota por hora: '))
        importea1= totalhorasa1*cuotaa1
        print(f'Importe de M.O.D. (Primer semestre): {importea1}')
        
        unidadesa2= int(input('\nUnidades a Producir (Segundo semestre): '))
        print(f'Horas requeridas por unidad: {horasa1}')
        totalhorasa2= unidadesa2*horasa1
        print(f'Total de horas requeridas: {totalhorasa2}')
        cuotaa2= float(input('Cuota por hora: '))
        importea2= totalhorasa2*cuotaa2
        print(f'Importe de M.O.D. (Primer semestre): {importea2}')
        
        
        unidadesa3= unidadesa1+unidadesa2
        totalhorasa3= totalhorasa1+totalhorasa2
        importea3= importea1+importea2
        print(f'\nUnidades a Producir (Total): {unidadesa3}')
        print(f'Horas requeridas por unidad: {horasa1}')
        print(f'Total de horas requeridas: {totalhorasa3}')
        print(f'Importe de M.O.D. (Total): {importea3}')
        
        
        
        print('\n\n~Producto CE')
        unidadesb1= int(input('Unidades a Producir (Primer semestre): '))
        horasb1= float(input('Horas requeridas por unidad: '))
        totalhorasb1= unidadesb1*horasb1
        print(f'Total de horas requeridas: {totalhorasb1}')
        cuotab1= float(input('Cuota por hora: '))
        importeb1= totalhorasb1*cuotab1
        print(f'Importe de M.O.D. (Primer semestre): {importeb1}')
        
        unidadesb2= int(input('\nUnidades a Producir (Segundo semestre): '))
        print(f'Horas requeridas por unidad: {horasb1}')
        totalhorasb2= unidadesb2*horasb1
        print(f'Total de horas requeridas: {totalhorasb2}')
        cuotab2= float(input('Cuota por hora: '))
        importeb2= totalhorasb2*cuotab2
        print(f'Importe de M.O.D. (Primer semestre): {importeb2}')
        
        
        unidadesb3= unidadesb1+unidadesb2
        totalhorasb3= totalhorasb1+totalhorasb2
        importeb3= importeb1+importeb2
        print(f'\nUnidades a Producir (Total): {unidadesb3}')
        print(f'Horas requeridas por unidad: {horasb1}')
        print(f'Total de horas requeridas: {totalhorasb3}')
        print(f'Importe de M.O.D. (Total): {importeb3}')
        
        
        print('\n\n~Producto CR')
        unidadesc1= int(input('Unidades a Producir (Primer semestre): '))
        horasc1= float(input('Horas requeridas por unidad: '))
        totalhorasc1= unidadesc1*horasc1
        print(f'Total de horas requeridas: {totalhorasc1}')
        cuotac1= float(input('Cuota por hora: '))
        importec1= totalhorasc1*cuotac1
        print(f'Importe de M.O.D. (Primer semestre): {importec1}')
        
        unidadesc2= int(input('\nUnidades a Producir (Segundo semestre): '))
        print(f'Horas requeridas por unidad: {horasc1}')
        totalhorasc2= unidadesc2*horasc1
        print(f'Total de horas requeridas: {totalhorasc2}')
        cuotac2= float(input('Cuota por hora: '))
        importec2= totalhorasc2*cuotac2
        print(f'Importe de M.O.D. (Primer semestre): {importec2}')
        
        
        unidadesc3= unidadesc1+unidadesc2
        totalhorasc3= totalhorasc1+totalhorasc2
        importec3= importec1+importec2
        print(f'\nUnidades a Producir (Total): {unidadesc3}')
        print(f'Horas requeridas por unidad: {horasc1}')
        print(f'Total de horas requeridas: {totalhorasc3}')
        print(f'Importe de M.O.D. (Total): {importec3}')
        
        
        horasrequeridas1= totalhorasa1+totalhorasb1+totalhorasc1
        horasrequeridas2= totalhorasa2+totalhorasb2+totalhorasc2
        horasrequeridas3= totalhorasa3+totalhorasb3+totalhorasc3
        importetotal1= importea1+importeb1+importec1
        importetotal2= importea2+importeb2+importec2
        importetotal3= importea3+importeb3+importec3
        
        print(f'\n\nTotal de horas requeridas por semestre: {horasrequeridas1}, {horasrequeridas2}, {horasrequeridas3}')
        print('Total M.O.D. por semestre: {importetotal1}, {importetotal2}, {importetotal3}')
        
        print('\nDevuelta al menu')
        
    
    elif respuesta== 8:
        print('[Presupuesto de Gastos Indirectos de Fabricación]')
        print('\n~Primer Semestre')
        depreciacion1= int(input('Depreciación: '))
        seguros= int(input('Seguros: '))
        mantenimiento1= int(input('Mantenimiento: '))
        energia1= int(input('Energeticos: '))
        varios= int(input('Varios: '))
        total1= depreciacion1+seguros+mantenimiento1+energia1+varios
        print(f'Total G.I.F. por semestre: {total1}')
        
        
        print('\n\n~Segundo Semestre')
        depreciacion2= int(input('\nDepreciación: '))
        print(f'Seguros: {seguros}')
        mantenimiento2= int(input('Mantenimiento: '))
        energia2= int(input('Energeticos: '))
        print('Varios: {varios}')
        total2= depreciacion2+seguros+mantenimiento2+energia2+varios
        print(f'Total G.I.F. por semestre: {total2}')
        
        
        print('\n\n~Total Anual')
        depreciacion3= depreciacion1+depreciacion2
        seguros3= seguros+seguros
        mantenimiento3= mantenimiento1+mantenimiento2
        energia3= energia1+energia2
        varios3= varios+varios
        total3= total1+total2        
        print(f'Depreciación: {depreciacion3}')
        print(f'Seguros: {seguros3}')
        print(f'Mantenimiento: {mantenimiento3}')
        print(f'Energeticos: {energia3}')
        print(f'Varios: {varios3}')
        print(f'Total G.I.F. por semestre: {total3}')
        
        print(f'\n\nTotal de G.I.F.: {total3}')
        horasmod= int(input('Total horas M.O.D. Anual: '))
        horagif= total3/horasmod
        print(f'Costo por Hora de G.I.F.: {horagif}')
    
    
    elif respuesta== 9:
        print('[Presupuesto de Gastos de Operación]')
        print('\n~Primer Semestre')
        depreciacion1= int(input('Depreciación: '))
        salarios= int(input('Sueldos y Salarios: '))
        comisiones1= int(input('Comisiones: '))
        varios1= int(input('Varios: '))
        prestamo= int(input('Intereses por Préstamo: '))
        total1= depreciacion1+salarios+comisiones1+varios1+prestamo
        print(f'Total de Gastos de Operación: {total1}')
        
        print('\n\n~Segundo Semestre')
        depreciacion2= int(input('Depreciación: '))
        print(f'Sueldos y Salarios: {salarios}')
        comisiones2= int(input('Comisiones: '))
        varios2= int(input('Varios: '))
        print('Intereses por Préstamo: {prestamo}')
        total2= depreciacion2+salarios+comisiones2+varios2+prestamo
        print(f'Total de Gastos de Operación: {total2}')
        
        print('\n\n~Total Anual')
        depreciacion3= depreciacion1+depreciacion2
        salarios3= salarios+salarios
        comisiones3= comisiones1+comisiones2
        varios3= varios1+varios2
        prestamo3= prestamo+prestamo
        total3= total1+total2        
        print(f'Depreciación: {depreciacion3}')
        print(f'Salarios: {salarios3}')
        print(f'Comisiones: {comisiones3}')
        print(f'Varios: {varios3}')
        print(f'Intereses por Préstamo: {prestamo3}')
        print(f'Total de Gastos por Operación: {total3}')
        
        print('\nDevuelta al menu')
    
    elif respuesta== 10:
        print('[Determinación del Costo Unitario de Productos Terminados]')
        print("[1] CL")
        print("[2] CE")
        print("[3] CR")
        producto= int(input('\n'))
        
        if producto==1:
            print('[Producto CL]')
            print('\n~Costo')
            materiala1= float(input('Material A: '))
            materialb1= float(input('Material B: '))
            materialc1= float(input('Material C: '))
            mano1= float(input('Mano de Obra: '))
            gastos1= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Cantidad')
            materiala2= float(input('Material A: '))
            materialb2= float(input('Material B: '))
            materialc2= float(input('Material C: '))
            mano2= float(input('Mano de Obra: '))
            gastos2= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Costo Unitario')
            materiala3= materiala1*materiala2
            materialb3= materialb1*materialb2
            materialc3= materialc1*materialc2
            mano3= mano1*mano2
            gastos3= gastos1*gastos2
            print(f'Material A: {materiala3}')
            print(f'Material B: {materialb3}')
            print(f'Material C: {materialc3}')
            print(f'Mano de Obra: {mano3}')
            print(f'Gatos Indirectos de Fabricación: {gastos3}')
            
            costo= materiala3+materialb3+materialc3+mano3+gastos3
            print(f'\nCosto Unitario: {costo}')
            
            print('\nDevuelta al menu')
            
        elif producto==2:
            print('[Producto CE]')
            print('\n~Costo')
            materiala1= float(input('Material A: '))
            materialb1= float(input('Material B: '))
            materialc1= float(input('Material C: '))
            mano1= float(input('Mano de Obra: '))
            gastos1= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Cantidad')
            materiala2= float(input('Material A: '))
            materialb2= float(input('Material B: '))
            materialc2= float(input('Material C: '))
            mano2= float(input('Mano de Obra: '))
            gastos2= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Costo Unitario')
            materiala3= materiala1*materiala2
            materialb3= materialb1*materialb2
            materialc3= materialc1*materialc2
            mano3= mano1*mano2
            gastos3= gastos1*gastos2
            print(f'Material A: {materiala3}')
            print(f'Material B: {materialb3}')
            print(f'Material C: {materialc3}')
            print(f'Mano de Obra: {mano3}')
            print(f'Gatos Indirectos de Fabricación: {gastos3}')
            
            costo= materiala3+materialb3+materialc3+mano3+gastos3
            print(f'\nCosto Unitario: {costo}')
            
            print('\nDevuelta al menu')
        
        elif producto==3:
            print('[Producto CR]')
            print('\n~Costo')
            materiala1= float(input('Material A: '))
            materialb1= float(input('Material B: '))
            materialc1= float(input('Material C: '))
            mano1= float(input('Mano de Obra: '))
            gastos1= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Cantidad')
            materiala2= float(input('Material A: '))
            materialb2= float(input('Material B: '))
            materialc2= float(input('Material C: '))
            mano2= float(input('Mano de Obra: '))
            gastos2= float(input('Gastos Indirectos de Fabricación: '))
            
            print('\n\n~Costo Unitario')
            materiala3= materiala1*materiala2
            materialb3= materialb1*materialb2
            materialc3= materialc1*materialc2
            mano3= mano1*mano2
            gastos3= gastos1*gastos2
            print(f'Material A: {materiala3}')
            print(f'Material B: {materialb3}')
            print(f'Material C: {materialc3}')
            print(f'Mano de Obra: {mano3}')
            print(f'Gatos Indirectos de Fabricación: {gastos3}')
            
            costo= materiala3+materialb3+materialc3+mano3+gastos3
            print(f'\nCosto Unitario: {costo}')
            
            print('\nDevuelta al menu')
        
        else:
            print('\nDevuelta al menu')
        
        
    
    elif respuesta== 11:
        print('[Valuación de Inventarios Finales]')
        print('\n*Inventario Final de Materiales*')
        print('~Unidades')
        materiala1= float(input('Material A: '))
        materialb1= float(input('Material B: '))
        materialc1= float(input('Material C: '))
            
        print('\n~Costo Unitario')
        materiala2= float(input('Material A: '))
        materialb2= float(input('Material B: '))
        materialc2= float(input('Material C: '))
            
        print('\n~Costo Total')
        materiala3= materiala1*materiala2
        materialb3= materialb1*materialb2
        materialc3= materialc1*materialc2
        print(f'Material A: {materiala3}')
        print(f'Material B: {materialb3}')
        print(f'Material C: {materialc3}')
            
        costo1= materiala3+materialb3+materialc3
        print(f'Inventario Final de Materiales: {costo1}')
            
        
        print('\n\n*Inventario Final de Producto Terminado*')
        print('~Unidades')
        productoa1= float(input('Producto CL: '))
        productob1= float(input('Producto CE: '))
        productoc1= float(input('Producto CR: '))
            
        print('\n~Costo Unitario')
        productoa2= float(input('Producto CL: '))
        productob2= float(input('Producto CE: '))
        productoc2= float(input('Producto CR: '))
            
        print('\n~Costo Total')
        productoa3= productoa1*productoa2
        productob3= productob1*productob2
        productoc3= productoc1*productoc2
        print(f'Producto CL: {productoa3}')
        print(f'Producto CE: {productob3}')
        print(f'Producto CR: {productoc3}')
            
        costo2= productoa3+productob3+productoc3
        print(f'Inventario Final de Producto Terminado: {costo2}')
            
        print('\nDevuelta al menu')           
            
               
    elif respuesta== 12:
        print('\nGracias, vuelva pronto :)')