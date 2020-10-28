# Estimación de la Incertidumbre 

La estimación de la incertidumbre tiene como objetivo ofrecer una **medida de fiabilidad** de las predicciones de un modelo de "deep learning".  Conocer el margen de error en las predicciones de un modelo es interesante en escenarios con alta incertidumbre y donde hay que evaluar riesgos para tomar decisiones. 

Un ejemplo lo podemos encontrar en la predicción de ventas de producto, donde surgen cuestiones con alta incertidumbre como:
> ¿Cuántos elementos X vamos a vender el mes que viene?

Ser capaces de dar una estimación, por ejemplo 50,  con un margen de error (bajo +-4 o alto +-30) nos ayudará a diseñar eficientes campañas de ventas y evitar costes innecesarios.

El reto también es interesante dentro de las directrices publicadas por comisión europea en 2018 de [Inteligencia Artificial Confiable](https://github.com/beeva/TEC_LAB-Trustworthy_AI), que respondes a la necesidad de industria de construir IA segura con una visión centrada en el humano. 



## Características de la incertidumbre de la predicción
Hemos identificado estas dimensiones para describir la incertidumbre:

* [**Aleatoriedad**](https://en.wikipedia.org/wiki/Uncertainty_quantification#Aleatoric_and_epistemic_uncertainty) del problema.
  * **Epistémica**  
    Es la incertidumbre sobre algo que teóricamente podríamos conocer pero que en la práctica no es así. Tiene solución.  
	Ejemplos de cómo se presenta:
    * _De aproximación_: surge si el modelo de ML es demasiado simple para aproximar la complejidad de los datos. Habrá que optar por un modelo más potente o complejo.
	* _De datos_: aparece cuando los datos de entrenamiento no representan completamente el problema a modelar. Se da si el tamaño del dataset (_interpolación_) y la significancia (_experimentación_) de sus variables no es suficiente para representar la variable objetivo.
  * **Aleatórica**  
    Aparece como ruido, por elementos del entorno que "no podemos medir" pero que nos afectan. Es imposible reducirla, aunque es posible modelarla de forma probabilística.
* **Variabilidad** del error de predicción.
  * [Homocedástica](https://es.wikipedia.org/wiki/Homocedasticidad)  
    La varianza del error de predicción es constante en todas las observaciones.
  * [Heterocedástica](https://es.wikipedia.org/wiki/Heterocedasticidad)  
     El error de predicción esperable varía con cada ejemplo.


## Técnicas y experimentos

### 1 - Al vuelo
La técnica de estimación del error al vuelo es nuestro punto de entrada al reto y consiste en añadir (antes de entrenar) una salida más a nuestra red neuronal para que haga una estimación del error de predicción.

Aunque los experimentos proporcionan un buen fundamento teórico de cómo aproximar el reto, los resultados desaconsejan usar esta técnica, en favor de otras que se ven a continuación. El principal problema viene de mezclar predicción y estimación del error de dicha predicción en el mismo proceso de aprendizaje, lo que trae problemas en el entrenamiento y dificulta la explicación del modelo al mezclar hipótesis.

#### Experimentos (Pytorch)
Experimento original y pruebas derivadas del mismo

**01-initial_validation** 
* FECHA: 11/12/2019
* DESCRIPCIÓN: validación básica (reproducibilidad de resultados) del funcionamiento de la técnica.
* RECURSOS:
  * [Notebook](on-the-fly/pytorch/01-initial_validation/initial_validation.ipynb)

**02-uncertainty_validation**  
* FECHA: 27/12/2019
* DESCRIPCIÓN: validación de las límitaciones de la técnica mediante la generación de datos sintéticos con distintos tipos de incertidumbre.
* RECURSOS:
  * 01-data_faraway_original: predicción de incertidumbre en ejemplos lejos de la distribucción del dataset de entrenamiento.
    * [Notebook](on-the-fly/pytorch/02-uncertainty_validation/01-data_faraway_original/predicting-uncertainty-PredictionFarAwayFromSignal.ipynb). Predicción lejos del dataset original de entrenamiento.
    * [Notebook](on-the-fly/pytorch/02-uncertainty_validation/01-data_faraway_original/predicting-uncertainty-AddedDataFarAwayFromOriginal.ipynb). Validación de interpolación entre nubes de datos de entrenamiento.
  * 02-nongaussian_noise: pruebas de validación de predicción de ruido no gausiano en puntos específicos
    * [Notebook](on-the-fly/pytorch/02-uncertainty_validation/02-nongaussian_noise/predicting-uncertainty-addedNonGaussianNoise.ipynb). Adición de ruido en puntos especificos del dataset sintético.
  * 03-synthetic_data_distribution: pruebas de validación de modelización de incertidumbre no gausiana
    * [Notebook](on-the-fly/pytorch/02-uncertainty_validation/03-synthetic_data_distributions/01-synthdata_noise_exp.ipynb). Generación de datos sintéticos con ruido no gausiano, usando una distribución exponencial estándar
    * [Notebook](on-the-fly/pytorch/02-uncertainty_validation/03-synthetic_data_distributions/02-synthdata_noise_uniform.ipynb). Prueba adicional de validación en datos sintéticos con adición de ruido no gausiano, usando una distribucción uniforme

**03-loss_function_customization** 
* FECHA: 24/12/2019
* DESCRIPCIÓN: pruebas realizadas modificando la función de pérdida con el objetivo de mejorar su compatibilidad con distintos frameworks y entender cómo se propaga el error en entrenamiento
* RECURSOS:
  * [Notebook](on-the-fly/pytorch/03-loss_function_customization/loss_error_experiments.ipynb)

#### Experimentos (TensorFlow)
Reimplementación en TensorFlow y pruebas exhaustivas.

**01-original-on_the_fly-tf**
* FECHA: 07/07/2020
* DESCRIPCIÓN: reimplementación del experimento original con la librería Tensorflow 2.0
* RECURSOS:
  * [Notebook](on-the-fly/tf/01-original-on_the_fly-tf.ipynb)


### 2 - Dos pasos
Comprendida la inconveniencia de estimar el error al vuelo y de las modificaciones sobre el proceso habitual de creación de un modelo, se propone hacerlo en dos pasos. Se parte de un modelo ya entrenado y se propone crear otro que estime su error de predicción.

#### Experimentos
Aún no se ha realizado ningún experimento.


### 3 - [Regresión cuantílica](quantile_regression/README.md)

La regresión cuantílica nos permite hacer una predicción sobre un cuantíl concreto de la distribución de la variable respuesta. Este método nos permite estimar los valores de predicción en los extremos (superior e inferior) de la distribución, ofreciendo un intervalo de error en la predicción que usamos como medida de incertidumbre. 

Por ejemplo, si queremos los valores extremos del intervalo que recogen el 50% de las observaciones, deberemos obtener dos predicciones, las asociadas a los cuantiles de orden 0.25 y 0.75 respectivamente.  
Si ponemos el ejemplo del precio de una acción en bolsa y queremos saber cuál es la variabilidad en el 90% de los casos, obtendremos los cuantiles 0.05 y 0.95. Pongamos que salen 200$ y 250$, con lo que podríamos decir que el 90% de las veces, la variabilidad es de 50$.

Si el concepto no es familiar, en esta [Introducción y referencias ](quantile_regression/README.md) se explora con algún ejemplo los conceptos alrededor de esta técnica para facilitar el comienzo.


#### Experimentos

**01-quantile_regression** 
* FECHA: 01/06/2020
* DESCRIPCIÓN: Benchmark básico con distintas técnicas de regresión cuantílica sobre el [dataset de precios de casas de Boston](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html) 
* RECURSOS:
  * 01-quantile_regression_techniques
    * [Notebook](quantile_regression/experiments/01-quantile_regression/01-quantile_regression_techniques.ipynb). Se exploran sobre diferentes modelos de ML la técnica de regresión cuantílica para comprenderla
    * [Notebook](quantile_regression/experiments/01-quantile_regression/02-quantile_regression_loss_function.ipynb). Estudio y comprensión de la función de pérdidas empleada para la regresión cuantílica


**02-lstm** (TODO: work-in-progress)
* FECHA: 10/06/2020
* DESCRIPCIÓN: Implementación del módelo más básico de LSTM con aplicación en un dataset sintético de series temporales
* RECURSOS:
  * [Notebook](quantile_regression/lstm/experiments/02-lstm/time_series_lstm_example.ipynb)

**03-deepquantile_lstm** 
* FECHA: 20/06/2020
* DESCRIPCIÓN: Implementación de estimación de la incertidumbre en forecasting utilizando el dataset sintético de series temporales
* RECURSOS:
  * [Lstm deep quantile regression con datos sintéticos](quantile_regression/deepquantile_lstm/experiments/03-dqr_lstm/lstm_dqr_synthdata.ipynb)
  * [Quantile regression con LSTM](quantile_regression/deepquantile_lstm/experiments/03-dqr_lstm/quantile_regression+LSTM.ipynb) (TODO: work-in-progress)


### 4 - [Modelos de mixturas](mixture_density_networks/README.md)
El modelo de mixturas son modelos probabilísticos que nos permite representar la modelizar la presencia de sub-poblaciones de la población general. Esta técnica nos permite modelar distribuciones más complejas que se alejen en forma de una distribucción normal.

Tras evaluar las límitaciones de la técnica 'On the Fly' para modelar problemáticas que presenten incertidumbre del tipo asimétrica, se decidió estudiar está técnica cómo solución alternativa.

#### Experimentos

**01-mixture_density_networks** (TODO: revisión)
* FECHA: 20/06/2020
* DESCRIPCIÓN: Aplicación del modelo MDN (Mixture Density Networks) para la estimación de la incertidumbre en el dataset sintético de 'On the Fly' y sobre el [dataset de precios de casas de Boston](https://www.kaggle.com/puxama/bostoncsv). El objetivo es comparar está técnica con los resultados obtenidos en 'On the Fly'
* RECURSOS:
  * [Notebook](mixture_density_networks/experiments/01-mixture_density_networks)

### 5 - [UMAL - Uncountable Mixture Asymetric Laplacian](umal/README.md)
[UMAL (Uncountable Mixture Asymetric Laplacian)](https://arxiv.org/abs/1910.12288) es una técnica avanzada que nos provee de características muy interesantes para la toma de decisiones en entornos de alta incertidumbre.__
En problemas de regresión, permite obtener una distribución de probabilidad de la predicción por cada punto sin presuponer la forma que tiene.__
En series temporales multimodales, permite hacer predicciones sin tener conocimiento previo sobre las distribuciones de los datos ni de sus errores.

Llegamos a la técnica de la mano de su autor [Axel Brando](https://www.linkedin.com/in/axelbrando) durante su estancia en [BBVA Data & Analytics](https://www.bbvadata.com/es/),  y combinamos todo el conocimiento previo para poder entenderla y aplicarla a ejemplos reales.


#### Experimentos

**01-umal_initial_validation** (TODO: revisión)
* FECHA: 01/07/2020
* DESCRIPCIÓN: Validación de la técnica UMAL utilizando la implementación del autor para estimar la estimación de incertidumbre aleátorica. Se utiliza un dataset sintético que modela distintos tipos de incertidumbre  
* RECURSOS:
  * [Notebook](umal/experiments/01-umal_initial_validation)
  
**02-umal_forecasting** (TODO: revisión)
* FECHA: 10/07/2020
* DESCRIPCIÓN: implementación de UMAL como librería y aplicación a la problemática de forecasting. Se proponen 2 datasets de series temporales: un dataset sintético y el [dataset M5 de Kaggle](https://www.kaggle.com/c/m5-forecasting-accuracy) [Work-in-Progress]
* RECURSOS:
  * [Notebook](umal/experiments/02-umal_forecasting)
  

## Otros documentos
* [Contexto del reto en la industria](industry_uncertainty_estimation.md) 
* [Estimación de la incertidumbre mediante técnicas frecuentistas](non_bayesian_techniques/frequentist_techniques.md)
* [Validación y métricas de estimación de la incertidumbre](uncertainty_validation_metrics.md)
* [Borrador técnico de estimación de la incertidumbre](https://docs.google.com/document/d/1DkcUwaWw3lTW_1ylt3POmfGURaD08xCuaUBYcRnc_5U)

## Referencias
* [Uncertainty quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification) - Wikipedia
* [Can You Trust Your Model’s Uncertainty? Evaluating
Predictive Uncertainty Under Dataset Shift](https://arxiv.org/pdf/1906.02530.pdf) - Evalúan diferentes técnicas de estimación de la incertidumbre
