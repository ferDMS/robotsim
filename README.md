Última actualización: 23/10/2021

#
<img src="resources/docs/logo_name.png" width="400" ><img> 
##
# **robotSim**

**robotSim** es un proyecto en desarrollo, así que le pedimos a los participantes de Candidates 2021 que estén atentos a cualquier aviso de actualización del programa. Igualmente, si hay cualquier duda no duden en contactarse con los programadores RoBorregos:

| Nombre | Correo | Github |
| ---- | ----- | ------ |
| Keven Arroyo | [A01283678@itesm.mx](mailto:A01283678@itesm.mx) | [@dake3601](https://github.com/dake3601) |

</br>

## Acerca de este proyecto

El simulador fue adaptado específicamente para los retos de Candidates 2021. En esta versión, se tiene un entorno específico para el [Hack de Programación de Robótica 2021](https://roborregos.com/).

### Uso del simulador

#### Correr programa localmente

1. Clonar el repositorio del proyecto.

	SSH:

	```bash
	$ git clone git@github.com:RoBorregos/robotSim.git
	```

	o HTTPS:
	```bash
	$ git clone https://github.com/RoBorregos/robotSim.git
	```

2. Entrar al directorio del proyecto.

	```bash
	$ cd robotSim
	```

3. Instalar dependencias del simulador.
	
	```bash
	$ pip install -r requirements.txt
	```

3. Codificar movimientos del robot en main\_program.py

4. Simular Programa 
	```bash
	$ python robotsim.py
	```
#### Correr online en Repl.it

1. Entrar a https://repl.it/languages/pygame
2. Copiar todos los archivos del repositorio en el env
3. Poner comando en terminal: python robotsim.py 


2. Entrar al directorio del proyecto.

	```bash
	$ cd robotSim
	```

3. Instalar dependencias del simulador.
	
	```bash
	$ pip install -r requirements.txt
	```

3. Codificar movimientos del robot en main\_program.py

4. Simular Programa 
	```bash
	$ python robotsim.py
	```

</br>

## Información para developer 
El repositorio tiene los siguientes archivos en un folder:

- **main\_program.py:** script donde se programan los movimientos del robot.
- **robotsim.py:** script de inicialización y actualización del entorno de simulación.
- **resources/map.json:** descripción del mapa (test case).

Para correr el simulador, símplemente se debe de correr el comando:
```bash
	$ python robotsim.py
```

</br>

## Mapa

![](resources/docs/map.png)

El mapa cuenta con las siguientes características:

- Dimensión de 8x6
- Paredes de color negro
- Baldosas de colores:	
  - Rojo
  - Azul
  - Verde
  - Magenta
  - Amarillo
  - Cyan


</br>

## Funciones del robot

| **Función** | **Descripción** | **Input** | **Output** |
| --- | --- | --- | --- |
| robot.move\_forward() | Mueve el robot a la baldosa de enfrente | - | - |
| robot.rotate\_right() | Gira el robot 90° a la derecha | - | - |
| robot.rotate\_left() | Gira el robot 90° a la izquierda | - | - |
| robot.display_color(color) | Hace que el robot señale un color específico. | string ('red','blue', 'green', 'magenta', 'yellow', 'cyan') | - |
| robot.finish\_round() | Termina la ronda. | - | - |
| robot.ultrasonic\_front() | Obtiene la distancia frente al robot en centímetros. | int (número de cuadros libres frente al robot)|
| robot.ultrasonic\_right() | Obtiene la distancia a la derecha del robot en centímetros. | int (número de cuadros libres a la derecha del robot)|
| robot.ultrasonic\_left() | Obtiene la distancia a la izquierda del robot en centímetros. | int (número de cuadros libres a la izquierda del robot)|
| robot.getColor() | Obtiene el color de la baldosa en la que el robot se encuentra | - | string ('white','red','blue', 'green', 'magenta', 'yellow', 'cyan') |

</br>

## Importante

Cuando se escriba código en main\_program.py se tienen que tomar en cuenta los siguientes detalles:

- Todo el código debe realizarse dentro de la función main()
- Si creas una función, de debe colocar como una función anidada
- Si se declara una variable, debe declararse dentro de main().

Con suerte, esto se puede solucionar en el futuro, pero por el momento se debe de realizar así para evitar que el programa tenga errores.

Si se identifica cualquier bug por favor manden mensaje a los organizadores correspondientes del Candidates 2021.
