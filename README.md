Este microservicio implementa el dominio de Usuarios siguiendo los pilares de microservicios.

## Pilares 
1. Descomposición por Dominio: Solo gestiona usuarios 
2. Comunicación: API REST con Flask.  
3. Datos Distribuidos: Base de datos SQLite propia.  
4. Despliegue y Operación: Contenerizado con Docker.  
5. Observabilidad y Resiliencia: Logs y configuración externa.

## Estructura

- appsettings.json – Configuración externa
- config.py – Carga el JSON de configuración 
- models.py – Interfaz abstracta
- services.py – Implementación UserService con SQLite 
- user_service.py – API Flask   
- Dockerfile – Contenerización  
- .gitignore – Ignorar archivos sensibles  

## Instalación

```bash
git clone https://github.com/TU_USUARIO/user-service.git
cd user-service
cp appsettings.json.example appsettings.json
# Ajusta SECRET_KEY en appsettings.json
pip install flask
python user_service.py
