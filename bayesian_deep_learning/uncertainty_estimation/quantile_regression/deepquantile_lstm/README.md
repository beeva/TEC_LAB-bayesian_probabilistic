# Deep Quantile LSTM

En este apartado se incluyen los aprendizajes de la combinación de las técnicas de [quantile regresión](../README.md) y [LSTM](../lstm/README.md) para resolver problemas de forecasting



El método de la regresión cuantílica para estimar uno o n cuantiles determinados dado un conjunto de datos de entrenamiento es aplicable a cualquier modelo de deep learning y se hace mediante la modificación de la función de pérdida por la **Pinball loss** de la regresión cuantílica

En el notebook [lstm_dqr_synthdata.ipynb](/experiments/lstm_dqr_synthdata.ipynb) se muestra la implementación del modelo de deep learning LSTM para la estimación de 5 cuantiles concretos [0.1, 0.3, 0.5, 0.7, 0.9]

Para resolver este problema existen dos implementaciones distintas:

* **Solución Naive**: Ajustamos N modelos, cada uno se entrena para ajustar un cuantil concreto que se pasa como entrada a cada modelo

* **Estimación conjunta**: Tenemos un único modelo capaz de ajustar una lista de N cuantiles distintos que se pasan como argumento de entrada [1][2][3]


Una de las limitaciones que se ha visto con esta técnica es el problema de los cuantiles cruzados:

* **Quantile crossing problem**: En la regresión cuantílica nada asegura que los cuantiles estimados mantengan un estricto orden creciente sobre el eje Y a lo largo del eje X.  Es decir, si pasaramos la lista ordenada de cuantiles [0.1, 0.3, 0.5, 0.7, 0.9] este orden creciente podría verse alterado dependiendo del valor de la X. Esto puede dar lugar a problemas de interpretabilidad como se explica en el siguiente ejemplo de aplicación

### Ejemplo de Aplicación 

La aplicación de la estimación por cuantiles a problemas de forecasting es de especial utilidad en riesgo financiero como sustituto de la métrica VaR (Value at Risk) para medir el riesgo al que está expuesto un portfolio financiero.

Por ejemplo, si el 95% de VaR de un portfolio es de 400$, quiere decir que cómo mucho vamos a perder 400$ en el 95% de los escenarios.

Esta medida viene a transmitir un nivel de confianza que tenemos sobre la estimación de pérdida de 400$, puesto que estamos indicando que cubrimos con ella el 95% de escenarios posibles, lo cual es un número de escenarios bastante alto.

Además, esta medida se suele ofrecer de manera continua y periódica en el tiempo junto con un horizonte temporal concreto sobre el que se hace la estimación. Por ejemplo, un horizonte de predicción de un día.

El problema de los cuantiles cruzados en esta problemática podría dar lugar a confusión puesto que estaríamos transmitiendo una alta confianza del 95% con la estimación de pérdida de 400$ que podría no ser cierta. Es decir, esto podría indicar que probablemente exista un valor superior que cubra mejor ese nivel de confianza y no lo estamos comunicando.



### Referencias 

[1] https://github.com/strongio/quantile-regression-tensorflow/blob/master/Quantile%20Loss.ipynb

[2] *Beyond Expectation: Deep Joint Mean and Quantile Regression for Spatiotemporal Problems* https://ieeexplore.ieee.org/document/8985289

[3] https://gdmarmerola.github.io/risk-and-uncertainty-deep-learning/