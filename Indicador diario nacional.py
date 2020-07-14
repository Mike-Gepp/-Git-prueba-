<saw:report xmlns:saw="com.siebel.analytics.web/report/v1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:sawx="com.siebel.analytics.web/expression/v1.1" xmlVersion="201201160">      
   <saw:criteria xsi:type="saw:simpleCriteria" subjectArea="&quot;Mesa_Servicio&quot;" withinHierarchy="true">            
      <saw:columns>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c6227ced8c271fd93">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."INCIDENT_NUMBER"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="center" vAlign="top" width="30" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>FOLIO</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c89b4ad441eae8d76">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."CREATION_DATE"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" width="138" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>F. CREACION</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="ccb617f95e71d062c">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."USER_NAME"</sawx:expr></saw:columnFormula>            
            <saw:tableHeading/>            
            <saw:columnHeading/></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c451620f27cd59bb0">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."CLAVE_UOP"</sawx:expr></saw:columnFormula></saw:column>         
         <saw:column xsi:type="saw:regularColumn" columnID="c5df1b0c5d3e84ea0">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"CDS_Hora_Solucion"."HORA_FIN"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="center" vAlign="top" width="84" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>CDS_Hora_Solucion</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat>               
               <saw:caption fmt="text">                  
                  <saw:text>HORA FIN</saw:text></saw:caption></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c839b8a80bfc4d46f">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"CDS_Hora_Solucion"."FECHA_FIN"</sawx:expr></saw:columnFormula>            
            <saw:tableHeading/>            
            <saw:columnHeading/></saw:column>                  
         <saw:column columnID="cbcb3831310524bba" xsi:type="saw:regularColumn">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60</sawx:expr></saw:columnFormula>                        
            <saw:displayFormat>               
               <saw:formatSpec suppress="repeat" vAlign="top" width="59" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>                        
            <saw:columnHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>TIEMPO</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column columnID="c7b2eb00571c15721" xsi:type="saw:regularColumn">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)</sawx:expr></saw:columnFormula>                        
            <saw:tableHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>CDS_Hora_Solucion</saw:text></saw:caption></saw:tableHeading>                        
            <saw:columnHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>DIAS</saw:text></saw:caption></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="ce846ec78cb8a24da">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."NEW_VALUE"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="109" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>ESTATUS</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c911c39f9c5fbb237">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."NAME" LIKE  '% SIO %' THEN 'SIO' ELSE  CASE WHEN "BS_REPORTE_PAROS"."NAME" LIKE  '% MSIO %' THEN 'MSIO' ELSE CASE WHEN "BS_REPORTE_PAROS"."NAME" LIKE  '%Monitoreo%' THEN 'MON' ELSE CASE WHEN "BS_REPORTE_PAROS"."NAME" =  'TI MST Hand Held' THEN 'HHC' ELSE CASE WHEN "BS_REPORTE_PAROS"."NAME" =  'TI MST Smartphone' THEN 'SMRT' ELSE "BS_REPORTE_PAROS"."NAME" END END END END END</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="59" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>TIPO</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c931768c006dc6d12">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">SUBSTRING("BS_REPORTE_PAROS"."PROBLEM_CODE" FROM POSITION('|' IN "BS_REPORTE_PAROS"."PROBLEM_CODE") + 1)
