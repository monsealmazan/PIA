print("Presupuesto de Ventas")
P1=(input("Producto 1:"))
P2=(input("Producto 2:"))
C1=int (input("Cantidad del producto 1:"))
C2= int (input("Cantidad del producto 2:"))
VV1=int (input("Valor de venta unitario del producto 1:"))
VV2=int (input("Valor de venta unitario del producto 2:"))
IV1=C1*VV1
IV2=C2*VV2
T1=C1+C2
T2=VV1+VV2
T3=IV1+IV2
print("Producto  |  Cantidad  |  Valor Venta unitario  |  Ingreso por ventas")
print ((P1),"    |", (C1),"   |",(VV1),"               |", (IV1))
print ((P2),"    |", (C2),"   |",(VV2),"               |", (IV2))
print("Total     |",(T1),"    |",(T2),"                |",(T3))
print ("-"*100)

print("Determinacion del saldo de Clientes y Flujo de Entrada")
SC=int (input("Saldo Total de clientes Diciembre del 2020:"))
TC=SC+T3
print("Detalle     |    Importe |   Total")
print("Saldo de Clientes Diciembre 2020|    |",(SC))
print("Ventas 2021|    |",(T3))
print("Total de Clientes |    |",(TC))
print("Entrada de efectivo")
print("Por Cobranza del 2020 |",(SC),"|")
PC=T3*.8
print("Por Cobranza del 2021 |",(PC),"|")
TE=SC+PC
print("Total de Entradas |    |",(TE))
SCF=TC-TE
print("Saldo de clientes del 2021|       |",(SCF))
print ("-"*100)


print ("Presupuesto de produccion")
FPT1=int (input("Inversion FPT del producto 1:"))
FPT2=int (input("Inversion FPT del producto 2:"))
IPT1=int (input("Inversion IPT del producto 1:"))
IPT2=int (input("Inversion IPT del producto 2:"))
TOTFPT1=C1+FPT1
TOTFPT2=C2+FPT2
PR1=TOTFPT1-IPT1
PR2=TOTFPT2-IPT2
print ("Producto |",(P1),"     |",(P2))
print("Ventas    |",(C1),"     |",(C2))
print("Inversion FPT|",(FPT1),"|",(FPT2))
print("TOTAL    |",(TOTFPT1),"|",(TOTFPT2))
print("Inversion IPT|",(IPT1),"|",(IPT2))
print("Produccion   |",(PR1),"|",(PR2))
print ("-"*100)

print("Presupuesto de Materiales y Compras")
MP1=(input("Material A:"))
MP2=(input("Material B:"))
SEM1P1=int (input("Unidades a producir del 1er semestre del producto 1:"))
SEM2P1=int (input("Unidades a producir del 2do semestre del producto 1:"))
SEM1P2=int (input("Unidades a producir del 1er semestre del producto 2:"))
SEM2P2=int (input("Unidades a producir del 2do semestre del producto 2:"))
TOTALAÑOP1=SEM1P1+SEM2P1
TOTALAÑOP2=SEM1P2+SEM2P2
RMA1=int (input("Requerimiento de material A para producto 1 en el 1er semestre:"))
RMA2=int (input("Requerimiento de material A para producto 2 en el 2do semestre:"))
RMB1=int (input("Requerimiento de material B para producto 1 en el 1er semestre:"))
RMB2=int (input("Requerimiento de material B para producto 2 en el 2do semestre:"))
IF1P1=int (input("Inventario final 1er semestre del producto 1:"))
IF2P1=int (input("Inventario final 2do semestre del producto 1:"))
IF1P2=int (input("Inventario final 1er semestre del producto 2:"))
IF2P2=int (input("Inventario final 2do semestre del producto 2:"))
II1P1=int (input("Inventario inical 1er semestre del producto 1:"))
II2P1=int (input("Inventario inicial 2do semestre del producto 1:"))
II1P2=int (input("Inventario inical 1er semestre del producto 2:"))
II2P2=int (input("Inventario inicial 2do semestre del producto 2:"))
PCA1= int (input("Precio de compra material A 1er semestre:"))
PCA2= int (input("Precio de compra material A 2do semestre:"))
PCB1= int (input("Precio de compra material B 1er semestre:"))
PCB2= int (input("Precio de compra material B 2do semestre:"))

