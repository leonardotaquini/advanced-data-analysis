# Advanced data analysis.

En el trabajo practico se realiza un análisis de datos utilizando pandas, numpy, matplotlib y seaborn. El código principal obtiene datos de una base de datos, calcula estadísticas descriptivas, analiza correlaciones y genera gráficos visuales.

## Crear la base de datos
1. Crea la base de datos con el nombre companydata.
2. En la raiz del proyecto se deja el archivo .sql para que importes en la base de datos creada.

## Instalar las dependencias


- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Instalar estas librerías usando pip:

```bash
pip install pandas numpy matplotlib seaborn
````


También se ha generado un archivo requirements.txt que incluye todas las dependencias necesarias. Puedes instalar las dependencias desde este archivo usando el siguiente comando:

```bash
pip install -r requirements.txt
````
## Modifica el archivo src/db/db_connection.py
En caso de que tengas usuario y contraseña diferente tenes que modificar las variables correspondientes.

## Ejecutar el script
```bash
py .\src\main.py
````