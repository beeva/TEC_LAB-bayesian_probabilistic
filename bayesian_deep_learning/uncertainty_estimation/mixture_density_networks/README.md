## Mixture Density Networks
En está página se explican brevemente **las redes de densidad mixta** como solución técnica para aproximar distribuciones heterogéneas de la variable respuesta. Este es el caso en el que sabemos que los datos u observaciones provienen de fuentes o procesos diferentes conocidos. Para ello, primero se incluye una breve introducción a **modelos de mixturas** que es a la familia a la que pertence este tipo de redes.


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
   - [Motivación](#motivacion) 
   - [Implementación](#implementacion) 
- [Mixture Density Networks](#mdn)

- [Experimentos y conclusiones](#Experimentos-y-conclusiones) 

<a name="introduccion"></a>
## Introducción

Un **modelo de mixturas** es un modelo probabilístico que nos permite representar la presencia de subpoblaciones de la población general. Esta representación de subpoblaciones nos va a permitir construir un estimador más robusto en el caso en el que la distribución de la variable respuesta sea heterogénea

En el siguiente gráfico tenemos un ejemplo de variable heterogénea *y* (el precio medio de unos cascos). Viendo este gráfico podemos inferir que podríamos tener 3 tipos de cascos diferentes: uno de precio bajo ~$30, medio ~$60, y alto ~$120. Sin embargo, las variables o procesos que causan realmente estas fluctaciones de precios no las tenemos ni las conocemos (son variables latentes).   

<p align="center"><img src="./img/mixture_models.png" height="160" alt="Mixture Density Network" /></p>
<p align="center">Mixture Density Network</p>

<a name="motivacion"></a>
### Motivación 

Si modelaramos este tipo de incertidumbre mediante técnicas como ['on-the-fly'](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/bayesian_deep_learning/uncertainty_estimation#1---al-vuelo) obtendriamos la distribucción de la izquierda, donde ignoramos las distintas fuentes que causan las fluctaciones en el precio, aunque la incertidumbre global seguiría siendo válida. Por el contrario, los modelos de mixturas si son capaces de modelar distitnas fuentes de incertidumbre y aproximar una distribución N modal (que contiene N modos) que se ajuste más a la distribucción real.

<a name="implementacion"></a>
### Implementación 

El problema que surje al estimar la distribucción de *y* es que por un lado no conocemos los distintos procesos que generan esas subpoblaciones ni a que subpoblación pertenece una observación concreta. Para esto, se utiliza el algoritmo de Maximum Likelihood Estimation que se explica en el siguiente [post de referencia](https://towardsdatascience.com/gaussian-mixture-models-and-expectation-maximization-a-full-explanation-50fa94111ddd).

<a name="MLE"></a>
#### MLE - Maximum Likelihood Estimation

El algoritmo de MLE o máxima verosimilitud nos permite obtener los parámetros del modelo o distribución que maximizan la probabibilidad de obtener unos datos dados.

Referencia - [Ejemplo de cálculo de MLE para la implementación de la función de pérdida](https://towardsdatascience.com/maximum-likelihood-estimation-explained-normal-distribution-6207b322e47f#:~:text=%E2%80%9CA%20method%20of%20estimating%20the,observed%20data%20is%20most%20probable.%E2%80%9D&text=Let's%20say%20we%20have%20some,that%20it%20is%20normally%20distributed)


<a name="mdn"></a>
## Mixture Density Networks

Las **redes de densidad mixta** (Bishop, 1994) es un tipo de red que combina las redes convencionales con el concepto de *modelo de mixturas*. En este modelo la sálida de la DNN hace la estimación de parámetros para la familia de distribuciones o componentes seleccionadas, las cuales se suman teniendo en cuenta el coeficiente de mezcla ⍺ para obtener finalmente una distribucción condicional hetérogena de *y* respecto a la entrada: 

<p align="center"><img src="./img/MDN.png" height="160" alt="Mixture Density Network" /></p>
<p align="center">Mixture Density Network</p>

Formalmente, la probabilidad condicionada de una red de mixturas tiene la siguiente forma:

<p align="center"><img src="./img/mdn_formula.png" height="70" alt="Formula MDN" /></p>
<p align="center">Mixture Density Network</p>

En esta fórmula los parámetros tienen la siguiente semántica:

* **c se corresponde con el índice de la correspondiente mixtura**. Hay hasta C componentes de mixtura (e.g. distribuciones) por salida, siendo un parámetro seleccionable.
* **⍺ es el coeficiente de mezcla**. Para entender este coeficiente podemos imaginarnos los controles deslizantes que controlan la mezcla de C salidas diferentes de audio. Este parámetro esta condicionado por la entrada x.
* **𝒟  esta es la correspondiente distribución de entrada a ser mezclada**. La distribución puede ser elegida atendiendo al tipo de aplicación.
* **λ son los parámetros de la distribución 𝒟**. En el caso de que denotemos 𝒟 como una distribución gausiana, estos parametros se corresponderian λ1 a la media condicional mean μ(x) y 
λ2 a la desviación estándar σ(x). Las distribuciones pueden tener distinto número de parámetros (e.g.: Bernoulli and Chi2 tienen 1 parámetro, Beta tiene 2, y la gaussiana truncada tiene hasta 4 parámetros) Estos son parámetros que forman también la salida de la red.


### Aplicaciones

Entre las **aplicaciones más destacadas** se encuentra la de Apple’s Siri en iOS 11 para reconocimiento de voz[2]. En [3] se puede ver su aplicación en generación de manuscritos y Amazon Forecast lo tiene dentro de la suite de algoritmos incluidos en su plataforma.

### Ventajas y desventajas

* *Ventajas* 

Permite estimar distribuciones heterogéneas de la variable respuesta.

* *Desventajas* 

El tamaño de la sálida de la red creada por la capa final de la MDN es (c+2)* m, dónde c es la dimensión de sálida de la red convencional y m el número de mixturas que estamos usando. Esto supone un incremento considerable en la dimensión de sálida respecto a la red convencional lo que puede volverlas muy inestables.

### Experimentos y conclusiones
   
Este método, en contraposición con lo validado en el Exp.I de [estimación de incertidumbre al vuelo](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/bayesian_deep_learning/uncertainty_estimation#1---al-vuelo), presentan las siguientes ventajas que se pueden resumir a mayor libertad en la definición del prior (condición de entorno o asunción dada):

 - Permite modelar facilmente que el ruido provenga de distintas familias de distribucciones.
 - Pueden modelar ruido multimodal, es decir, que no sólo provenga de una sola distribución si no de la suma de varias distribucciones de la misma familia con distintos parámetros. Este prior, sin embargo, también esta implicito en el exp.I y no es fácilmente modificable.
 - Tienen más soporte, es decir, el método está más comunmente aceptado. 

Se puede encontrar un [notebook](experiments/V0.1.6-real_datasets/uncertainty_prediction_house_prices_mdn.ipynb) con esta técnica aplicadas a un dataset para la estimación de incertidumbre.

En detalle, se puede encontrar un [notebook de redes de densidad mixta (MDN)](experiments/V3.0.0-mixture_density_networks), donde se puede encontrar una implementación y el detalle de las conclusiones.


#### Referencias

[1] https://towardsdatascience.com/a-hitchhikers-guide-to-mixture-density-networks-76b435826cca

[2] Siri Team, Deep Learning for Siri’s Voice: On-device Deep Mixture Density Networks for Hybrid Unit Selection Synthesis (2017)

[3] Alex Graves, Generating Sequences With Recurrent Neural Networks (2014)
