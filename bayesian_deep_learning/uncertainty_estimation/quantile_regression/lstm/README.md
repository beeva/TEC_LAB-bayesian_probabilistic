# LSTM

Las redes del tipo LSTM (Long Short Term Memory) son un tipo de arquitectura de red recurrente que pueden aprender de largas secuencias de datos ordenados. Estas secuencias pueden ser palabras de un texto, sonidos en una melodía o las variaciones temporales del precio de un producto.

Este tipo de arquitecturas a diferencia de las redes recurrentes convencionales incorporan en cada unidad una serie de operaciones que vienen a resolver el problema del desvanecimiento del gradiente.


Para más información de cómo funcionan las LSTM y el problema del desvanecimiento del gradiente se recomiendan las siguientes referencias:

* [¿Cómo funcionan las LSTM?](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

* [Problema del desvanecimiento del gradiente](https://www.youtube.com/watch?v=qO_NLVjD6zE)

### Contexto de las LSTM en el reto estimación de la incertidumbre 

En las problemáticas propuestas de estimación de la incertidumbre asumimos un escenario en el que contamos sufientes datos, por tanto, es necesario un modelo de Deep Learning que sea capaz de aprender de largas secuencias como las LSTM. 

El contar con suficientes datos es importante y está relacionado con la incertidumbre por aproximación (underfitting) e incertidumbre epistémica. En este tipo de escenarios ambas se podrían considerar despreciables por lo que nos podríamos centrar en el tipo de incertidumbre irreducible p la incertidumbre aleatórica.
