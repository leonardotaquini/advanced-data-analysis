import mysql.connector


def connect_to_db():
    # Configuración de la conexión
    config = {
        'user': 'root',         
        'password': '',   
        'host': 'localhost',        
        'database': 'companydata'  
    }

    # Conectar a la base de datos
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM employeeperformance"
            cursor.execute(query)

            results = cursor.fetchall()

            return results

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")