REQMATA1=RMA1+RMA2
REQMATA2=RMB1+RMB2
REQMATAÑO=REQMATA1+REQMATA2
print("Materia Prima    | 1er Semestre |   2do Semestre | Total del año")
print(MP1)
print("Unidades a producir|",(SEM1P1),"|",(SEM2P1),"|",(TOTALAÑOP1))
print("Requerimiento de materiales|",(REQMATA1),"|",(REQMATA2),"|",(REQMATAÑO))
print("Inventario final |",(IF1P1),"|",(IF2P1),"|",(IF2P1))
TOTALMATS1P1=SEM1P1+IF1P1
TOTALMATS2P1=SEM2P1+IF2P1
TOTALMATAÑOP1=TOTALAÑOP1+IF2P1
print("Total de Materiales |",(TOTALMATS1P1),"|",(TOTALMATS2P1),"|",(TOTALMATAÑOP1))
print("Inventario Inicial |",(II1P1),"|",(II2P1),"|",(II2P1))
COMPRA1P1=TOTALMATS1P1-II1P1
COMPRA2P1=TOTALMATS2P1-II2P1
COMPRATOT=TOTALAÑOP1-II2P1
print("Material a comprar |",(COMPRA1P1),"|",(COMPRA2P1),"|",(COMPRATOT))
print("Precio de compra |",(PCA1),"|",(PCA2))
materialdinero1=COMPRA1P1*PCA1
materialdinero2=COMPRA2P1*PCA2
totaldinero1=materialdinero1+materialdinero2
print("Total de material |",(materialdinero1),"|",(materialdinero2),"|",(totaldinero1))
print ("-"*100)

print("Materia Prima    | 1er Semestre |   2do Semestre | Total del año")
print(MP2)
print("Unidades a producir|",(SEM1P2),"|",(SEM2P2),"|",(TOTALAÑOP2))
print("Requerimiento de materiales|",(REQMATA1),"|",(REQMATA2),"|",(REQMATAÑO))
print("Inventario final |",(IF1P2),"|",(IF2P2),"|",(IF2P2))
TOTALMATS1P2=SEM1P2+IF1P2
TOTALMATS2P2=SEM2P2+IF2P2
TOTALMATAÑOP2=TOTALAÑOP2+IF2P2
print("Total de Materiales |",(TOTALMATS1P2),"|",(TOTALMATS2P2),"|",(TOTALMATAÑOP2))
print("Inventario Inicial |",(II1P2),"|",(II2P2),"|",(II2P2))
COMPRA1P2=TOTALMATS1P2-II1P2
COMPRA2P2=TOTALMATS2P2-II2P2
COMPRATOT2=TOTALAÑOP2-II2P2
print("Material a comprar |",(COMPRA1P2),"|",(COMPRA2P2),"|",(COMPRATOT2))
print("Precio de compra |",(PCB1),"|",(PCB2))
materialdinero3=COMPRA1P1*PCB1
materialdinero4=COMPRA2P1*PCB2
totaldinero2=materialdinero3+materialdinero4
print("Total de material |",(materialdinero3),"|",(materialdinero4),"|",(totaldinero2))
print ("-"*100)

print("Detalle de Materiales y compras")
CONSUMOA=int (input("Consumo de material A:"))
CONSUMOB= int(input("Consumo de material B:"))
INVFA=int(input("Inversion final de A:"))
INVFB=int(input("Inversion final de B:"))
INVIA=int(input("Inversion inicial de A:"))
INVIB=int(input("Inversion inicial de B:"))
UNIDA=int(input("Unidad de compras de A:"))
UNIDB=int(input("Unidad de compras de B:"))
VUA=int(input("Valor unitario de A:"))
VUB=int(input("Valor unitario de B:"))
CTOTALA=UNIDA*VUA
CTOTALB=UNIDB*VUB
CTOTAL=CTOTALA+CTOTALB
print("Detalle     |",(MP1),"|",(MP2),"|    TOTAL")
print("Consumo     |",(CONSUMOA),"|",(CONSUMOB),"|")
print("Inv Final   |",(INVFA),"|",(INVFB),"|")
print("Inv Inicial |",(INVIA),"|",(INVIB),"|")
print("Unid. Compras|",(UNIDA),"|",(UNIDB),"|")
print("Valor Unitario|",(VUA),"|",(VUB),"|")
print("TOTAL|",(CTOTALA),"|",(CTOTALB),"|",(CTOTAL))
print ("-"*100)

