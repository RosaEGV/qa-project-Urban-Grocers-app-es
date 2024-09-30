ROSA GUZMAN VALENCIA
COHORT 14
AUTOMATIZACION DE LISTA DE COMPROBACION DE PRUEBA API DE LA APLICACIÓN URBAN GROCERS MEDIANTE LA IDE PYCHARM, LIBRERÍA REQUEST Y PAQUETE PYTEST
EN ESTE PROYECTO SE PRETENDE VALIDAR LA LISTA DE COMPROBACION DE LA API GROCERY URBAN, PARA LA CREACION DE UN KIT, EN EL CAMPO NAME Y LA VALIDACION DEL AUTHTOKEN
La automatización hace que las pruebas de API sean mucho más fáciles, ya que no tienes que enviar solicitudes y respuestas manualmente, la automatización es una manera muy eficiente y rápida para nosotros los testers , es una herramienta valiosa. Python ofrece muchas soluciones listas para usar: librerías. Hacen que sea más fácil interactuar con el código. Python es bueno para escribir pruebas automatizadas. Hay varias razones para ello:
* Sintaxis concisa
 *Una gran cantidad de librerías. Estas son plantillas que puedes utilizar en tu código. Esto significa que podrás escribir pruebas automatizadas más rápido y con menos errores. Una característica clave de Pytest es que reconoce las pruebas basándose en un prefijo específico.
El entorno de desarrollo integrado o IDE (Integrated Development Environment) es un programa para escribir código. En cuanto a Python, el IDE más popular es PyCharm.
DESCRIPCION DE LAS TECNOLOGIAS UTILIZADAS
Las tecnologías utilizadas fueron las siguientes:
-	PyCharm(IDE)Python
-	GitHub
-	GIT Bash
-	Librería Request
-	Paquete Pytest
INSTRUCCIONES PARA EJECUTAR LAS PRUEBAS
Primeramente , tenemos que tener a la mano la documentación de la API Urban Grocers después tuvimos que vincular la cuenta tripleten con la cuenta en GitHub, después se creo automáticamente un proyecto llamado: “qa-project-Urban-Grocers-app-es”, dentro de este proyecto se cargaron los siguientes archivos , llamados:
-configuration.py
-data.py
-sender_stand_request.py
.gitignore
README.md
Solamente se tuvo que crear un archivo mas , en donde se trabajo la lista de comprobación, el nombre de este  archivo fue: 
-create_kit_name_kit_test.py
Dentro de cada archivo , se cargaron diferentes datos:
Configuration.py:
	Se anexaron la: URL_SERVICE= URL del servidor
			CREATE_USER_PATH=endpoint para la creación de un usuario
			KITS_PATH=endpoint para la creación de un kit
Data.py:
	Se anexaron: Aquí se anexaron los headers y bodys para las query, los cuales son los siguientes:
Headers = {
	“Content-Type”: “application/json”
}
User_body = {
	“fistName”: “Andrea”,
	“pone”: “+10005553535”,
	“address”: “8042 Lancaster Ave.Hamburgo, NY”
}
kit_body = {
	“name”: “Mi conjunto”
}
kit_body_1 = {
	“name”: “a”
}
kit_body_2 = {
	“name”: “a”
}
kit_body_3= {
	“name”: “”
}
kit_body_4 = {
	“name”: “a”
}
kit_body_5 = {
	“name”: “\N%@\,”
}
kit_body_6 = {
	“name”: “A Aaa”
}
kit_body_7 = {
	“name”: “123”
}
kit_body_8 = {
	
}
kit_body_9 = {
	“name”: 123
}

ARCHIVO sender_stand_request.py
En este archivo vamos a realizar nuestras solicitudes para crear un usuario (new_user) y crear un kit(new_client_kit), para estas dos solicitudes , de acuerdo a la aplicación de la documentación de la API, es necesario hacer dos solicitudes con método POST, para esto tenemos que crear dos funciones con este método y en la segunda solicitud nos piden la autorizacion del AuthToken, tambien es necesario la instalación de la libreris Request.
Es necesario , no olvidar que para el buen funcionamiento de estas funciones debemos importar los siguientes archivos:
IMPORT CONFIGURATION
IMPORT REQUEST
IMPORT DATA
ARCHIVO créate_kit_name_kit_test.py
En este archivo vamos a automatizar la lista de comprobación de la API de Urban Grocery para la creación de un usuario y para la creación de un kit, solamente utilizando el campo “name”,   mediante los autotest y con ayuda de la paquetería de Pytest.
Es importante no olvidar que necesitamos importar ciertos archivos para el buen funcionamiento de nuestros test y aserciones:
IMPORT sender_stand_request
IMPORT data
Dentro de esta lista de comprobación , solamente para el campo “name”, vamos a tener nueve pruebas , tanto positivas como negativas para comprobar, asi que , necesitamos definir dos funciones para las pruebas a automatizar, una de ellas será una aserción positiva y otra negativa. En la lista de comprobación existen pruebas positivas y negativas , las cuales deben dar cierto tipo de código para su aprobación o  fallo o desaprobación de estas. Para esto necesitamos realizar estas funciones y posteriormente llamar a los autotest para cada una de las variables de la lista de comprobación a probar.

ARCHIVO README.md
Tuvimos que realizar una breve explicación de este proyecto, explicar la descripción  de las pruebas, que se pretende validar, descripción de las tecnologías  utilizadas, instrucciones para ejecutar las pruebas, etc.
ARCHIVO .gitignore
Dentro de este archivo vamos a tener ciertas carpetas que debe ignorar al ejecutar los test
TECNOLOGIAS UTILIZADAS
Dentro de las tecnologías que utilizamos, estan las siguientes:
PyCharm, esta es una IDE comúnmente utilizada para PyThon y esta nos permite ejecutar funciones para poder automatizar ciertos procesos en el ámbito de lista de comprobaciones de diferentes API. Para esta tecnología tuvimos que instalar la librería Request y la paqueteria de Pytest para la creacion de funciones y autest.
GitBash: Dentro de esta consola estuvimos aprendiendo la manera de obtener un repositorio local asi como vincular con un repositorio remoto en GitHub , también se realizo el “commit” de los archivos y se empujaron hacia el repositorio remoto.
GitHub: En esta tecnología, creamos una cuenta y dentro de esta se vinculo el repositorio local con el repositorio remoto aquí. Tambien se creo una “primary key” con una URL SSH, para poder hacer la vinculación de nuestros repositorios.
Librería request: esta se instala dentro de los paquetes que nos provee PyCharm, dentro de la terminal, buscamos “Request” y le damos clic en instalar y asi quedara instalado sin  problemas
Paquete Pytest: Se instala desde la terminal de PyCharm y solo buscamos en la parte de Python Packages la palabra Pytest y le damos clic en “instalar”
INSTRUCCIONES PARA EJECUTAR LAS PRUEBAS
1.	Hay que estar actualizando y metiendo la URL del servidor , constantemente
2.	Tenemos que tener instalado la paqueteria Request y paqueteria Pytest
3.	Llamar las funciones en el archivo sender_request.py, son dos solicitudes Post, una para creacion de usuario y otra para creación de un kit.
4.	Llamar funciones Negative assert y Possitive assert, dentro del archive create, para después correr los autotest de cada uno de los puntos de la lista de comprobación en la cual solamente varia el campo: “name”
5.	Vamos a checar que este en “Current File”
6.	Correrlas y checar cuantas fueron aprobadas y cuantas no lo fueron