</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="109" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>PROBLEMA</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c7d2b0e2ec03d405d">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."UOP"</sawx:expr></saw:columnFormula>            
            <saw:tableHeading/>            
            <saw:columnHeading/></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c2eec68b30a85f4cd">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."REGION"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat/>            
            <saw:tableHeading/>            
            <saw:columnHeading>               
               <saw:displayFormat/></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="c5a894e765008b8b9">            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat>                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."SERVICIO"</sawx:expr></saw:columnFormula>            
            <saw:tableHeading/>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="cacd4701fa0cf2c2a">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."TIEMPO"</sawx:expr></saw:columnFormula></saw:column>                  
         <saw:column xsi:type="saw:regularColumn" columnID="cee7d5910641d0ec9">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."EMPLOYEE_LOCATION"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="134" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat>               
               <saw:caption fmt="text">                  
                  <saw:text>LOCALIDAD</saw:text></saw:caption></saw:columnHeading></saw:column>                  
         <saw:column columnID="cf97aa24603538a62" xsi:type="saw:regularColumn">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('01-MON-INT-DWH|Interface - DWH','02-MON-INT-GL|Interface - GL','03-MON-INT-FAC|Interface - FAC','04-MON-INT-FAL|Interface - FAL','05-MON-INT-AR|Interface - AR','06-MON-MSIO-RQ|RQ No Procesados','07-MON-MSIO-PED|Pedidos No Procesados','08-MON-MSIO-CUS|Replicacion de Clientes','09-MON-OPM-CMI|Codigo de Motivo Incorrecto','10-MON-OPM-ID|Interface Descuadrada','11-MON-OPM-FF|Fechas Futuras','12-MON-OPM-SNA|SKU No Asignado','13-MON-DSD-ALR|DSD Alertas','14-MON-TLC-ENL|Enlace','15-MON-BKP-RSR|Restauracion de Respaldos','16-MON-LIQ-CRR|Cierre de Liquidaciones','17-MON-BDS-ERR|Error Base de Datos','18-MON-APT-CRR|Cierre de APT') THEN 'EVENTO' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('011804-DESBUSRS|Desbloqueo De Usuario','011805-RESETPWD|Reseteo Contraseña','011806-HABIUSRS|Habilitar Usuario','011201-RESETCTA|Reseteo De Cuenta','011202-DESBLOQ|Desbloqueo','010203-ABC_USRS|Alta Usuarios') THEN 'ACCESOS' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('011101-CARGACTE|Carga De Clientes Tlv','012501-ASIGNADI|Asignacion Duplicada','012402-REACTEMP|Reactivacion Temporal','010708-CONFCELD|Configuracion De Celdas','010711-APEDIDOS|Apertura De Ajuste De Pedidos','010712-CAMFECHA|Cambio Fecha De Pedido','010802-APERTDIA|Apertura De Dia','011102-CONFDESC|Configuracion De Descuentos','011001-INACDESC|Inactivacion De Descuentos','011002-ACTDESCU|Activacion De Descuentos','011003-LISTAPRE|Lista De Precios','010204-CONFRUTA|Configuracion Masiva De Rutas','011603-CATALOGO|Catalogos','011604-DEPTRANS|Depuracion Transferencias','010803-FRECUENC|Frecuencias','012601-DEPSALDO|Depuracion Y Traspaso De Saldo','012001-BAJACDG|Baja Cdg','010601-CONFIG|Actualizacion De Ambiente') THEN 'CAMBIOS' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('010801-CIERRE|Cierre De Dia') THEN 'ERROR CONOCIDO' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('011303-GENREPOR|Generacion De Reportes') THEN 'INFORMACION' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('012401-TIPOMERC|Asignacion Tipo De Mercado','012201-REGENDWH|Regeneración Dwh','011801-DESCUSRS|Desconexion De Usuarios','012202-REGENPOL|Regeneración Poliza','010201-SYNCCTES|Sincronizacion Clientes','010202-SYNC_VTA|Sincronizacion Venta') THEN 'PETICION' ELSE CASE WHEN "BS_REPORTE_PAROS"."PROBLEM_CODE" IN ('010501-CARGDISP|Carga Dispositivo','010501-DOWNLOAD|Descarga Dispositivo','012701-CARGDISP|Carga Dispositivo','012704-DESCDISP|Descarga Dispositivo','010301-REDLOC|Red Local','010302-ENLACE|Enlace','011802-ALTABD|Alta Bd','011803-SINACCES|Sin Acceso','011702-CUPONES|Cierre De Cupones','010702-CARGASOL|Carga De Soluciones','010704-CONFGSKU|Sku Sin Impuesto','010705-SKUINACT|Sku Inactivo','010706-DESCELDA|Desarmado De Celda','010707-ARMDOPAR|Armado Parcial','010709-CUPONES|Cierre De Cupones','010710-SCONFCOM|Sin Configuración Completa','010502-INICDIA|Inicio De Dia','010501-FECOPERA|Fecha Incorrecta','012702-INICIODI|Inicio De Dia','012705-FECHINCO|Fecha Incorrecta','011301-FACTURAR|Facturacion Ar','012305-RTSNMOVI|Ruta Sin Movimientos','012306-RTDESCUA|Ruta Descuadrada','012307-FOLIOUNI|Folio Unico','012310-REFBANC|Referencias Bancarias','012311-CHKDUPLI|Cheques Duplicados','012312-CREDSNFO|Creditos Sin Folio Factura','012313-COBRENVA|Cobro De Envase','012101-ARMADO|Armado Automatico','012102-CUPONSAL|Cupón De Salida','011701-GENINTER|Generación De Interface','011703-CMOVIMIE|Captura De Movimientos','012403-LISTAPRE|Lista De Precios','012404-IMPUESTO|Impuestos','011901-ERROAPLI|Errores De Aplicacion','010701-REPLINFO|Replicacion Informacion Ruta','010703-NORUTENT|No Se Muestra Ruta De Entrega','010503-INCMERCA|Incidencia En Mercado','010501-PLANIFIC|Planificadores','010501-LOGINUSR|Inicio De Sesion','012703-INCMERCA|Incidencia En Mercado','012706-INICIOSE|Inicio De Sesión','012707-FALLDISP|Falla De Dispositivo','012708-MENSAJES|Mensajeria','012301-APLDESCU|Aplicacion De Descuentos','012302-BONIFICA|Bonificaciones','012303-CREDITOS|Aplicacion De Creditos','012304-LIQUIDRT|Liquidación De Ruta','012308-CIERRELQ|Cierre Del Dia','011902-ERRORCOM|Errores De Compilacion','011903-ERRORMOD|Errores En Modulos','011602-COMODATO|Comodatos','010901-LENTITUD|Lentitud','011302-FACTURCO|Facturacion Contado','012309-CARGYABO|Cargos Y Abonos','011601-TRANSACT|Transferencia De Activos') THEN 'INCIDENCIA' ELSE "BS_REPORTE_PAROS"."PROBLEM_CODE" END END END END END END END</sawx:expr></saw:columnFormula>                        
            <saw:displayFormat/>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>                        
            <saw:columnHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>TIPO</saw:text></saw:caption>               
               <saw:displayFormat/></saw:columnHeading></saw:column>                  
         <saw:column columnID="c6f580749de79bf19" xsi:type="saw:regularColumn">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."USER_NAME" = 'ORACLE' THEN 'PORTAL' ELSE 'DIRECTO' END</sawx:expr></saw:columnFormula>                        
            <saw:displayFormat/>            
            <saw:tableHeading/>                        
            <saw:columnHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>ORIGEN</saw:text></saw:caption>               
               <saw:displayFormat/></saw:columnHeading></saw:column>                  
         <saw:column columnID="c9223312e9b92658e" xsi:type="saw:regularColumn">                        
            <saw:columnFormula>                              
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."USER_NAME" IN ('ORACLE', '426620', '50093313', '50134403', '50134404', '50134405', '50139581', '50160956', '50232252', 'EASALASR', 'VMMORONESS','50243928', '50244307') THEN 'MAT' ELSE CASE WHEN "BS_REPORTE_PAROS"."USER_NAME" IN ('50152043', '50178187', '50138271', 'JADURANP') THEN 'MON' ELSE 'JTI' END END</sawx:expr></saw:columnFormula>                        
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="24" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>                        
            <saw:columnHeading>                              
               <saw:caption fmt="text">                                    
                  <saw:text>EQ</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>         
         <saw:column columnID="cfe8874d129fde890" xsi:type="saw:regularColumn">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Excelente' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Excelente' THEN 'Excelente' ELSE 
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Excelente' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Bueno' THEN 'Bueno' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Excelente' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Regular' THEN 'Bueno' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Excelente' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Malo' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Bueno' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Excelente' THEN 'Bueno' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Bueno' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Bueno' THEN 'Bueno' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Bueno' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Regular' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Bueno' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Malo' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Regular' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Excelente' THEN 'Bueno' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Regular' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Bueno' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Regular' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Regular' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Regular' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Malo' THEN 'Malo' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Malo' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Excelente' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Malo' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Bueno' THEN 'Regular' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Malo' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Regular' THEN 'Malo' ELSE
CASE WHEN "BS_REPORTE_PAROS"."SERVICIO" = 'Malo' AND "BS_REPORTE_PAROS"."TIEMPO" = 'Malo' THEN 'Malo' ELSE 'S/E' END END END END END END END END END END END END END END END END</sawx:expr></saw:columnFormula>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>ENCUESTA</saw:text></saw:caption></saw:columnHeading></saw:column>         
         <saw:column columnID="c167362146cd2e2ec" xsi:type="saw:regularColumn">            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" wrapText="true" borderPosition="none">                  
                  <saw:dataFormat xsi:type="saw:date" predefinedFormat="dddd, dd&quot; de &quot;MMMM&quot; de &quot;yyyy"/></saw:formatSpec></saw:displayFormat>            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 0 AND 5  THEN ' &lt; 5 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 6 AND 14 THEN ' &gt; 5 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 15 AND 29 THEN '&gt; 15 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 30 AND 44 THEN '&gt; 30 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 45 AND 59 THEN '&gt; 45 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) BETWEEN 60 AND 70 THEN '&gt; 60 min' ELSE
