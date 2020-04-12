# Examen de cómputo matricial equipo PLU

# Factorización PLU: Cómputo Matricial

**Integrantes del equipo**

| # | Alumno    |        Rol         |      User github       |
|---|-----------|--------------------|------------------------|
| 1 | Rafael    |    Project Manager |      123972            |
| 2 | Paola     |    Programadora    |      paola-md          |
| 3 | Sebastián |    Programador     |      C1587S            |
| 4 | Alfie     |    Programador     |      gonzalezalfie     |
| 5 | Maggie    | Revisión de código |      maggiemusa        |  
| 6 | Karla     | Revisión de código |      alpika19186       |
| 7 | Yalidt    | Revisión de código |      Yalidt            |

El objetivo de este programa es resolver la factorización PLU por bloques para matrices grandes.

## Factorización PLU simple

La factorización $LU$ de una matriz resume el proceso de [eliminación Gaussiana](https://en.wikipedia.org/wiki/Gaussian_elimination) aplicada a una matriz, lo cual es conveniente en términos del número total de operaciones de punto flotante cuando se desea calcular la inversa de una matriz o cuando se resolverá una serie de sistema de ecuaciones con una misma matriz de coeficientes. 

Frecuentemente no es posible escalonar una matriz solamente con operaciones de eliminación, por lo se requiere realizar un intercambio de renglones; para este tipo de matrices no existe la factorización $LU$ y lo que se aplica es la factorización $PA = LU$, donde la matriz P es una matriz de permutación, la cual se obtiene a partir de la matriz identidad al realizar el mismo intercambio de renglones. Ver [Factorización PLU](http://cb.mty.itesm.mx/ma1010/materiales/ma1010-26.pdf).

**Teorema**

Si $A \in  \mathbb{R}^{n \times n}$ es no singular, existen matrices $P, L, U$ de permutación, triangular inferior con $1$'s en la diagonal y triangular superior invertible respectivamente tales que $PA = LU$.

### Programación del código simple en Python

Para poder utilizar el código, es necesario instalar los paquetes que se encuentran en el archivo **Requirements.txt**

* Requirements: Importar los siquientes paquetes: numpy as np , timeit, matplotlib.pyplot as plt

* Breve descripción del script: Factorización_PLU.py












# Actividades y roles en el examen:
El equipo creado por el prof se subdivide en tres grupos: grupo de programación, grupo de revisión y una persona project manager. Esta división está inspirada en el *framework* [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) en un ambiente laboral real (y en esta práctica estaremos simplificando tal *framework*).  


A continuación se detallan las tareas a realizar en cada grupo.

* Project manager **(1 persona)**: es la persona más importante para el éxito del proyecto. Conoce el/los objetivo(s) a resolver, detalla las tareas que realizarán el grupo de programación y el grupo de revisión, organiza a ambos grupos, crea tarjetas en el [project board de github](https://help.github.com/en/github/managing-your-work-on-github/creating-a-project-board) y [milestones](https://help.github.com/en/github/managing-your-work-on-github/tracking-the-progress-of-your-work-with-milestones) para dar seguimiento a [issues](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue). Mantiene un contacto directo con el prof para dudas que tengan alguno de los otros grupos y para avisar en qué fase se encuentran. Les explica al grupo de programación y al grupo de revisión la correcta creación de *issues*, solución de los mismos y el uso de *milestones* y del *project board*.

Otras referencias útiles:

  * [Video sobre project management](https://www.youtube.com/watch?v=ff5cBkPg-bQ)

  * [Milestones in project cards](https://github.blog/changelog/2019-05-30-milestones-in-project-cards/).
  
  * [Video sobre issues, milestones](https://www.youtube.com/watch?v=ukYSRu4k0gs)
  
* Grupo de programación **(3 personas)**: se encarga de programar los métodos descritos en el objetivo y de documentarlos. La documentación involucra a los parámetros de entrada, los de salida y ejemplos de ejecución. Ver [documenting python code](https://realpython.com/documenting-python-code/) para un ejemplo en python de cómo documentar. Mantiene constante contacto con project manager para resolver *issues*, revisión de las tarjetas del *project board* y *milestones*.

* Grupo de revisión de programación y realización de reportes de resultados **(3 personas)**: se encarga de probar los métodos que realiza el grupo de programación con diferentes parámetros. Genera reportes de resultados con las variaciones de los parámetros. Su objetivo es encontrar *bugs* en el código y revisar que la documentación esté apropiadamente escrita y sea entendible. Si no pasa algún requerimiento anterior entonces crea uno o más *issues* por cada hallazgo encontrado. Ver [issues](https://guides.github.com/features/issues/). Le indica al grupo de programación y al project manager que deben resolverse los *issues*. ¿Cuáles son los parámetros en el contexto del objetivo de esta gh-classroom? los parámetros son diferentes matrices y lados derechos, diferentes dimensiones de las matrices y del los lados derechos, diferentes tamaños de los bloques.  

**Cada equipo decide qué personas están en qué rol.**

## Objetivos:

* Programar el método de eliminación por bloques que se encuentra en la sección **Métodos o algoritmos numéricos por bloques para SEL** en la nota [3.3.Solucion_de_SEL_y_FM](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/III.computo_matricial/3.3.Solucion_de_SEL_y_FM.ipynb). Para resolver este método, el equipo también programará [3.3.a.Factorizacion_LU](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/III.computo_matricial/3.3.a.Factorizacion_LU.ipynb) para resolver los sistemas de ecuaciones que surjan en el método de eliminación por bloques. Utilizar matrices pseudoaleatorias de tamaño mediano: aprox de dimensiones de $10^4 \times 10^4$.

* Aprendizaje sobre el uso de github como herramienta colaborativa en la creación y desarrollo de proyectos.

* Aprendizaje en la organización de trabajo en equipo para adopción de frameworks como [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) para el desarrollo de proyectos. 

**Nota para los equipos que programan una factorización matricial distinta a la SVD:** una vez que programan su factorización matricial tienen que utilizar métodos de sustitución hacia delante y hacia atrás para resolver el SEL asociado. Utilicen [solve triangular](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_triangular.html) de `scipy` o [backsolve/forwardsolve](https://stat.ethz.ch/R-manual/R-devel/library/base/html/backsolve.html) de `R` para esto.

## Fecha de entrega y aspectos a calificar

* 19 de abril 11:59 pm

* Cada equipo y persona obtendrán una calificación. Para el equipo consideraré que los métodos obtengan correctamente los resultados y vale 70%. Para la calificación individual calificaré de acuerdo a sus commits, *issues*, *milestones* o tarjetas creadas y vale 30%.


## Lenguaje a utilizar: Python


## % de la calificación final: 20 puntos



