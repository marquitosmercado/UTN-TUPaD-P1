# • ¿Qué es GitHub?  
# GitHub es una plataforma en la nube donde los desarrolladores pueden almacenar, compartir y colaborar en proyectos.

# • ¿Cómo crear un repositorio en GitHub?  
# Dentro de la terminal Git Bash se crea una carpeta con el comando "mkdir". Luego se usa el comando "cd", para ingresarlo en la carpeta que se buscó antes. 
# Después con el comando "git init" se crea el muevo repositorio.

# • ¿Cómo crear una rama en Git? 
# Dentro de Git Bash colocando el comando "git checkout -b nombre_de_la_rama"

# • ¿Cómo cambiar a una rama en Git?  
# Con el comando "git branch". Después se coloca el comando "git checkout nombre_de_la_rama"

# • ¿Cómo fusionar ramas en Git? 
# Primero, se tiene que hacer heckout a la rama destino "git checkout rama_destino", después se ejecuta con el comando "git merge rama_nueva"

# • ¿Cómo crear un commit en Git?  
# Se usa el comando "git add" para agregar todos los cambios). Luego, "git commit -m mensaje_descriptivo" para crear el commit con un mensaje descriptivo.

# • ¿Cómo enviar un commit a GitHub?  
# Se utiliza el comando "git push" seguido del nombre del repositorio remoto y el nombre de la rama local. Ejemplo: git push origin nombre_de_tu_rama_local

# • ¿Qué es un repositorio remoto?  
# Es una versión del repositorio Git hecho desde una pc pero alojada en un servidor en línea (GitHub)

# • ¿Cómo agregar un repositorio remoto a Git?  
# Usando el comando "git remote add <nombre_del_remoto> <URL_del_repositorio_remoto>"

# • ¿Cómo empujar cambios a un repositorio remoto?  
# Utilizando el comando "git push <nombre_del_remoto> <nombre_de_la_rama_local>"

# • ¿Cómo tirar de cambios de un repositorio remoto?  
# Con el comando "git pull <nombre_del_remoto> <nombre_de_la_rama_remota>"

# • ¿Qué es un fork de repositorio?  
# Es una copia de un repositorio personal que está en la propia cuenta dentro de GitHub

# • ¿Cómo crear un fork de un repositorio? 
# Utilizando el comando "git clone <URL_del_repositorio_remoto>"

# • ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?  
# Crear y gestionar Pull Requests se hace directamente desde GitHub. Una vez que el repositorio esté 
# forkeado, en GItHub seleccionar la opción "Comparar y crear una solicitud de extracción". Se aparecerá
# un formulario donde hay que seleccionar la rama del fork, seleccionar la rama del repositorio original,
# seleccionar la rama del repositorio original. Después hay que hacer click en el botón para crear la 
# solicitud de extracción.

# • ¿Cómo aceptar una solicitud de extracción?  
# Desde GitHub
# Fusionar: Integrar los cambios a la rama principal
# Cerrar: Marcar la Pull Request como completada.

# • ¿Qué es un etiqueta en Git?  
# Es una referencia a un punto específico en la historia del repositorio. Sólo estético.

# • ¿Cómo crear una etiqueta en Git?  
# Para una Lightweight Tags se usa el comando "git tag <nombre_de_la_etiqueta>"
# Para una Annotated Tags se usa el comando "git tag -a <nombre_de_la_etiqueta> -m "<mensaje_de_la_etiqueta>" "

# • ¿Cómo enviar una etiqueta a GitHub?  
# Para enviar una en particular se usa el comando "git push origin <nombre_de_la_etiqueta>"
# Para enviar todas se usa el comando "git push origin --tags"

# • ¿Qué es un historial de Git?  
# Es un registro cronológico de todos los cambios que se han realizado en el repositorio, a
# través de los commits

# • ¿Cómo ver el historial de Git? 
# Con el comando "git log"

# • ¿Cómo buscar en el historial de Git?  
# Para buscar información específica dentro del historial se puedes utilizar varias opciones (despues del git log colocar): --grep (para un texto puntual), -S (commits que cambiaron el número de ocurrencias de la cadena especificada), pickaxe-all (commits donde se añadió o eliminó una frase), --author="Nombre del Autor" (buscar por autor), entre otros

# • ¿Cómo borrar el historial de Git?  
# Con el comando "git reset"

# • ¿Qué es un repositorio privado en GitHub?  
# Es un repositorio que solo es accesible para el propietario de la cuenta

# • ¿Cómo crear un repositorio privado en GitHub?  
# Dentro de la web de GitHub, a la izq en el boon "NEW" se crea el repositorio y hay una opción para
# hacerlo privado, hacer click ahí.

# • ¿Cómo invitar a alguien a un repositorio privado en GitHub?  
# Ir a la configuración del repositorio en GitHub, dentro de la sección de "Collaborators" buscar a la
# persona que se quiera invitar por su nombre de usuario, ahí se le otorgar el permiso que se quiera.

# • ¿Qué es un repositorio público en GitHub?  
# Es un repositorio donde todo el contenido es visible para cualquier persona.

# • ¿Cómo crear un repositorio público en GitHub?  
# Dentro de la web de GitHub, a la izq en el boon "NEW" se crea el repositorio y hay una opción para
# hacerlo público, hacer click ahí.

# • ¿Cómo compartir un repositorio público en GitHub? 
# Si es público, compartiendo el URL del repositorio. Si es privado, agregar la persona (Add people) en
# la sección de colaboradores y otorgar permisos
