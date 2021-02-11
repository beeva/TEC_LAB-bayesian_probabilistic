
# UMAL (Uncountable Mixture Asymetric Laplacian)
En está página se explica UMAL como **solución técnica para estimar la incertidumbre aleatórica heterocedastica**


### Indice de contenidos
- [Introducción a UMAL](#introduccion)
- [¿Qué problemática resuelve UMAL?](#umal_problematica)
- [Comparación con otras técnicas](#comparacion_tecnicas)
- [Aplicaciones](#aplicaciones)
- [Modelo de implementación UMAL](#modelo_umal)
- [Ejemplos de implementación](#implementacion)
- [*ANEXO: Profundización téorica UMAL*](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/bayesian_deep_learning/uncertainty_estimation/umal/umal_profundizacion_teorica.md)
- [FAQ](#FAQ)


<a name="introduccion"></a>
## Introducción a UMAL

**UMAL (Uncountable Mixture Asymetric Laplacian)** es una técnica bayesiana que permite estimar la incertidumbre aleatórica [heterocesdástica](#heterocesdástica) de las predicciones P(Y|X) *sin necesidad de conocimiento previo* de cómo se modela esta incertidumbre. Esta técnica es *capaz de modelar caraceterísticas complejas de las distribuciones* (e.g. asimétrias, multimodalidades), adaptandose mejor a la distribucción real de las mismas y *ofreciendo información relevante en escenarios de alta incertidumbre*

<a name="umal_problematica"></a>
## ¿Qué problemática resuelve UMAL?

Las técnicas convencionales de BDL para la modelización de la incertidumbre o generación de inferencias probabilísitcas **utilizan una fuerte suposición de asunciones** (e.g. Y∼N(μ,σ) ) que **no permite modelar distribuciones más complejas de la variable Y, P(Y|X=x)** cómo las distintas distribuciones que modelan el dataset de la fig.1. y cuyas estimaciones se aproximan a la esperanza condicional E[Y|X = x] para un x dado

<p align="center"><img src="./img/heterogeneous_dataset_umal2.PNG" alt=“Dataset sintético generado con 4 distribuciones distintas” /></p>
<p align="center"><em>Dataset sintético generado con 4 distribuciones distintas</em></p>

Este tipo asunciones hace que sea **dificil modelizar la inceridumbre aleatórica heterocedástica** de la cual es imposible adquirir conocimiento previo para la definición de estos priors o asunciones. Además, la modelización de la incertidumbre sin necesidad de conocimiento previo de cómo es esta incertidumbre **nos podría permitir realizar posteriormente un análisis más detallado y orientado a tarea** para poder entender las causas por las que se está dando esas variaciones en las estimaciones y aportarnos conocimiento o insights relevantes. 

## Profundización técnica en el tipo de problemática que resuelve UMAL

En la fig.2 se muestra un problema de regresión con unos datos sintéticos cuya distribucción de Y varia a lo largo del eje X por zonas. Estas zonas son generadas con distintos procesos generadores que modelan distintas distribucciones de probabilidad, en este caso de los tipos: asimétrica, simétrica, uniforme, multimodal. Estas variaciones a lo largo del eje X hace que el tipo de incertidumbre a modelar sea del tipo <a name="heterocesdástica"> *heterocedástica*, ya que la variabilidad de la Y en función de la X no se mantiene constante </a>. 

Además, si nos fijamos en un input de X concreto, pongamos X1 = 0.6 vemos que <a name="heterogénea"> el tipo de distribucción de Y puede presentar varias modas, es decir, la varianza de la distribucción de Y es del tipo *heterogénea* </a>


<a name="comparacion_tecnicas"></a>
**Qué soluciones existen para estimar este tipo de incertidumbre?**

Para comprender la aplicación de UMAL respecto a otras técnicas bayesianas, es necesario compararlo con las aunciones iniciales que realizan otras técnicas. Para esto es necesario ponernos en 2 casos o soluciones hipóteticas

<p align="center"><img src="./img/technique1_vs_umal.png" height="400" alt=“Fig.2  Comparación de soluciones - estimación de la incertidumbre” /></p>
<p align="center"><em>Fig.2  Comparación de soluciones - estimación de la incertidumbre </em></p>

* **Solución 1 : Asunción restrictiva de prior - Utilizada por técnicas convencionales Bayesian Deep Learning**: Este es el caso en el que estimamos Y como *una esperanza condicional E[Y|X = x] asumiendo una distribucción normal de Y*, como sucede en la mayoría de las técnicas BDL. El resultado que obtendriamos utilizando este tipo de soluciones es que para la zona en la que la distribucción es simétrica; no nos alejaríamos mucho de la distribucción real de Y puesto que este tipo de distribucción está centrada en la media. Sin embargo, si nos vamos a otras regiones en el eje X, como por ejemplo, la que se muestra en el gráfico x=0.6, vemos que no vale con tomar una distribucción centrada en la media de Y (solución 1 gráfico) puesto que la varianza de la misma varía según el valor que esta tome, es decir, el tipo de distribucción es multimodal o *heterogénea*

* **Solución 2: Asunción menos restrictiva, agnóstica del tipo de distribucción de probabilidad - UMAL**: En UMAL utilizamos el concepto de regresión cuantílica que permite construir un estimador sin realizar fuertes asunciones del tipo de distribucción de Y. Esto permite estimar una distribucción heterogénea que cómo se ve en el gráfico (solución 2) al final se aproxima mejor a la distribucción real de Y. 

    Para ello, se hace una aproximación de esta distribucción usando una composición de distintas ALDs (Asymmetric Laplace Distribution) que realiza una discretización por partes de la distribucción real, es decir, hace una estimación por cuantil de la distribucción. (*Nota: La moda de la distribucción posterior de la función de probabilidad de la ALD se corresponde con el valor del estimador de la regresión cuantilica para un cuantil*)
    
    
----
Esta comparativa de soluciones se puede encontrar en el notebook [synthetic_regression_umal_vs_exp_1.ipynb](/experiments/synthetic_regression_umal_vs_exp_1.ipynb) que utiliza el dataset sintético explicado anteriormente para responder a la pregunta:
> H1: Can we use techniques with restrictive priors to model aleatoric uncertainty with zero-knowledge about this uncertainty? How does this restrictive prior affect model performance?
----

<a name="aplicaciones"></a>
## Aplicaciones

Se ha detectado que esta técnica *es de especial interés en problemas de forecasting* debido a la gran incertidumbre o volatilidad inherente al realizar predicciones a futuro. Otras aplicaciones podrían ser sistemas en tiempo real o sistemas expuestos a un riesgo alto.

**Algunos ejemplos de estas aplicaciones** son: *la evaluación del riesgo en aplicaciones financieras, predicción de demanda/mobilidad para la optimización de sistemas de transporte o predicción del consumo energético*. 

* *Evaluación de riesgo financiero*: En este caso nos podría dar predicciones mucho más robustas; también se podría utilizar cómo sustituto de la métrica VaR (Value at Risk), utilizada actualmente en negocio y que mide la exposición al riesgo de un determinado activo financiero. En este caso, tendríamos una métrica mucho más robusta que no realiza asunciones previas de cúal es la distribucción de la varianza del valor del activo.


* *Optimización de sistemas de transporte*: Utilizando información del tráfico podríamos inferir información relevante para estimar la probabilidad de accidentes o congestiones puntuales de tráfico. Además podría ayudar a los operadores de tráfico a interpretar mejor las posibles varianciones de tráfico mostrando la varianza de las mismas.

* *Consumo energético*: En este caso, nos podría servir para anticipar posibles picos de consumo o detectar y conocer las causas por las que se están dando estas variaciones de consumo.

Cómo se puede observar, **todas estas problemáticas comparten un componente aleatórico heterocedastico dificil de modelar** que proporciona información muy relevante para el negocio. 

----
Para ilustrar mejor la aplicabilidad de esta técnica se ha desarrollado el [Notebook 2 - Uncertainty Forecasting with UMAL](https://github.com/beeva/TEC_LAB-bayesian_probabilistic/blob/master/poc_forecasting_uncertainty/techniques/umal/umal_implementation.ipynb) que utiliza un dataset sintético de forecasting para responder a la pregunta:

> H2: Can we use UMAL to model aleatoric uncertainty in forecasting tasks? How does this uncertainty interpreted?
----


**Aplicación de UMAL en la problemática de Forecasting**

<p align="center"><img src="./img/forecasting_uncertainty.png" alt=“Fig.3 Forecasting - estimación de la incertidumbre - UMAL” /></p>
<p align="center"><em>Fig.3 Forecasting - estimación de la incertidumbre - UMAL </em></p>

En la Fig.3 se puede observar un dataset sintético o serie temporal representativa de problemas de forecasting. Este tipo de problemática a diferencia de la regresión convencional **encuentra relaciones temporales en datos ordenados cronológicamente en el tiempo para infererir predicciones a futuro**. Estas relaciones pueden ser muy simples como estacionalidades, ciclos, etc. o más complejas que tengan en cuenta la autocorrelación de otras variables asociadas o contexto.

Para hacer inferencias a futuro en este tipo de problemáticas **se suele establecer un horizonte o ventana de tiempo** a la que se quiere predecir (e.g. predicción de demanda a 2 horas vista). En el caso del dataset representado de la Fig.3 se ha utilizado un horizonte de 1 hora. Sin embargo, la selección de este horizonte de tiempo no suele ser arbitraria y suele venir dado por el conocimiento actual de negocio. 

En escenarios de alta incertidumbre, a veces no es posible adquirir este conocimiento o los datos de negocio necesarios para medir el riesgo de las predicciones que nos permitirian mejorar la selección de este horizonte. Es en estos escenarios dónde es importante contar con un método robusto cómo el propuesto aqui sin necesidad de tener conocimiento o datos del problema y que permita tomar decisiones teniendo en cuenta el riesgo de estas.

Para resolver este problema, UMAL estima intervalos de predicción o cuantiles, representados en franjas de colores en el gráfico, que realizan una discretización de la distribucción de P(Y|X) y **permite modelar la varianza de las predicciones para cada uno de los intervalos** (representada con una linea transversal para cada cuantil). Esta varianza nos permite medir el riesgo de las predicciones por partes de la distribuccion, ayudándonos por ejemplo a ponernos en el mejor y peor escenario y facilitar la selección del horizonte temporal de predicción.

<a name="modelo_umal"></a>
## Modelo de implementación UMAL

El **modelo de UMAL (Uncountable Mixture Asymetric Laplacian)**, como se ha mencionado anteriormente, tiene cómo objetivo aproximar la densidad predictiva P(Y|X) de tipo heterogénea. (véase Figura 1). Para ello predice para cada input x los parámetros de la ALDs condicionadas seleccionadas (μ,  τ , σ ) (por la lista de quantiles que se introduce como entrada) de manera simultánea.
 
Este modelo se caracteriza por lo siguiente:
  * **entrada**: vector de entrada X ∈ Rn y una lista de quantiles τ  =  { 0.1, 0.2, … ,0.9}  (selección de ALDs)
  * **salida**: los parámetros de la ALDs condicionadas seleccionadas, y el cuantil τi :  {μ,  τ , σ }
  
<p align="center"><img src="./img/umal_model.PNG" height="200" alt=“UMAL modelo” /></p>
<p align="center"><em>UMAL modelo</em></p>

Es importante destacar que UMAL *es agnóstico del modelo de Deep Learning que se utilice*, es decir, podría ser válido tanto para CNN; LSTM, etc.

<a name="implementacion"></a>
#### Ejemplos de Implementación 

* [Notebook 1 - synthetic_regression_umal_vs_exp_1.ipynb](experiments/synthetic_regression_umal_vs_exp_1.ipynb) *Comparativa de UMAL con técnicas BDL que utilizan asunciones restrictivas en la modelización de la incertidumbre de las predicciones*

* [Notebook 2 - Uncertainty Forecasting with UMAL](experiments/umal_implementation.ipynb) *Implementación de UMAL con aplicación en medición de la incertidumbre en forecasting mediante la generación de una serie temporal sintética*

* [Original UMAL collaboration notebook](experiments/UMAL_original/README.md) *Notebook original generated along collaboration with Axel Brando*

### FAQ

##### ¿Dónde tendría sentido aplicar la técnica UMAL? [Core Question]

**Conocimiento del problema**
 - Problemas en los que (se sospecha) que no se dispone o va a disponer de información relevante de la problemática o conjunto de variables que modelizan esa problemática. Es decir, tenemos un alto grado de incertidumbre.
 [En problemas de forecasting siempre se va a dar esta problemática y va ser dependiente del horizonte de tiempo de predicción](#https://github.com/beeva/TEC_LAB-bayesian_probabilistic/tree/master/bayesian_deep_learning/uncertainty_estimation/quantile_regression#Aplicaci%C3%B3nForecasting) 

**Aplicación**
 - Mejora de la robustez en aplicaciones en tiempo real
 - Nos interesa ser capacaces de modelizar esa incertidumbre porque nos proporciona información core para el negocio (e.g. riesgo financiero)


