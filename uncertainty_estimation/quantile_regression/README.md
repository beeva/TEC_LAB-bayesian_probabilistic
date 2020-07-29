## Regresión Cuantílica
En está página se explica la regresión cuantílica como solución técnica para medir la incertidumbre de las predicciones en problemas de forecasting


### Indice de contenidos
- [Introducción a la técnica](#introduccion)
- [Regresión cuantílica en la medición de la incertidumbre](#cuantil-incertidumbre)
  - [¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?](#forecast-incertidumbre)
- [Otras aplicaciones de la regresión cuantílica](#aplicaciones)
- [Implementación de la regresión cuantílica](#implementacion)
  - [Técnicas de regresión cuantílica](#tecnicas)
  - [Validación - Función de pérdida](#validacion)


<a name="introduccion"></a>
## Introducción

La **regresión cuantílica** tiene como objetivo aproximar la mediana condicional u otros **cuantiles** (proporción τ de la distribución) de la variable de respuesta [2]

<a name="cuantil-incertidumbre"></a>
### Regresión cuantílica en la medición de la incertidumbre

En el siguiente gráfico vemos la aplicación de **regresión cuantílica en el dataset de precios de vivienda de boston**. En este ejemplo se busca encontrar una relación entre el precio de la vivienda y el número de habitaciones para responder preguntas del tipo **¿Cuánto cuesta una vivienda de 5 habitaciones?**

En el caso de la regresión lineal la estimación del precio se haría mediante **la media aproximada de las observaciones** de los precios de las viviendas. Sin embargo, en el caso de **regresión cuantílica podríamos responder con la mediana** que se ve menos afectada por valores atípicos (por ejemplo casas lujosas) o incluso el cuantil superior 90 e inferior 10 que nos podría dar una estimación de **cuánto podría costar este tipo de vivienda en el mejor y en el peor de los casos**. En este caso, estaríamos aproximando el valor de la vivienda sobre las partes superiores e inferiores de la distribución, lo que nos daría nuestra **estimación de la incertidumbre o intervalo de error de la predicción del precio**

 <p align="center"><img src="/docs/assets/quantile_regression/quantile_regression_example.PNG" height="350" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Ejemplo de regresión cuantílica</em><sup>[1]</sup></p>

En este ejemplo concretamente se realiza **un ajuste de 5 regresiones cuantiles que se corresponden con los percentiles o cuantiles** de 10, 30, 50, 70 y 90. El que el cuantil 50 se corresponde con la mediana que deja justo a cada lado el 50% de las observaciones, llegando hasta los límites o cuantiles extremos en los que el intervalo [10,90] recoge el 80% de las observaciones

Cómo se puede observar en el gráfico además la varianza del precio de la vivienda **no es constante u homocedastica**, por lo que es necesario proporcionar una medida de fiabilidad sobre esa posible variación o margen de error de las predicciones. Utilizar un **estimador más robusto basado en la mediana** se ve menos afectado por los outliers que la regresión lineal que aproxima la media.

<a name="forecast-incertidumbre"></a>
#### ¿Por que utilizar intervalos de predicción o cuantiles en Forecasting?

En problemas de forecasting se suele hacer forecasting sobre distintos horizontes de tiempo. Esto tiene una **implicación en la incertidumbre y varianza de las predicciones**

El cálculo de esta varianza o intervalo de predicción en forecasting en el h-instante (h:horizonte) de la variable respuesta y con una desviación estándar σₕ, puede ser calculada como:

<p align="center"><img src="/docs/assets/quantile_regression/forecast_variance.png" height="50" alt=“Ejemplo de regresión cuantílica” /></p>
<p align="center"><em>Estimación de la varianza de forecasting en el instante u horizonte h</em><sup>[2]</sup></p>

La constante c depende de la cobertura de probabilidades. Estos valores se pueden encontrar [aqui](https://otexts.com/fpp2/prediction-intervals.html)

Un característica importante de los intervalo de predicción es que incrementan con el horizonte. Cuánto más lejano sea el horizonte de tiempo al que hacemos forecasting, mayor será la incertidumbre asociada con esta predicción y más amplio será el intervalo de predicción

<a name="implementacion"></a>
### Implementación de la regresión cuantílica

<a name="validacion"></a>
####  Función de Pérdida

La **función de pérdida de la regresión cuantílica** minimiza una suma con **penalizaciones asimétricas** para las sobre-predicciones (aquellas predecciones que se realizan por encima del valor real) y las infra-predicciones (aquellas que están por debajo) de tal forma que **para un mismo quantile o valor de q, las penzalizaciones que se aplican sobre estas predicciones son diferentes**

En concreto, se observa que los errores más positivos (sobre-predicciones) son penalizados más en los cuantiles superiores (se tienen más en cuenta) y los errores más negativos (infra-predicciones) se penalizan más en los cuantiles inferiores. En el caso del cuantil 50 o mediana, se penaliza por igual

Esto ofrece la capacidad de poder estimar un cuantil concreto de la distribucción de la variable respuesta como se muestra en el siguiente cuadro:

<p align="center"><img src="/docs/assets/quantile_regression/loss_quantile_learn.PNG" height="270" alt=“Métodos de aproximación de la variable respuesta” /></p>
<p align="center"><em>Métodos de aproximación de la variable respuesta</em><sup></sup></p>


*Notebook de referencia: [quantile_regression_loss_function.ipynb](./quantile_regression_loss_function.ipynb)*


<a name="tecnicas"></a>
#### Técnicas de regresión cuantílica

La regresión cuantílica se puede aplicar casi con cualquier regresor **cambiando la función de pérdida**. Entre los métodos más populares están la regresión cuantílica lineal, los métodos basados en árboles y deep learning (deep quantile regression). En el siguiente notebook se puede encontrar la implementación de cada uno de ellos y el comportamiento o rendimiento sobre la problemática del dataset de precios de viviendas de boston de scikit-learn

Métodos implementados:

* OLS Linear regression - confident intervals
* Linear quantile regression
* Random forest regression
* Gradient Boosting regression
* Deep quantile regression

*Notebook de referencia: [quantile_regression_techniques.ipynb](./quantile_regression_techniques.ipynb)*

<a name="aplicaciones"></a>
### Otras aplicaciones de la regresión cuantílica

La regresión cuantílica tiene los siguientes usos y ventajas:

*Aplicación y ventajas*

* Proyectos sujetos **a gran incertidumbre** (e.g. falta de datos, gran volatilidad, mucho ruido, predicciones a futuro)
* El poder realizar regresión sobre cualquier parte de la distribución permite **conocer la influencia de los predictores desde el mínimo al máximo rango de la variable respuesta**

```
En el ejemplo anterior esto equivaldría a poder responder en el peor y el mejor de los casos cúal sería 
el precio de la vivienda, conocer estos valores te puede ayudar a hacer una mejor previsión de los ahorros
en el caso en el que haya mucha volatilidad en el precio o no sólo te interese otra carácteristica a parte 
del número de habitaciones que sospechas que puede afectar a los datos.
```

* Cuando las **condiciones de la regresion lineal no se cumplen** (homocedasticidad, normalidad, colinearidad, etc)
* **No hace asunciones de la distribución** de los residuos
* Ofrece una medida más robusta (estimamos la mediana condicionada) cuando la **distribución de los datos está sesgada** 
* Nos interesa realizar un **estudio de outliers** o sesgar la respuesta del modelo para minimizar el riesgo o por restricciones de negocio


*Ejemplos de aplicaciones*

* **Estudio de la desigualdad salarial de género**. Se estudian cuales son los factores que más afectan a la brecha salarial de género o sí los salarios más bajos se corresponden realmente con salarios de mujeres u hombres [3]

* **Estudio de tratamientos médicos** Queremos estudiar un tratamiento y queremos observar cómo se comporta en enfermedades raras y resulta muy costoso repetir el experimento o recoger más datos de ese sector poblacional 


#### Referencias

[1] https://medium.com/analytics-vidhya/quantile-regression-and-prediction-intervals-e4a6a33634b4

[2] https://otexts.com/fpp2/prediction-intervals.html

[3] https://www.semanticscholar.org/paper/La-desigualdad-salarial-de-g%C3%A9nero-medida-por-el-del-Freitas/610f046522d329e917f1b090b89fdf0da604d7dc