CASE WHEN ("CDS_Hora_Solucion"."FECHA_FIN" - CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE)) &lt; 1 AND  ROUND(("BS_REPORTE_PAROS"."TIEMPO_SOLUCION" * 60),0) IS NULL THEN '' ELSE '&gt; 70 min'  END END END END END END END</sawx:expr></saw:columnFormula>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>CDS_Hora_Solucion</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>RANGO</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>         
         <saw:column columnID="c4c77f4268e4edd17" xsi:type="saw:regularColumn">            
            <saw:displayFormat>               
               <saw:formatSpec suppress="repeat" wrapText="true"/></saw:displayFormat>            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">COUNT(*)</sawx:expr></saw:columnFormula>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>COUNT(*)</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>TOTAL</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>         
         <saw:column xsi:type="saw:regularColumn" columnID="c2b878195c0fca52c">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."SUMMARY"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="repeat" wrapText="true" hAlign="left" vAlign="top" width="345"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat>               
               <saw:caption fmt="text">                  
                  <saw:text>DESCRIPCION</saw:text></saw:caption></saw:columnHeading></saw:column>         
         <saw:column columnID="c6a089ee33897c250" xsi:type="saw:regularColumn">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 0	THEN '00:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 1	THEN '01:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 2	THEN '02:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 3	THEN '03:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 4	THEN '04:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 5	THEN '05:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 6	THEN '06:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 7	THEN '07:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 8	THEN '08:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 9	THEN '09:00' ELSE 
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 10	THEN '10:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 11	THEN '11:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 12	THEN '12:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 13	THEN '13:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 14	THEN '14:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 15	THEN '15:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 16	THEN '16:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 17	THEN '17:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 18	THEN '18:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 19	THEN '19:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 20	THEN '20:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 21	THEN '21:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 22	THEN '22:00' ELSE
CASE WHEN HOUR("BS_REPORTE_PAROS"."CREATION_DATE") = 23	THEN '23:00' ELSE '' END END END END END END END END END END END END END END END END END END END END END END END END</sawx:expr></saw:columnFormula>            
            <saw:tableHeading/>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>HORARIO</saw:text></saw:caption></saw:columnHeading></saw:column>         
         <saw:column xsi:type="saw:regularColumn" columnID="cddb88c1d3363708b">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."EMAIL_ADDRESS"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" hAlign="left" vAlign="top" width="109" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat>               
               <saw:caption fmt="text">                  
                  <saw:text>CORREO</saw:text></saw:caption></saw:columnHeading></saw:column>         
         <saw:column xsi:type="saw:regularColumn" columnID="ca9bda4aafa33c567">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_FECHA"."TI_FECHA"</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" borderPosition="none" wrapText="true" fontStyle="bold">                  
                  <saw:dataFormat xsi:type="saw:date" predefinedFormat="dddd, dd&quot; de &quot;MMMM&quot; de &quot;yyyy"/></saw:formatSpec></saw:displayFormat>            
            <saw:columnHeading>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column>         
         <saw:column columnID="c1fab0c1bd0ba3304" xsi:type="saw:regularColumn">            
            <saw:columnFormula>               
               <sawx:expr xsi:type="sawx:sqlExpression">CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4056,4064,4061,3052,4063,4064,4065,4066,4067,4068,4063,3052) THEN 'GUERRERO' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4057,4053,4054,4057,4053,4060,4058,4059,4060,4058) THEN 'MORELOS' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4109,4073,4080,4071,4072,4074,4075,4077,4078,4079) THEN 'OAXACA' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4070,4070,4103,4105,4110,4111,4103,4104,4110) THEN 'PUEBLA' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4050,4107,4113,4116,4112,4115,4117,4118,4107,4117,4116,4106) THEN 'TLAXCALA' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4069,4092,4090,4093,4095,4096,4090,4093,4069,4096,4095) THEN 'VERACRUZ CENTRO' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4119,4082,4086,4087,4088,4089,4119,4082,4086,4081) THEN 'VERACRUZ PUERTO' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (4085,4097,4084,4091,4098,4100,4101,4102,4098,4099,4100,4084,4101) THEN 'VERACRUZ SUR' ELSE          CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3061,3061,3058,3058,3059,3055,3055,3074,3074,3077,3077,3078,3078)  THEN 'AGUASCALIENTES' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3053, 3053, 3054) THEN 'BAJIO' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3057,3057,3105,3105,3106,3106,3107,3107,3108,3108,3109,3109,3112,3112,3113,3113,3144) THEN 'CELAYA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3080,3080,3082,3082,3084,3127,3127,3128,3128,3139,3139,3130,3130) THEN 'COLIMA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3068,3068,3076,3076,3120,3120,3123,3123,3124,3124,3125,3125,3065) THEN 'GUADALAJARA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3066,3066,3067,3067,3072,3072,3079,3079,3086,3086) THEN 'JALISCO ORIENTE' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3069,3069,3071,3071,3073,3073,3081,3081,3083,3083,3085,3085) THEN 'JALISCO PONIENTE' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3090,3091,3091,3092,3092,3093,3093,3097,3097,3098,3098,3099,3099,3101,3101,3089) THEN 'MORELIA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3063,3131,3131,3133,3133,3134,3134,3135,3135,3136,3138,3138) THEN 'TEPIC' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (3100,3100,3102,3102,3103,3103,3115,3115,3116,3116,3117,3117,3118,3118,3119,3119,3121,3121) THEN 'URUAPAN' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (6098,6094,6095,6097,6094) THEN 'BCS' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (6073,6071,6072,6072,6067,6063,6068,6065,6064,6070,6066,6069) THEN 'CHIHUAHUA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (0740,0743,0726) THEN 'DAS BCS' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (479,0479,0594,591) THEN 'DAS CHIHUAHUA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (750) THEN 'DAS SONORA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (6074,6100,6075,6076,6077) THEN 'MEXICALI' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (6089,6090,6091,6092,6093) THEN 'SINALOA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (6080,6080,6084,6082,6087,6081,6083,6085,6086) THEN 'SONORA' ELSE     CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (2052,2053,2054,2054,2056,2055,2055,2058,2059) THEN 'CANCUN' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (2057,2057,2060,2062,2064,2065,2069,2072,2072,2063,2063) THEN 'MERIDA' ELSE     CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (2074,2075,2086,2087,2088,2089,2090,2076) THEN 'TAPACHULA' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (2077,2078,2079,2080,2081,2081,2082,2083,2084,2085,2096) THEN 'TUXTLA' ELSE     CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (2066,2066,2068,2091,2091,2092,2092,2093,2093,2099) THEN 'VILLAHERMOSA' ELSE        CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5097,5092,5093,5099,5098,5094,5096,5091,5091) THEN 'COAHUILA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (479,5094,513,508,509,5093) THEN 'DAS COAHUILA' ELSE    CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (566,0565,0566,0573,5117) THEN 'DAS DURANGO' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (495) THEN 'DAS FRONTERA' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (0542) THEN 'DAS GOLFO' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5079) THEN 'DAS MONTERREY' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5063,5064) THEN 'DAS SLP-ZAC' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5072,5121,5116,5120,5119,5117,5122,5122,5123,5121) THEN 'DURANGO' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5090,5086,5089,5085,5087,5084,5088) THEN 'FRONTERA' ELSE      CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5103,5112,5113,5104,5111,5101,5114,5114,5102) THEN 'GOLFO' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5105,5106,5109,5110,5107,5108) THEN 'HUASTECA' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5082,5082,5079,5080,5077,5077,5079,5078,5078,5076,5076,5127,5127) THEN 'MONTERREY' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5067,5067,5063,5064,5066,5068,5060,5062,5069,5061) THEN 'SAN LUIS POTOSI' ELSE       CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (5071,5073,5073,5070,5070,5074) THEN 'ZACATECAS' ELSE        CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1064,1064,1069,1065,1068,1090,1090,1089) THEN 'HIDALGO' ELSE        CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1070, 1057, 1055, 1088 ) THEN 'MM-PTE' ELSE         CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1076, 1072, 1507, 1502 ) THEN 'NORTE' ELSE           CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1060, 1063, 1052 ) THEN 'ORIENTE' ELSE            CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1504, 1503 ) THEN 'ORIENTE 1' ELSE             CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1505, 1506 ) THEN 'ORIENTE 2' ELSE             CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1510, 1512, 1512 ) THEN 'PONIENTE' ELSE             CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1085, 1085, 1086, 1086, 1087 ) THEN 'QUERETARO' ELSE              CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1059, 1053  ) THEN 'SUR'ELSE               CASE WHEN "BS_REPORTE_PAROS"."CLAVE_UOP" IN (1084, 1084, 1081, 1081, 1080, 1082, 3096 ) THEN 'TOLUCA '              END END END END END END END END END END           END END END END END END END END END END           END END END END END END END END END END           END END END END END END END END END END           END END END END END END END END END END           END END END END END</sawx:expr></saw:columnFormula>            
            <saw:displayFormat>               
               <saw:formatSpec suppress="suppress" wrapText="true"/></saw:displayFormat>            
            <saw:tableHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>BS_REPORTE_PAROS</saw:text></saw:caption></saw:tableHeading>            
            <saw:columnHeading>               
               <saw:caption fmt="text">                  
                  <saw:text>ZONA</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:columnHeading></saw:column></saw:columns>            
      <saw:filter>                  
         <sawx:expr xsi:type="sawx:logical" op="and">                                    
            <sawx:expr xsi:type="sawx:comparison" op="equal">                              
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."ULTIMO_REG"</sawx:expr>                              
               <sawx:expr xsi:type="xsd:decimal">1</sawx:expr></sawx:expr>                        
            <sawx:expr xsi:type="sawx:sql">CAST("BS_REPORTE_PAROS"."CREATION_DATE" AS DATE) =  CURRENT_DATE - 1</sawx:expr>            
            <sawx:expr xsi:type="sawx:comparison" op="equal">               
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."FIELD"</sawx:expr>               
               <sawx:expr xsi:type="xsd:string">Estado</sawx:expr></sawx:expr>            
            <sawx:expr xsi:type="sawx:sql">"BS_REPORTE_PAROS"."NAME" IN ('TI MST Hand Held','TI MST Smartphone','TI MST Business Mail','TI MST Ediwin','TI MST Pac','TI MST Signature','TI MST Comunicaciones','TI MST SIO Liquidaciones','TI MST SIO Base De Datos','TI MST SIO Rh','TI MST SIO Despacho','TI MST SIO Apt','TI MST SIO Productos','TI MST SIO Interfaces','TI MST SIO Bitacoras Y Parches','TI MST SIO Saldos','TI MST SIO Adc','TI MST SIO Clientes','TI MST MSIO Despacho','TI MST MSIO Fecha Operación','TI MST MSIO Televenta','TI MST MSIO Precios Y Descuentos','TI MST MSIO Usuarios','TI MST MSIO Performance','TI MST MSIO Configuracion','TI MST Cas','TI MST Pepsi Si','TI MST Monitoreo')