print("Determinacion del saldo de Proveedores y Flujos de Salida")
SP20=int(input("Saldo de Proveedores Dic 2020:"))
print("Detalle     |    Importe |   Total")
print("Saldo de Proveedores Diciembre 2020|    |",(SP20))
print("Compras 2021|    |",(CTOTAL))
TP=SP20+CTOTAL
print("Total de Proveedores |    |",(TP))
print("Salida de efectivo")
print("Por Proveedores del 2020 |",(SP20),"|")
PP=CTOTAL*.5
print("Por Proveedores del 2021 |",(PP),"|")
TS=SP20+PP
print("Total de Salidas |    |",(TS))
SPF=TP-TS
print("Saldo de Proveedores del 2021|       |",(SPF))
print ("-"*100)

print("Presupuesto de Mano de Obra directa")
PRODP1= int (input("Cantidad de produccion de producto 1:"))
PRODP2= int (input("Cantidad de produccion de producto 2:"))
HUP1=int (input("Horas por unidad de producto 1:"))
HUP2=int (input("Horas por unidad de producto 2:"))
CPP1=int (input("Costo por unidad del producto 1:"))
CPP2=int (input("Costo por unidad del producto 2:"))
CPHP1= int (input("Cuota por hora del producto 1:"))
CPHP2= int (input("Cuota por hora del producto 2:"))
print("Producto   |",(P1),"|",(P2),"|  total",)
print("Produccion |",(PRODP1),"|",(PRODP2),"|",)
print("H/h x unidad |",(HUP1),"|",(HUP2),"|",)
THP1=PRODP1*HUP1
THP2=PRODP2*HUP2
HTOTAL=THP1+THP2
CXH=CPHP1+CPHP2
print("TOTAL HORAS |",(THP1),"|",(THP2),"|",(HTOTAL))
print("Cuota x hora |",(CPHP1),"|",(CPHP2),"|",(CXH))
ODP1=THP1*CPHP1
ODP2=THP2*CPHP2
ODT=ODP2+ODP1
print("Total Moneda|",(ODP1),"|",(ODP2),"|",(ODT))
print ("-"*100)

print("Presupuesto Inventario Final Materia Primaria")
UMA=int (input("Unidades del material A:"))
UMB=int (input("Unidades del material B:"))
CUAA=int (input("Costo Unitario del material A:"))
CUBB=int (input("Costo Unitario del material B:"))
print("Detalle     |",(MP1),"|",(MP2))
print("Unidades    |",(UMA),"|",(UMB))
print("Costo Unitario|",(CUAA),"|",(CUBB))
SUBA=UMA*CUAA
SUBB=UMB*CUBB
print("SUBTOTAL|",(SUBA),"|",(SUBB))
TOT=SUBA+SUBB
print("TOTAL|            |          |",(TOT))
print ("-"*100)

print("Presupuesto de Gastos de Operacion")
DP1= int(input("Drepreciacion del 1er semestre:"))
DP2= int(input("Drepreciacion del 2do semestre:"))
SYS1= int(input("Sueldos y Salarios 1er semestre:"))
SYS2= int(input("Sueldos y Salarios 2do semestre:"))
COM1= int(input("Comisiones 1er semestre:"))
COM2= int(input("Comisiones 2do semestre:"))
VAR1= int(input("Varios 1er semestre:"))
VAR2= int(input("Varios 2do semestre:"))
IDP= int(input("Intereses de prestamo:"))
TGO1=DP1+SYS1+COM1+VAR1+IDP
TGO2=DP2+SYS2+COM2+VAR2+IDP
TDP=DP1+DP2
TSYS=SYS1+SYS2
TCOM=COM1+COM2
TVAR=VAR1+VAR2
TIP=IDP*2
TGOA=TDP+TSYS+TCOM+TVAR+TIP
print("        | 1er Semestre |   2do Semestre | Total del año")
print("Depreciacion|",(DP1),"|",(DP2),"|",(TDP))
print("sueldos y Salarios|",(SYS1),"|",(SYS2),"|",(TDP))
print("Comisiones|",(COM1),"|",(COM2),"|",(TCOM))
print("Varios|",(VAR1),"|",(VAR2),"|",(TVAR))
print("Intereses de prestamo|",(IDP),"|",(IDP),"|",(TIP))
print("Total de gastos de operacion|",(TGO1),"|",(TGO2),"|",(TGOA))
print ("-"*100)


