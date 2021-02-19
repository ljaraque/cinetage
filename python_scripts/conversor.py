import psycopg2
import csv

conector1 = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = '1234',
                dbname = 'dvdrental', 
                port = '5434'
            ) # alternativamente dbname='arriendos'


conector2 = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = '1234',
                dbname = 'xtage2', 
                port = '5434'
            )

def tabla_a_csv(nombre_tabla, conector):
    cursor = conector.cursor()
    cursor.execute("Select * FROM "+nombre_tabla+" LIMIT 0")
    lista_campos = [desc[0] for desc in cursor.description]
    cursor.execute("SELECT * from "+nombre_tabla+";")
    data = cursor.fetchall()
    with open('archivos/'+nombre_tabla+'.csv', 'w') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(lista_campos)
        for fila in data:
            writer.writerow(fila)


def csv_a_tabla(nombre_archivo,
                nombre_tabla,
                campos_origen,
                campos_destino,
                conector):
    cursor = conector.cursor()
    with open('archivos/'+nombre_archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        campos_archivo = next(reader)
        indices_campos = []
        for campo in campos_origen:
            indices_campos.append(campos_archivo.index(campo))
        campos = ""
        for elemento in campos_destino:
            campos+=elemento+","
        campos = campos.rstrip(",")
        for fila in reader:
            valores=""
            for indice in indices_campos:
                if str(fila[indice])!="":
                    valor="'"+str(fila[indice]).strip()+"',"
                else:
                    valor="null,"
                valores+=valor
            valores=valores.rstrip(",")
            query = "INSERT INTO "+nombre_tabla+" ("+campos+") VALUES ("+valores+");"
            print("Ejecutando Query: " + query)
            cursor.execute(query)
            query = "SELECT setval('"+nombre_tabla+"_id_seq', (SELECT MAX(id) FROM "+nombre_tabla+"));"
            cursor.execute(query)
        conector.commit()
        conector.close()




tabla_a_csv('film', conector1)
tabla_a_csv('language', conector1)
tabla_a_csv('category', conector1)
tabla_a_csv('inventory', conector1)
tabla_a_csv('rental', conector1)
tabla_a_csv('actor', conector1)
tabla_a_csv('film_actor', conector1)
tabla_a_csv('film_category', conector1)


# tabla category
#campos_category=['category_id','name','last_update']
#seleccion_campos_category = ['category_id','name','last_update']
#campos_categoria = ['id', 'nombre', 'ultima_actualizacion']
#csv_a_tabla('category.csv', 'servicio_categoria', seleccion_campos_category, campos_categoria, conector2)

# tabla rental
campos_rental = ['rental_id','rental_date','inventory_id','customer_id','return_date','staff_id','last_update']
seleccion_campos_rental = ['rental_id','rental_date','inventory_id','customer_id','return_date','staff_id','last_update']
campos_arriendo = ['id', 'fecha_arriendo', 'temporal', 'id_cliente', 'fecha_devolucion', 'id_empleado', 'ultima_actualizacion']
csv_a_tabla('rental.csv', 'servicio_arriendo', seleccion_campos_rental, campos_arriendo, conector2)