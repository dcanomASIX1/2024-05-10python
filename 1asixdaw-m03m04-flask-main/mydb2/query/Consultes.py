import mydb2.ConexioDB as ee



def mostrar_clientes():
    ee.conexio_BD()
    try:
        print("tus muertos")
        mycursor = ee.mydb.cursor()
        mycursor.execute("SELECT * FROM clientela")
        pagines = mycursor.fetchall()
        clients=[]

        for x in pagines:
            pagines2 = {}
            pagines2['id']=x[0]
            pagines2['nom']=x[1]
            pagines2['cognom1']=x[2]
            pagines2['cognom2']=x[3]
            pagines2['telefon']=x[4]
            clients.append(pagines2)
    except:
        print("Error en la obtencio de dades")
    finally:
        ee.desconecxio()
    return clients

def mostrar_clientes_individual(id):
    ee.conexio_BD()
    try:
        mycursor = ee.mydb.cursor()
        sql="SELECT * FROM clientela WHERE id= %s"
        mycursor.execute(sql, [id])
        pagines = mycursor.fetchall()
        client=[]
        pagines3= {}
        x=pagines[0]
        pagines3['id']=x[0]
        pagines3['nom']=x[1]
        pagines3['cognom1']=x[2]
        pagines3['cognom2']=x[3]
        pagines3['telefon']=x[4]
        client.append(pagines3)
    except:
        print("Error en la seleccio de dades simples")
    finally:
        ee.desconecxio()
    return pagines3