print("Presupuesto de Inventarios Final de Productos Terminados")
UUP1=int (input("Unidades del producto 1:"))
UUP2=int (input("Unidades del producto 2:"))
CP111=int (input("Costo Unitario del producto 1:"))
CP222=int (input("Costo Unitario del producto 2:"))
print("Producto   |",(P1),"|",(P2))
print("Unidades    |",(UUP1),"|",(UUP2))
print("Costo Unitario|",(CP111),"|",(CP222))
SUBP1=UUP1*CP111
SUBP2=UUP2*CP222
print("SUBTOTAL|",(SUBP1),"|",(SUBP2))
TO=SUBP2+SUBP1
print("TOTAL|            |          |",(TO))
print ("-"*100)


print("Presupuesto de Gastos de Fabricación")
print("Producto   |",(P1),"|",(P2),"|  total",)
print("Cuota x hora |",(CPHP1),"|",(CPHP2),"|",(CXH))
print("TOTAL HORAS |",(THP1),"|",(THP2),"|",(HTOTAL))
print("Produccion |",(PRODP1),"|",(PRODP2),"|",)
CXT1=CPHP1*THP1
CXT2=CPHP2*THP2
CXTOTAL=CXT2+CXT1
print("Total |",(CXT1),"|",(CXT2),"|",(CXTOTAL))
print ("-"*100)


print("Productos Terminados")
print(P1)
print("Detalle   | Costo| Cantidad | Costo Unitario")
CUU1=VUA*RMA1
CUU2=VUB*RMB1
print(MP1),"|",(VUA),"|",(RMA1),"|",(CUU1)
print(MP2),"|",(VUB),"|",(RMB1),"|",(CUU2)
mma=ODP1*HUP1
print("Mano de Obra|",(ODP1),"|",(HUP1),"|",(mma))
GF1=INVIA*HUP1
print("Gasto fabricacion|",(INVIA),"|",(HUP1),"|",(GF1))
CUT1=CUU2+CUU1+mma+GF1
print("Costo unitario|             |            |",(CUT1))


print(P2)
print("Detalle   | Costo| Cantidad | Costo Unitario")
CUU3=VUA*RMA2
CUU4=VUB*RMB2
print(MP1),"|",(VUA),"|",(RMA2),"|",(CUU2)
print(MP2),"|",(VUB),"|",(RMB2),"|",(CUU4)
mmB=ODP1*HUP1
print("Mano de Obra|",(ODP1),"|",(HUP1),"|",(mmB))
GF2=INVIA*HUP1
print("Gasto fabricacion|",(INVIA),"|",(HUP1),"|",(GF2))
CUT1=CUU3+CUU4+mmB+GF2
print("Costo unitario|             |            |",(CUT1))
print ("-"*100)


print("Resumen para hallar el Costo de Ventas")
IIGT=int (input("Inventario inicial de producto terminado:"))
print("DETALLE                                | IMPORTE S/")
MPT=totaldinero1+totaldinero2
print("MATERIA PRIMA                          |",(MPT))
print("MANO DE OBRA DIRECTA                   |",(ODT))
print("GASTOS INDIRECTOS                      |",(CXTOTAL))
COSTOTOL=MPT+ODT+CXTOTAL
print("COSTO TOTAL                            |",(COSTOTOL))
print("COSTO TOTAL DE PRODUCCION              |",(COSTOTOL))
print("Inventario inicial prod term           |",(IIGT))
print("Inventario final prod term           |",(CUT1))
print ("-"*100)

print("Estado de Costo de Produccion y Ventas")
COMPRATOTAL=CTOTAL
SIM= int(input("Saldo inicial de Materiales:"))
MD=SIM+CTOTAL
print("Presupuesto de Enero a Diciembre:")
print("Saldo Inicial. de Materiales |",(SIM))
print("Compras de Materiales |",(CTOTAL))
print("Material Disponible |",(MD))
print("Inventario Final de Materiales |",(TO))
MU=MD-TO
print("Materiales Utilizados |",(MU))
print("Mano de obra directa |",(ODT))
print("Gastos de Fabricacion Indirectos |",(CXTOTAL))
CDP=CXTOTAL+ODT+MU
print("Costo de Produccion |",(CDP))
print("Inventario inicial de productos terminados |",(IIGT))
TPD=CDP+IIGT
print("Total de produccion disponible |",(TPD))
print("Inventario final de productos terminados |",(CUT1))
CDV=TPD-CUT1
print("Costo de ventas |",(CDV))
print ("-"*100)

