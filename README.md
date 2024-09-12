# Access4 - Sistema de Control de Acceso mediante QR

## ¡Importante!
**Arquitectura:** Model Template View (Arquitectura Django) es lo mismo que Modelo vista controlador
- Modelo = Modelo (Capa de la Logica) Donde van a trabajar los Back
- Templeate = Vista (Capa de Interface) Donde van a trabajar los Front
- View = Controlador (Capa que cominca el modelo con la template) Lo usan ambos

### Git
**Crear la carpeta para el proyecto:** Elija donde va a mantener la carpeta con el proyecto
**Terminal:** Abra la terminal (git bash) y muevete a la carpeta (cd "[Ruta-a-la-carpeta]")
**Inicie git:** En la carpeta coloque (git init)
**Clonar el repositorio:** Permite descargar el repositorio (git clone https://github.com/M-P4rdo/Access4.git)
**Cree una nueva rama (Obligatorio):** Para evitar errores en el repositorio hay que crear una rama (git switch -c [Nombre-Rama]) Como nombre de la rama usa tu primer nombre para identificarlas
**Despues de Relaizar los cambios:** Cuando finalice de modificar o crear haga el commit con el mensaje claro de que hizo (git commit -m "[Expliacion-Cambio]")y luego realice el push (git push origin [Nombre-Rama])

### Visual Studio / Python
**Extenciones:** (Django Template, Python, Pylint, Python Debugger)
**Version de Python:** Python 3.12.3
**Crear Entorno Virtual (Opcional):** Si lo crean usen el nombre (venv) para que sea ignorado cuando lo suba
**Installar Django:** pip install django


## Distribucion del Proyecto
Cada uno de los FN es una vista distinta del mocup, por ende es un archivo distinto en el template de cada app, se pueden guiar por documento de requerimientos
(En cada carpeta Template de cada app van todos los archivos .html, en la cartela Static de la clase Base_App Va todo el Css, Js, Imagenes etc y de ahi se importa a las demas templaes)
*Los FNX Nombre-Internfaz son la guia para los Front*
*Los - [Nombre-Funcion] son la guia de los Back*

**(autenticacion_app):** App de Autenticación y Gestión
FN1 Ingreso (usuario) - [Validar-que-exista]
FN7 Login de Acceso (administrador) - [Login-Admin]
FN12 Editar Usuario (administrador) - [Cambiar-Informacion]
FN14 Perfil (administrador) - [Cambiar-informacion-propia]
FN13 Crear Administrador (administrador) - [Crear-si-es-SuperAdmin]

**(acceso_app):** App de Control de Accesos y QR
FN2 Cierre (usuario) [Generar-QR]
FN5 Registro de Usuario (usuario) [Formulario-de-Registro]
FN17 Registro de QR (administrador)
FN9 Registro de Ingresos (administrador)
FN15 Registro Manual (administrador).

**(usuarios_app):** App de 

**(dispositivos_app):** App de Gestión de Artículos
FN3 Registrar Dispositivo (usuario) - [Formulario-de-Registro]
FN4 Selección de Artículos a Ingresar (usuario) - [Consultar-Dispositivos-BD]

**(admin_app):** App de Administración y Panel de Control
FN10 Estadística (administrador)
FN11 Informe (administrador)

**(base_app):** App Base/Común:
FNX Diseño Base (usuarios)
FN8 Menú Lateral (administrador)
FNX Barra de navegadion Superior (administrador)
FN16 Menú Lateral Ingresos (administrador)


