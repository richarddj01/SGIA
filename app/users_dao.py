from conexion import cn

cursor = cn.cursor()



#users=[]

#for x in usuarios:
#    users[x] = {'nombre':usuarios[x][0],'pass':usuarios[x][1]}

def users_login(usuario,clave):
    '''
    sql = "docentes_login"
    parametros =  (f'{usuario}',f'{clave}')
    resultado = cursor.callproc(sql,parametros)
    '''
    sql = f'CALL docentes_login ("{usuario}","{clave}")'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

def datos_usuarios():
    cadena = "SELECT * FROM usuario"
    cursor.execute(cadena)
    usuarios = cursor.fetchall()
    
    return usuarios

def insertar_usuario(user,password):
    cadena = f"INSERT INTO usuario  VALUES(null,'{user}','{password}')"
    cursor.execute(cadena)
    cn.commit()