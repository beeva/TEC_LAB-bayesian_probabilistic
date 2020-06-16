## Estimación de la incertidumbre en Forecasting 

El problema de forecasting realiza inferencias a futuro utilizando datos del pasado. Se podría considerar un caso particular de regresión en el que las variables están ordenadas en el tiempo. Se ha detectado especial aplicabilidad de las técnicas probabilísitcas debido a la **gran incertidumbre presente al realizar inferencias a futuro**.  

Está necesidad se ha detectado tras realizar un research en la industria y en BBVA Next Technologies. En concreto, se tiene como referencia la competición [M5 Forecasting Uncertainty de Kaggle](https://www.kaggle.com/c/m5-forecasting-uncertainty) en la que se pretende aplicar las técnicas estudiadas en este contexto

### Indice de contenidos

[PoC: Predicción de incertidumbre en ventas de producto](/poc_forecasting_uncertainty/m5_forecasting_uncertainty)
* [Exploratorio de datos](/poc_forecasting_uncertainty/m5_forecasting_uncertainty/dataset_exploration/) *Formulación de Hipótesis y Exploratorio de datos* 
* [Limipieza de datos](/poc_forecasting_uncertainty/m5_forecasting_uncertainty/dataset_cleaning/) *Transformaciones para la limpieza de datos*
* [Transformación de datos](/poc_forecasting_uncertainty/m5_forecasting_uncertainty/dataset_tranformation/) *Procesamiento y transformación de datos necesarias, feature engineering*
* [Modelado de la solución](/poc_forecasting_uncertainty/m5_forecasting_uncertainty/ml_solutions/) *Aplicación de soluciones técnicas*
* [MVP](/poc_forecasting_uncertainty/m5_forecasting_uncertainty/mvp_final_solution/) *Despliegue y documentatión de la solución final*

[Soluciones técnicas de estimación de la incertidumbre en forecasting](/poc_forecasting_uncertainty/techniques)
* [Regresión Cuantílica](/poc_forecasting_uncertainty/techniques/quantile_regression/) 
* [LSTM](/poc_forecasting_uncertainty/techniques/lstm/)

### Objetivos

Los **objetivos** a alcanzar en el contexto de este trabajo son:

1. **Aplicación y validación** de técnicas de estimación de la incertidumbre en una problemática real
2. Validación de la **solución técnica UMAL** para resolver este tipo de problemática
3. Obtener conocimiento sobre **técnicas adyacentes** con aplicación en **Forecasting** (e.g. LSTM, regresión cuantílica)
