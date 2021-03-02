# Proyecto CINETAGE/XTAGE21
**Actualizado: 2021-03-02**  
## Introducción:  
Este repositorio contiene el avance actual de desarrollo del proyecto de estudio CINETAGE/XTAGE21.  

## Detalles:  
**2021-03-02:**  
1. Se incluye CRUD de Películas sólo para `rol="operador"`. Se disponibilizan para CRUD sólo un subconjunto de campos de la base de datos, que son compatibles con la aplicación. Se han dejado fuera campos tales como: `precio de arriendo`, `duración del arriendo`, `costo de reemplazo` y otros, por tener sentido sólo en el caso de arriendo físico.  
1. Se incluye contador de visitas en vista `principal` y se incluye mensaje de bienvenida en template en caso de número de visitas >=2.  
1. Se incluye dropdown en barra de navegación para acciones exclusivas de `rol="operador"`.  
1. Se actualiza el nombre del repositorio a `cinetage`. Sin embargo url original sigue operativa para realizar `pull`.  


**2021-02-24:**  
1. La aplicación `panel` contiene la definicion de usuario personalizado heredando desde `AbstractUser` de Django.  
1. Se implementan roles: `superadmin`, `operador`, `cliente`, `subcliente`.  
1. Dentro de `python_scripts/` se incluye script `conversor.py` que inserta datos desde base de datos histórica `dvdrental` a base de datos del proyecto llamada `xtage`. El script indica procedimientos que deben llevarse a cabo para lograr insertar los datos.  
1. Dentro de `proyecto/scripts/` se incluye el script `create_users.py` que permite crear los usuarios solicitados. Este script está siendo ejecutado al inicio de ejecución del proyecto (Importado y función invocada desde `urls.py`).    
1. La aplicación `servicio` posee páginas de servicios provistos por `Cinetage`, discriminando roles de usuarios para mostrar contenidos diferenciados.  

## Demo:  

Se disponibilizará prontamente un enlace de demo del sistema en operación.  

<a href="#">Enlace demo</a>
