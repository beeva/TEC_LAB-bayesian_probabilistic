**Revisión del trabajo UMAL**
---
El problema que se trata de resolver es el de la predicción de gastos e ingresos en la App del BBVA. Se intenta evitar notificar al usuario de un futuro posible gasto cuando el modelo no esté seguro (nivel de incertidumbre alto).
conclusions

Al parecer se proponen 2 mejoras:
    - (Está no es importante para nosotros) A nivel de modelización se propone una red usando una LSTM
    - La modelización de incertidumbre modificando la función de pérdida de la red con un método similar al MLE

En este Paper se propone una modelización de la función pérdida para la estimación de los parámetros de la PDF, incluida la varianza, similar al método de MLE. Este método usan los mismos conceptos que las Redes de Densidad Mixta. (Mixture Density Networks)

En el paper se utiliza la PDF de Laplace. No entiendo muy bien la elección de la función de distribución Laplace.

**Experimento**
---
Es el notebook orginal de la técnica. Es una validación inicial de que podemos reproducir los resultados.

**Próximos pasos**
---
Para poder comprender mejor esta elección se propone un experimento que use la función de pérdida propuesta y la función de pérdida que se obtendría usando una función de distribución gaussiana. Una vez obtenida la estimación de los parámetros, sigma y mu de la distribución normal, estaría bien comparar esta estimación con la que se obtiene del exp.I
