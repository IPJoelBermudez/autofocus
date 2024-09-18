
# Autoenfoque de Cámaras

Este script está diseñado para realizar un autoenfoque en cámaras a horas específicas. 

## Descripción

El script envía comandos a la cámara para ajustar el enfoque en horarios programados. Asegúrate de que las cámaras estén bien iluminadas para obtener resultados óptimos, ya que el enfoque puede no funcionar correctamente en condiciones de poca luz o durante la noche.

## Configuración

1. **Edita el archivo `credentials.json`:**

   Crea o modifica el archivo `credentials.json` en el mismo directorio que el script. El archivo debe tener el siguiente formato:

   ```json
   {
     "lpr": {
       "user": "tu_usuario",
       "password": "tu_contraseña",
       "ip": "direccion_ip_de_la_camara",
       "Horas de enfoque": ["06:01", "10:36", "15:01", "18:01"]
     }
   }
   ```

   - **user**: Usuario para la autenticación de la cámara.
   - **password**: Contraseña para la autenticación de la cámara.
   - **ip**: Dirección IP de la cámara.
   - **Horas de enfoque**: Lista de horas en formato de 24 horas para realizar el autoenfoque.

2. **Asegúrate de que la cámara tenga habilitada la autenticación `digest/basic`:**

   Configura la cámara para que use el modo de autenticación `digest/basic` para que el script funcione correctamente.

## Notas Importantes

- **Evita ejecutar el script en cámaras ubicadas en áreas con poca luz o durante la noche.**
  La cámara realiza un ajuste del lente para enfocar, y si está en completa oscuridad, puede que el enfoque no sea preciso.

## Requisitos

- Python 3.x
- Librerías Python:
  - `requests`
  - `schedule`
  - `json` (incluida en la biblioteca estándar de Python)

   Puedes instalar las librerías necesarias usando pip:

   ```bash
   pip install requests schedule
   ```

## Uso

Ejecuta el script con Python:

```bash
sudo python3 autoFocus.py
```

El script se mantendrá en ejecución y realizará el enfoque en las horas programadas.
