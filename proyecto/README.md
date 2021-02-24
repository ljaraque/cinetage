# Proyecto CINETAGE/XTAGE21

## Introducción:  
Este repositorio contiene el avance actual de desarrollo de CINETAGE/XTAGE21.  

## Detalles:  
1. La aplicación `panel` contiene la definicion de usuario personalizado heredando desde `AbstractUser` de Django.  
1. Se implementan roles: `superadmin`, `operador`, `cliente`, `subcliente`.  
1. Dentro de `python_scripts/` se incluye script `conversor.py` que inserta datos desde base de datos histórica `dvdrental` a base de datos del proyecto llamada `xtage`. El script indica procedimientos que deben llevarse a cabo para lograr insertar los datos.  
1. Dentro de `proyecto/scripts/` se incluye el script `create_users.py` que permite crear los usuarios solicitados. Este script está siendo ejecutado al inicio de ejecución del proyecto (Importado y función invocada desde `urls.py`).    
1. La aplicación `servicio` posee páginas de servicios provistos por `Cinetage`, discriminando roles de usuarios para mostrar contenidos diferenciados.  

## Demo:  

Se disponibilizará prontamente un enlace de demo del sistema en operación.  

Enlace:
<a href="#">Enlace demo</a>
