# Factorización PLU: Examen de Cómputo Matricial

## Integrantes del equipo y roles de trabajo:

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

## Estructura del repositorio:

La estructura del repositorio está basado en [este](https://drivendata.github.io/cookiecutter-data-science/) template y está organizado de la siguiente forma:

- Carpeta [docker](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/docker): Contiene la información pertienete para poder correr los scripts y notebooks en un contenedor de docker.

- Carpeta [img](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/img): Contiene las imágenes utilizadas en el reporte final.

- Carpeta [notebooks](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks): Contiene dos carpetas con los notebooks y scripts del equipo de Programación y Revisión.   
     1. [Programación](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks/Programacion): Dentro de esta carpeta se encuentran la siguiente carpeta:
           * [Historicos](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks/Programacion/Historicos): Contiene todos los scripts y notebooks históricos del equipo de Programación.  
           
           **Nota:** Todos los scripts finales del equipo de Programación se pasaron a la carpeta [src](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms) para que pudieran importarse las funciones mediante comandos.
     2. [Revisión](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks/Revision): Dentro de esta carpeta se encuentran los siguientes archivos y carpetas:
           * [Historicos](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks/Revision/Historicos): Contiene todos los scripts y notebooks históricos del equipo de Revisión.
           
           **Nota:** Todos los scripts finales del equipo de Revisión se pasaron a la carpeta [src](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/test_algorithms) para que pudieran importarse las funciones mediante comandos.
           * [Procedimiento_revision.ipynb](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/notebooks/Revision/Procedimiento_revision.ipynb]): Notebook que contiene todo el proceso que siguió el equipo de Revisión y pruebas de los algoritmos del script `revision_modular.py`. 
           
- Carpeta [references](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/references): Contiene información sobre las referencias utilizadas para desarrollar el proyecto.

- Carpeta [results](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/results): Contiene el notebook [reporte.ipynb](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/results/reporte.ipynb) que trae el reporte final del proyecto. 

- Carpeta [src](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src): Contiene los scripts del equipo de Revisión en formato de clases.
     1. [algorithms](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms): Dentro de esta carpeta se encuentran los siguientes archivos y carpetas:
          * [TodoJunto.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms/TodoJunto.py): Script final del equipo de Programación. Une los métodos de la clase `EliminaciónPorBloques` y `FactorizacionPLU`.
          * [EliminacionPorBloques.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms/EliminacionPorBloques.py): Es la clase de `Eliminación por bloques` que llama al método de solve de la clase `Factorización PLU`.
          * [factorizacion_PLU.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms/factorizacion_PLU.py): Contiene el algoritmo de factorización PLU y los métodos necesarios para poder resolver sistemas de ecuaciones utilizando dicha factorización. 
          * [FactorizacionPLU.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/algorithms/FactorizacionPLU.py): Mismos métodos que `factorizacionPLU.py` pero están dentro de una clase para que se pueda instanciar `FactorizacionPLU` como objeto.
     2. [test_algoritms](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/test_algorithms)Dentro de esta carpeta se encuentran los siguientes archivos y carpetas:
          * [revision_modular.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/test_algorithms/revision_modular.py): Script final utilizado por el equipo de Revisión.
          * [revision_factorizacion_PLU.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/src/test_algorithms/revision_factorizacion_PLU.py): Script inicial que ayudó a verificar si la factorización se estaba llevando a cabo correctamente al comparar con los resultados de la librería scipy.

- Carpeta [tests](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/tests): Contiene los scripts siguientes para correr las pruebas unitarias:
     1. .
          * [img](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/tests/img): Carpeta con la captura de pantalla del resultado de las pruebas unitarias.
          * [plu_functions.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/tests/plu_functions.py): Script que contiene las funciones disponibles en el modulo `TodoJunto.py` y se toman como input para los test unitarios.
          * [revision_functions.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/tests/revision_functions.py): Script que contiene las funciones disponibles en el modulo `revision_modular.py` y se toman como input para los test unitarios.
          * [test_plu.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-plu-paola-md/tree/master/tests/test_plu.py): Script que contiene los 6 test unitarios realizados y se ejecutan con la librería `pytest`. Utiliza como input las funciones disponibles en `plu_functions.py` y `revision_functions.py`.
          

## Instrucciones del examen: 

------------------------------------------------------------------------------------------------------------------------------

#### Actividades y roles en el examen:
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

#### Objetivos:

* Programar el método de eliminación por bloques que se encuentra en la sección **Métodos o algoritmos numéricos por bloques para SEL** en la nota [3.3.Solucion_de_SEL_y_FM](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/III.computo_matricial/3.3.Solucion_de_SEL_y_FM.ipynb). Para resolver este método, el equipo también programará [3.3.a.Factorizacion_LU](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/III.computo_matricial/3.3.a.Factorizacion_LU.ipynb) para resolver los sistemas de ecuaciones que surjan en el método de eliminación por bloques. Utilizar matrices pseudoaleatorias de tamaño mediano: aprox de dimensiones de $10^4 \times 10^4$.

* Aprendizaje sobre el uso de github como herramienta colaborativa en la creación y desarrollo de proyectos.

* Aprendizaje en la organización de trabajo en equipo para adopción de frameworks como [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) para el desarrollo de proyectos. 

**Nota para los equipos que programan una factorización matricial distinta a la SVD:** una vez que programan su factorización matricial tienen que utilizar métodos de sustitución hacia delante y hacia atrás para resolver el SEL asociado. Utilicen [solve triangular](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_triangular.html) de `scipy` o [backsolve/forwardsolve](https://stat.ethz.ch/R-manual/R-devel/library/base/html/backsolve.html) de `R` para esto.

#### Fecha de entrega y aspectos a calificar

* 19 de abril 11:59 pm

* Cada equipo y persona obtendrán una calificación. Para el equipo consideraré que los métodos obtengan correctamente los resultados y vale 70%. Para la calificación individual calificaré de acuerdo a sus commits, *issues*, *milestones* o tarjetas creadas y vale 30%.


#### Lenguaje a utilizar: Python


#### % de la calificación final: 20 puntos

