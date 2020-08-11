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

### 0 - [Técnicas Frecuentistas]
La estimación de la incertidumbre se puede realizar mediante técnicas frecuentistas. Estas técnicas tienen unas límitaciones respecto a las técnicas bayesianas. El objetivo de los experimentos incluidos aqui es realizar un recopilatorio de técnicas existentes y analizar las ventajas y desventajas respecto a las técnicas bayesianas.

**V1.0.0-nonbayesian_techniques** (TODO: revisión)
* DATE: 03/12/2019
* EXPERIMENT-TECHNIQUE: Non bayesian techniques for uncertainty estimation in ML
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Explore other non bayesian and standard approches commonly applied in ML
    * EXPERIMENT GOAL: Understand its limitations. Why should be use a bayesian approach?
* RESOURCES:
  * [Notebooks](/non_bayesian_techniques/V1.0.0-nonbayesian_techniques)

### 1 - [Al vuelo](on-the-fly/README.md)
La técnica de estimación del error al vuelo es nuestro punto de entrada al reto y consiste en añadir (antes de entrenar) una salida más a nuestra red neuronal para que haga una estimación del error de predicción.

Aunque los experimentos proporcionan un buen fundamento teórico de cómo aproximar el reto, los resultados desaconsejan usar esta técnica, en favor de otras que se ven a continuación. El principal problema viene de mezclar predicción y estimación del error de dicha predicción en el mismo proceso de aprendizaje, lo que trae problemas en el entrenamiento y dificulta la explicación del modelo al mezclar hipótesis.

#### Experimentos (Pytorch)
Experimento original y pruebas derivadas del mismo

**V0.0.1-nongaussian_noise** (TODO: revisión)
* DATE: 11/12/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: add non gaussian noise to the original process
* RESOURCES:
  * [Notebooks](/on-the-fly/pytorch/V0.0.1-nongaussian_noise)

**V0.0.2-data_faraway_original** (TODO: revisión)
* DATE: 11/12/2019
* EXPERIMENT-TECHNIQUE: On fly variance estimation - EXP.I
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Added data in both training and validation far away from the original dataset distribution
    * EXPERIMENT GOAL: We would like to test if the uncertainty estimation increases in that points
* RESOURCES:
  * [Notebooks](/on-the-fly/pytorch/V0.0.2-data_faraway_original)

**V0.0.3-loss_function_customization** (TODO: revisión)
* DATE: 24/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Play with the loss functions using different custom losses
    * EXPERIMENT GOAL: Understand how is propagated both errors (y and sigma losses)
* RESOURCES:
  * [Notebooks](/on-the-fly/pytorch/V0.0.3-loss_function_customization)

**V0.0.4-loss_function_frameworks** (TODO: revisión)
* DATE: 27/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Implementation in different deep learning frameworks: pytorch, tensorflow
   * EXPERIMENT GOAL: Tests compatibility of the experiment-technique with different deep learning frameworks
* RESOURCES:
  * [Notebooks](/on-the-fly/pytorch/V0.0.4-loss_function_frameworks)

**V0.0.5-bayesian_interpretation** (TODO: revisión)
* DATE: ---
* DESCRIPTION: The goal of this notebook is twofold: first, it is explained the original experiment design since a bayesian perspective. Secondly, it is proposed the evaluation of the conformity of the assumptions taken
* RESOURCES:
  * [Notebook](/on-the-fly/pytorch/exp1_bayesian_interpretation.ipynb

**V0.0.6-synthetic_data_distribution** (TODO: revisión)
* DATE: 30/12/2019
* EXPERIMENT-TECHNIQUE: Loss Function - On fly variance estimation - EXP.I
* DATASET DESCRIPTION: Synthetic data - linear sinusoidal gaussian error variance
* DESCRIPTION: Play with different non gaussian error distirbutions and adapt the loss functions accordingly
   * EXPERIMENT GOAL: Do we improve results if the prior is satisfied?
* RESOURCES:
  * [Notebooks](/on-the-fly/pytorch/V0.0.6-synthetic_data_distribution)





#### Experimentos (TensorFlow)
Reimplementación en TensorFlow y pruebas exhaustivas.

**TF - 01-original-on_the_fly** (TODO: revisión)
* FECHA: 07/07/2020
* DESCRIPCIÓN: reimplementación del experimento original con la librería Tensorflow 2.0.
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


#### Experimentos


### 4 - [Modelos de mixturas](mixture_density_networks/README.md)


#### Experimentos


### 5 - [UMAL - Uncountable Mixture Asymetric Laplacian](umal/README.md)
[UMAL (Uncountable Mixture Asymetric Laplacian)](https://arxiv.org/abs/1910.12288) es una técnica avanzada que nos provee de características muy interesantes para la toma de decisiones en entornos de alta incertidumbre.__
En problemas de regresión, permite obtener una distribución de probabilidad de la predicción por cada punto sin presuponer la forma que tiene.__
En series temporales multimodales, permite hacer predicciones sin tener conocimiento previo sobre las distribuciones de los datos ni de sus errores.

Llegamos a la técnica de la mano de su autor [Axel Brando](https://www.linkedin.com/in/axelbrando) durante su estancia en [BBVA Data & Analytics](https://www.bbvadata.com/es/),  y combinamos todo el conocimiento previo para poder entenderla y aplicarla a ejemplos reales.


#### Experimentos

**-**
* FECHA: 
* DESCRIPCIÓN: introdución a la técnica de UMAL.
* RECURSOS:
  * [Notebook](umal/)
  
**-**
* FECHA: 
* DESCRIPCIÓN: implementación de UMAL como librería.
* RECURSOS:
  * [Notebook](umal/)
  
**-**
** Introducción
* FECHA: 
* DESCRIPCIÓN: aplicación de UMAL al [dataset M5 de Kaggle](https://www.kaggle.com/c/m5-forecasting-accuracy).
* RECURSOS:
  * [Notebook](umal/)


### 6 - Monte Carlo dropout

(TODO: qué hacer con traffic ligths, no es nuestro código)

#### Experimentos
** **
**MC-dropout**
* FECHA: - (por hacer)
* DESCRIPCIÓN: introducción a la técnica de Monte Carlo dropout.
* RECURSOS:
  * [Notebook](montecarlo_dropout/MC-dropout.ipynb)


---
>(TODO:
_NOTA: completar con la [lista de experimentos](https://raw.githubusercontent.com/beeva/TEC_LAB-bayesian_probabilistic/f8b30546cc2d2e216336c864568813f9ed5fcfff/labs_experiments/README.md)
)
---

## Otros documentos
* [Contexto del reto en la industria](industry.md) (TODO: revisar, no se menciona ninguna industria, candidato a trustworthy)
* [Validación y métricas de estimación de la incertidumbre](uncertainty_validation_metrics.md)

## Referencias

* [Uncertainty quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification) - Wikipedia

