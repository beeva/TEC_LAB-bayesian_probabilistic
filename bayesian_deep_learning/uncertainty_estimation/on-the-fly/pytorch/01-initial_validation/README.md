En este experimento se pretende hacer una validación inicial del experimeto propuesto en [1]

- Se consigue reproducir los mismos resultados de estimacion de la varianza de las predicciones
- Se observa que el método descrito en este post no influye en el rendimiento de la red. Para ello se entrena la red con la capacidad de estimar la incertidumbre y sin esta modificación. Se obtiene lo siguiente:
```
the score training with variance is 0.8009559643409793 and training without variance is 0.8008319692729339
```

[1] https://medium.com/@steve_thorn/predicting-uncertainty-with-neural-networks-aec0217eb37d