print("Estado de Resultados")
print ("Ventas |",(T3))
print("Costo de Ventas |",(CDV))
UB=T3-CDV
print("Utilidad Bruta |",(UB))
print("Gastos de operacion |",(TGOA))
UDO=UB-TGOA
print("Utilidad de Operacion |",(UDO))
ISR=UDO*.3
PTU=UDO*.1
print("ISR |",(ISR))
print("PTU |",(PTU))
UN=UDO-ISR-PTU
print("Utilidad Neta |",(UN))
print("-"*100)

print("Estado de Flujo de EFECTIVO")
SIE=int (input("Saldo Inicial de Efectivo:"))
print("Saldo Inicial de Efectivo |          |",(SIE))
print("Entradas:")
print("Cobranza 2020 |",(SC),"|")
print("Cobranza 2021 |",(PC),"|")
TDE=SC+PC
print("Total de entradas |     |",(TDE))
EF=SIE+TDE
print("Efectivo Disponible |    |",(EF))
print("SALIDAS:")
print("Proveedores 2020|",(SP20),"|")
print("Proveedores 2021|",(PP),"|")
print("Mano de obra directa |",(ODT),"|")
print("Gastos de Fabricacion Indirectos |",(CXTOTAL),"|")
print("Gastos de Operacion |",(TGOA),"|")
CDAF=int (input("Compra de activo fijo:"))
PISR= int (input("Pago ISR 2020:"))
print("Pago ISR 2020", (PISR),"|")
print("Pago ISR 2021", (ISR),"|")
TDS=SP20+PP+ODT+CXTOTAL+TGOA+PISR+ISR
TDEA=EF-TDS
print("TOTAL DE SALIDAS|      |",(TDS))
print("FLUJO DE EFECTIVO ACTUAL|    |",(TDEA))
print("-"*100)


print("Balance General")
print("Activo")
print("CIRCULANTE")
print("Efectivo",(TDEA),"|")
print("Clientes",(SCF),"|")
print("Inventario de Materiales",(TOT),"|")
print("Inventario de Producto Terminado",(TO),"|")
tac=TDEA+SCF+TOT+TO
print("Ttotal de Activos Circulantes|       |",(tac))
ter=int(input("Terreno:"))
pye=int(input("Planta y Equipo:"))
dpaa=int(input("Depreciacion acumulada"))
print("NO CIRCULANTE")
print("Terreno|",(ter),"|")
print("Planta y equipo|",(pye),"|")
print("Depreciacion acumulada|",(dpaa),"|")
TANC=ter+pye+dpaa
print("TOTAL ACTIVOS NO CIRCULANTES|    |",(TANC))
print("ACTIVO TOTAL|     |",(TANC))
DxP=int(input("Documentos por pagar"))
print("PASIVO")
print("CORTO PLAZO")
print("Proveedores|",(SPF),"|")
print("Doc x pagar|",(DxP),"|")
print("ISR x pagar|",(ISR),"|")
print(("PTU x pagar|",(PTU),"|"))
TPCP=SPF+DxP+ISR+PTU
print("TOTAL DE PASIVO CORTO PLAZO|         |",(TPCP))
print("LARGO PLAZO")
OXP=int(input("Obligacaiones x pagar"))
print("Obligaciones x pagar|",(OXP))
print("TOTAL DE PASIVO LARGO PLAZO|       |",(OXP))
PTTT1=TPCP+OXP
print("PASIVO TOTAL|         |",(PTTT1))
print("CAPITAL CONTABLE")
CA=int(input("Capital aportado:"))
CG=int(input("Capital ganado:"))
print("Capital Aportado|",(CA),"|")
print("Capital Ganado|",(CG),"|")
print("Utilidad|",(UN),"|")
TCC1=CA+CG+UN
SPYC=PTTT1+TCC1
print("TOTAL CAPITAL CONTABLE|     |",(TCC1))
print("SUMA DE PASIVO Y CAPITAL|   |",(SPYC))