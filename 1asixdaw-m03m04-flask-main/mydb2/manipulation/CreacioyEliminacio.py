import mydb2.ConexioDB as aa


def crear_client(url,categoria):
                mycursor = aa.mydb.cursor()
                sql = """INSERT INTO dades_web (url, categoria, date) 
                        VALUES (%s, %s, %s)"""
                mycursor.execute(sql, [url, categoria])
                aa.mydb.commit()
                return  mycursor.rowcount


def crear_client2(dadas):
                aa.conexio_BD()
                try:
                        mycursor=aa.mydb.cursor()
                        nom = dadas['nom']
                        cognom1 = dadas['cognom1']
                        cognom2= dadas['cognom2']
                        telefon = dadas['telefon']
                        sql = """INSERT INTO clientela (nom, cognom1, cognom2, telefon) 
                                        VALUES (%s, %s, %s, %s)"""
                        mycursor.execute(sql, [nom, cognom1,cognom2, telefon])
                        id=mycursor.lastrowid
                        aa.mydb.commit()
                except:
                        print("error en la insercio de dades")
                finally:
                        aa.desconecxio()
                return id
                
                

def eliminar_pagina():
                            mycursor = aa.mydb.cursor()
                            sql = "DELETE FROM dades_web WHERE id = %s"
                            mycursor.execute(sql, [id])
                            aa.mydb.commit()
                            print("Pàgina eliminada")


def eliminar_pagina2(id):
                aa.conexio_BD()
                try:
                        mycursor = aa.mydb.cursor()
                        sql = "DELETE FROM clientela WHERE id = %s"
                        mycursor.execute(sql, [id])
                        aa.mydb.commit()
                except:
                        print("Error en la eliminacio")
                finally:
                        aa.desconecxio()



def Actualitzacio(data,id):
                aa.conexio_BD()
                try:
                        mycursor = aa.mydb.cursor()
                        sql = "UPDATE clientela SET nom = %s,cognom1 = %s ,cognom2 = %s,telefon = %s WHERE id = %s"
                        mycursor.execute(sql, [data['nom'],data['cognom1'],data['cognom2'],data['telefon'], id])
                        aa.mydb.commit()
                        print("Pàgina eliminada")
                except:
                        print("Error en la modificacio d'usuaris")
                finally:
                        aa.desconecxio()
        