</sawx:expr>            
            <sawx:expr xsi:type="sawx:list" op="in">
               <sawx:expr xsi:type="sawx:sqlExpression">"BS_REPORTE_PAROS"."REGION"</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Metro Embotellado</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Metro Garrafón</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Centro</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Garc-Crespo</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Norte</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Occidente</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Pacifico</sawx:expr>
               <sawx:expr xsi:type="xsd:string">Region Sur</sawx:expr></sawx:expr></sawx:expr></saw:filter></saw:criteria>      
   <saw:views currentView="0">            
      <saw:view xsi:type="saw:compoundView" name="compoundView!1">                  
         <saw:cvTable>
            <saw:cvRow>
               <saw:cvCell viewName="titleView!1" colSpan="4">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec borderPosition="none" width="1200px" hAlign="center"/></saw:displayFormat></saw:cvCell></saw:cvRow>
            <saw:cvRow>
               <saw:cvCell viewName="tableView!3" colSpan="4">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="right" paddingTop="2"/></saw:displayFormat></saw:cvCell></saw:cvRow>
            <saw:cvRow>
               <saw:cvCell viewName="dvtchart!1">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="dvtchart!6">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec borderPosition="all" width="400px" hAlign="center" vAlign="middle"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="dvtchart!3" colSpan="2">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell></saw:cvRow>
            <saw:cvRow>
               <saw:cvCell viewName="dvtchart!4">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="dvtchart!8">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="dvtchart!7" colSpan="2">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell></saw:cvRow>
            <saw:cvRow>
               <saw:cvCell viewName="dvtchart!5">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="dvtchart!2" colSpan="2">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" vAlign="middle" borderPosition="all" width="400px"/></saw:displayFormat></saw:cvCell>
               <saw:cvCell viewName="pivotTableView!1">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" width="400px" vAlign="middle"/></saw:displayFormat></saw:cvCell></saw:cvRow>
            <saw:cvRow>
               <saw:cvCell viewName="tableView!1" colSpan="4">                  
                  <saw:displayFormat>                     
                     <saw:formatSpec hAlign="center" width="1200px" vAlign="middle"/></saw:displayFormat></saw:cvCell></saw:cvRow></saw:cvTable></saw:view>            
      <saw:view xsi:type="saw:titleView" name="titleView!1" includeName="false" startedDisplay="none" logoUrl="cmap:/shared/custom/images/banner.jpg">         
         <saw:logoFormat>            
            <saw:displayFormat>               
               <saw:formatSpec borderPosition="none" wrapText="true" width="1200"/></saw:displayFormat></saw:logoFormat></saw:view>            
      <saw:view xsi:type="saw:tableView" name="tableView!1" scrollingEnabled="true" width="1200" repeat="false">                  
         <saw:edges>            
            <saw:edge axis="page" showColumnHeader="true"/>            
            <saw:edge axis="section">                                             
               <saw:edgeLayers>                  
                  <saw:edgeLayer type="column" columnID="c1fab0c1bd0ba3304">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontSize="18" wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c4c77f4268e4edd17" insertPageBreak="false">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontSize="18" wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:edgeLayer></saw:edgeLayers></saw:edge>            
            <saw:edge axis="row" showColumnHeader="true">                              
               <saw:columnOrder>                  
                  <saw:columnOrderRef columnID="c89b4ad441eae8d76" direction="ascending"/></saw:columnOrder>               
               <saw:edgeLayers>                  
                  <saw:edgeLayer type="column" columnID="c89b4ad441eae8d76">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="cee7d5910641d0ec9">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c6227ced8c271fd93">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c911c39f9c5fbb237">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c931768c006dc6d12">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c2b878195c0fca52c">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="ce846ec78cb8a24da">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c5df1b0c5d3e84ea0">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="cbcb3831310524bba">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="cddb88c1d3363708b">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer>                  
                  <saw:edgeLayer type="column" columnID="c9223312e9b92658e">                     
                     <saw:headerFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:headerFormat></saw:edgeLayer></saw:edgeLayers></saw:edge>            
            <saw:edge axis="column" showColumnHeader="rollover"/></saw:edges></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!1">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>% SOLUCION</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:title>            
            <saw:border/></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>                  
                  <saw:columnRef columnID="ce846ec78cb8a24da"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true">            
            <saw:textFormat/></saw:legendFormat>         
         <saw:seriesFormats>
            <saw:seriesFormatGroup name="pie">
               <saw:seriesFormatRule>
                  <saw:seriesCondition position="2"/>
                  <saw:visualFormats>
                     <saw:visualFormat explodeWedge="true"/></saw:visualFormats></saw:seriesFormatRule></saw:seriesFormatGroup></saw:seriesFormats></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!2">         
         <saw:display type="bar" subtype="basic" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>SOLICITUDES POR ZONA</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:category>
                  <saw:columnRef columnID="c1fab0c1bd0ba3304"/></saw:category></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="y">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:measureLabels/></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="none" transparentFill="true"/>         
         <saw:axesFormats>            
            <saw:axisFormat axis="X">               
               <saw:title mode="custom"/></saw:axisFormat></saw:axesFormats></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!3">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>EQUIPO DE RESOLUTOR</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>                  
                  <saw:columnRef columnID="c9223312e9b92658e"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true">            
            <saw:textFormat/></saw:legendFormat></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!4">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>% POR TIEMPO DE SERVICIO</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>                  
                  <saw:columnRef columnID="c167362146cd2e2ec"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true"/>         
         <saw:seriesFormats>            
            <saw:seriesFormatGroup name="pie">               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="1"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="2"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="3"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="4"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="5"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="6"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat explodeWedge="true"/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="7"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule></saw:seriesFormatGroup></saw:seriesFormats></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!5">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>SOLICITUDES POR REGIÓN</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>
                  <saw:columnRef columnID="c2eec68b30a85f4cd"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true"/></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!6">         
         <saw:display type="bar" subtype="basic" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="default" label="default" position="below" transparentBackground="true" valueAs="default"/>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>SOLICITUDES POR HORA</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:category>                  
                  <saw:columnRef columnID="c6a089ee33897c250"/></saw:category></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="y">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:measureLabels/></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="none" transparentFill="true"/>         
         <saw:axesFormats>            
            <saw:axisFormat axis="X" displayScaleLabels="true">               
               <saw:title mode="auto">                  
                  <saw:caption/>                  
                  <saw:displayFormat>                     
                     <saw:formatSpec/></saw:displayFormat></saw:title>               
               <saw:labels rotate="90" rotateLabels="true" skipLabels="true" abbreviation="default"/>               
               <saw:textFormat/></saw:axisFormat></saw:axesFormats></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!7">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption>                  
                  <saw:text>GPO SOLICITUD</saw:text></saw:caption></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>                  
                  <saw:columnRef columnID="c911c39f9c5fbb237"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true"/></saw:view>      
      <saw:view xsi:type="saw:dvtchart" name="dvtchart!8">         
         <saw:display type="pie" subtype="default" renderFormat="default" mode="online">            
            <saw:style barStyle="default" lineStyle="default" scatterStyle="default" fillStyle="default" bubblePercentSize="100" effect="2d"/></saw:display>         
         <saw:canvasFormat height="330" width="400">            
            <saw:dataLabels display="always" label="default" position="below" transparentBackground="true" valueAs="default" abbreviation="default">               
               <saw:textFormat/></saw:dataLabels>            
            <saw:title mode="custom">               
               <saw:caption truncate="false" truncateLength="0">                  
                  <saw:text>TIPO SOLICIUTD</saw:text></saw:caption>               
               <saw:displayFormat>                  
                  <saw:formatSpec/></saw:displayFormat></saw:title></saw:canvasFormat>         
         <saw:selections>            
            <saw:categories>               
               <saw:measureLabels/></saw:categories>            
            <saw:measures showMeasureLabelsOnCategory="false">               
               <saw:column measureType="pie">                  
                  <saw:columnRef columnID="c4c77f4268e4edd17"/></saw:column></saw:measures>            
            <saw:seriesGenerators>               
               <saw:seriesGenerator>                  
                  <saw:columnRef columnID="cf97aa24603538a62"/></saw:seriesGenerator></saw:seriesGenerators>            
            <saw:page/></saw:selections>         
         <saw:legendFormat position="bottom" transparentFill="true"/>         
         <saw:seriesFormats>            
            <saw:seriesFormatGroup name="pie">               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="1"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat explodeWedge="true"/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="2"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="3"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="4"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="5"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat/></saw:visualFormats></saw:seriesFormatRule>               
               <saw:seriesFormatRule>                  
                  <saw:seriesCondition position="6"/>                  
                  <saw:visualFormats>                     
                     <saw:visualFormat explodeWedge="true"/></saw:visualFormats></saw:seriesFormatRule></saw:seriesFormatGroup></saw:seriesFormats></saw:view>      
      <saw:view xsi:type="saw:tableView" name="tableView!2" scrollingEnabled="true">         
         <saw:edges>            
            <saw:edge axis="page" showColumnHeader="true"/>            
            <saw:edge axis="section"/>            
            <saw:edge axis="row" showColumnHeader="true">               
               <saw:edgeLayers>                  
                  <saw:edgeLayer type="column" columnID="cf97aa24603538a62"/>                  
                  <saw:edgeLayer type="column" columnID="c5a894e765008b8b9"/>                  
                  <saw:edgeLayer type="column" columnID="cacd4701fa0cf2c2a"/>                  
                  <saw:edgeLayer type="column" columnID="cfe8874d129fde890"/>                  
                  <saw:edgeLayer type="column" columnID="c839b8a80bfc4d46f"/>                  
                  <saw:edgeLayer type="column" columnID="c7b2eb00571c15721"/>                  
                  <saw:edgeLayer type="column" columnID="c6f580749de79bf19"/>                  
                  <saw:edgeLayer type="column" columnID="c9223312e9b92658e"/>                  
                  <saw:edgeLayer type="column" columnID="ce846ec78cb8a24da"/>                  
                  <saw:edgeLayer type="column" columnID="c911c39f9c5fbb237"/>                  
                  <saw:edgeLayer type="column" columnID="c167362146cd2e2ec"/>                  
                  <saw:edgeLayer type="column" columnID="c2eec68b30a85f4cd"/>                  
                  <saw:edgeLayer type="column" columnID="ccb617f95e71d062c"/>                  
                  <saw:edgeLayer type="column" columnID="c6a089ee33897c250"/>                  
                  <saw:edgeLayer type="column" columnID="c931768c006dc6d12"/>                  
                  <saw:edgeLayer type="column" columnID="cee7d5910641d0ec9"/>                  
                  <saw:edgeLayer type="column" columnID="c7d2b0e2ec03d405d"/>                  
                  <saw:edgeLayer type="column" columnID="cbcb3831310524bba"/>                  
                  <saw:edgeLayer type="column" columnID="c5df1b0c5d3e84ea0"/>                  
                  <saw:edgeLayer type="column" columnID="c89b4ad441eae8d76"/>                  
                  <saw:edgeLayer type="column" columnID="c2b878195c0fca52c"/>                  
                  <saw:edgeLayer type="column" columnID="c6227ced8c271fd93"/>                  
                  <saw:edgeLayer type="column" columnID="c4c77f4268e4edd17"/></saw:edgeLayers></saw:edge>            
            <saw:edge axis="column" showColumnHeader="rollover"/></saw:edges></saw:view>      
      <saw:view xsi:type="saw:pivotTableView" name="pivotTableView!1" scrollingEnabled="true" width="400">                  
         <saw:edges>
            <saw:edge axis="page" showColumnHeader="true"/>
            <saw:edge axis="section"/>
            <saw:edge axis="row" showColumnHeader="true">               
               <saw:displayGrandTotals>                  
                  <saw:displayGrandTotal id="gt_row" grandTotalPosition="after">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec backgroundColor="#004c97" wrapText="true" fontColor="#FFFFFF"/></saw:displayFormat>                        
                        <saw:caption>                           
                           <saw:text>Total</saw:text></saw:caption></saw:memberFormat>                     
                     <saw:dataBodyFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec backgroundColor="#004c97" wrapText="true" fontColor="#FFFFFF"/></saw:displayFormat></saw:dataBodyFormat></saw:displayGrandTotal></saw:displayGrandTotals>               
               <saw:columnOrder>                  
                  <saw:columnOrderRef columnID="c2eec68b30a85f4cd" direction="descending">                     
                     <saw:QDR>                        
                        <saw:staticMemberGroup specialDimension="grandTotal">                           
                           <saw:members xsi:type="saw:stringMembers">                              
                              <saw:value>gt_column</saw:value></saw:members></saw:staticMemberGroup>                        
                        <saw:staticMemberGroup specialDimension="measure">                           
                           <saw:members xsi:type="saw:stringMembers">                              
                              <saw:value>c4c77f4268e4edd17</saw:value></saw:members></saw:staticMemberGroup></saw:QDR></saw:columnOrderRef>                  
                  <saw:columnOrderRef columnID="c1fab0c1bd0ba3304" direction="descending">                     
                     <saw:QDR>                        
                        <saw:staticMemberGroup specialDimension="grandTotal">                           
                           <saw:members xsi:type="saw:stringMembers">                              
                              <saw:value>gt_column</saw:value></saw:members></saw:staticMemberGroup>                        
                        <saw:staticMemberGroup specialDimension="measure">                           
                           <saw:members xsi:type="saw:stringMembers">                              
                              <saw:value>c4c77f4268e4edd17</saw:value></saw:members></saw:staticMemberGroup></saw:QDR></saw:columnOrderRef></saw:columnOrder>               
               <saw:edgeLayers>
                  <saw:edgeLayer type="column" columnID="c2eec68b30a85f4cd"/></saw:edgeLayers></saw:edge>
            <saw:edge axis="column" showColumnHeader="rollover">               
               <saw:displayGrandTotals>                  
                  <saw:displayGrandTotal id="gt_column" grandTotalPosition="after">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec backgroundColor="#004c97" wrapText="true" fontColor="#FFFFFF"/></saw:displayFormat>                        
                        <saw:caption>                           
                           <saw:text>Total</saw:text></saw:caption></saw:memberFormat></saw:displayGrandTotal></saw:displayGrandTotals>               
               <saw:edgeLayers>
                  <saw:edgeLayer type="column" columnID="ce846ec78cb8a24da">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontColor="#FFFFFF" backgroundColor="#004c97" wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:edgeLayer>
                  <saw:edgeLayer type="measure" visibility="hidden">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:edgeLayer></saw:edgeLayers></saw:edge></saw:edges>
         <saw:measuresList>            
            <saw:measure columnID="c4c77f4268e4edd17">               
               <saw:memberFormat>                  
                  <saw:displayFormat>                     
                     <saw:formatSpec wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:measure></saw:measuresList></saw:view>      
      <saw:view xsi:type="saw:htmlview" name="htmlview!1"/>      
      <saw:view xsi:type="saw:tableView" name="tableView!3" scrollingEnabled="true">         
         <saw:edges>            
            <saw:edge axis="page" showColumnHeader="true"/>            
            <saw:edge axis="section"/>            
            <saw:edge axis="row" showColumnHeader="false">               
               <saw:edgeLayers>                  
                  <saw:edgeLayer type="column" columnID="ca9bda4aafa33c567">                     
                     <saw:memberFormat>                        
                        <saw:displayFormat>                           
                           <saw:formatSpec fontStyle="bold" borderPosition="none" wrapText="true"/></saw:displayFormat></saw:memberFormat></saw:edgeLayer></saw:edgeLayers></saw:edge>            
            <saw:edge axis="column" showColumnHeader="rollover"/></saw:edges></saw:view></saw:views>      
   <saw:prompts scope="report" subjectArea="&quot;Mesa_Servicio&quot;"/></saw:report>