# 23 DE MAYO 2024
## prueba commit
# Ataque a Linux 
## ¿Cuándo? 
### (sin fecha específica, frustrado antes de ocurrir)

Todo empieza un 2 de noviembre de 2021, un usuario de Github registrado como JiaT75 (Jia Tan) envió un Pull Request al proyecto libarchive. Su contribución agregaba código inseguro a la librería y se fusionó a la rama principal sin discusión, nadie se dio cuenta. Este cambio pasó años sin detectarse y se ha parchado solo después de descubrirse el ataque a XZ Utils.
Lo más probable es que Jia Tan hizo este Pull Request para probar que tan fácil, o que tan difícil, era insertar código inseguro o malicioso en un proyecto Open Source.
Para el año 2022 empieza un constante acoso para la persona que mantenía el proyecto (Lasse Collin), dos personajes (Jigar y Dennis) lo atacan con varios correos en alusión a la falta de tiempo, de actualizaciones, que le estaba dando al proyecto y le pedían que busque a otra persona que se interese más por el avance de este, el acoso constante, la presión y los problemas personales de Collin lograron derrumbarlo.
En el 2023 Jia Tan se gano la confianza de colin al trabajar juntos, por este motivo Collin nomino a Jia Tan como un mantenedor de su proyecto, pensando que había encontrado a alguien que al fin podría ayudarlo, aquí empieza Jia Tan a introducir sus propias modificaciones, ya que él podía aceptar las modificaciones que se envíen para el programa, Primero, un usuario con el nombre Han Jansen envía un commit que Jian Tan aprueba y en julio se envía otro Pull Request que supuestamente corregía un problema con el commit anterior. Pero que preparaban el terreno para introducir el código malicioso.
En el 2024 a finales de febrero de este año se agregó el código con los pasos finales del ataque. Dicho código estaba lo suficientemente ofuscado para que sea muy difícil detectarlo.
Este código malicioso creaba una puerta trasera capaz de secuestrar conexiones remotas con SSH. El objetivo es que esta versión infectada se publique en las versiones finales de Debian y Red Hat, las dos distribuciones de Linux más usadas a nivel empresarial.

Cuando todo estaba listo para lanzar el ataque un ingeniero de Microsoft (Andres Freund) que trabaja en el desarrollo de Postgres (base de datos de código abierto), estaba realizando pruebas de rutina y se dio cuenta que el inicio de sesión de SSH demoraba más de lo normal y consumía más recursos de lo habitual.
Empezó a investigar y llego a la librería Liblzma de XZ Utils, descubrió la puerta trasera entre el repositorio original y los tarballs distribuidos (contenedor que puede almacenar ficheros, directorios y otros objetos en un archivo).
Al descubrirlo envió la información a los correos de OSS-Security, uno de los foros más importantes en temas de seguridad de software Open Source, Jia Tan suspendió su cuenta de Github y desapareció del mapa, Lesse Collin, que estaba descansando por su salud mental, tuvo que iniciar una carrera contrarreloj para revertir todos los cambios.
Hasta el momento se desconoce si Jia Tan era una sola persona, era un grupo o algún gobierno, según Costin Raiu, exjefe de seguridad de Kapersky, por el tiempo invertido y la complejidad y dedicación, puede ser un grupo financiado por un gobierno.
## ¿Como funciona?
Dentro del código de XZ había dos archivos que hacían la comprobación de calidad de código, pasaban como inofensivos, se volvían maliciosos con solo cambiar unos caracteres, el primer script convierte a un archivo de prueba en un script malicioso y este a su vez convertía el segundo también a script malicioso.
En el proceso de compilación de liblzma se crea un objeto con nombre “liblzma_la_crc64-fast.o” este objeto busca archivos específicos para comprobar en que sistema se está ejecutando, si encuentra estos archivos, activa y secuestra conexiones SSH.
liblzma no se conecta directamente con SSH sino que hay distribuciones de Linux que usan un parche de OpenSSH que se conecta a systemd-notify, que es una herramienta que lanza notificaciones para iniciar otros servicios cuando se inicia la conexión SSH. De esta manera se inicia libsystemd, que es una herramienta que controla a otros servicios y es quien carga a liblzma.
El siguiente paso es que liblzma utiliza la función de C ifunc para redireccionar las claves de autenticación de SSH y dárselas al hacker. Esto porque ifunc es la función que SSH utiliza para comunicarse con la herramienta que encripta las claves.
¿A quién afectaría?
Con la puerta trasera pudieron desde corromper sistemas, robar información, espionaje, manipular el mercado o iniciar una guerra y también afectar servidores de cloud computing, empresas gigantes, bancos o servidores gubernamentales.
