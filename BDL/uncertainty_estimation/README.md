# Uncertainty Estimation

<de qué va todo esto>
<hablar de la estimación de la incertidumbre>
Ejemplo:
https://github.com/beeva/TEC_LAB-ai_watermarking/edit/master/README.md


## Documentation
* [Applications](applications.md)


## Experiments
### V0.0.1-Protect_CGAN
* DATE: 19/11/2019
* DESCRIPTION: protect a complex model, a CGAN generator.
* RESOURCES:
  * [Notebook](.ipynb)


---

## First Experiment: Synthetic data
This experiments are based on this release:
https://github.com/sthorn/deep-learning-explorations/blob/master/predicting-uncertainty.ipynb

The claiming of that release is that model can learn to predict and offers a value of predict uncertainty at the same time with a simple model.
It uses random data generate on the fly.

It uses the "variance" as error function, but actually it is not the variance, it is the difference between real y and predicted y.
The implicit dataset for training is a three column dataset with (x,y and error function), being the values of error function calculated on the fly.

The bayesian prior probability is set by using the error function as a variance, since it defines implicitly the error as a gaussian.


### 01-syntheticData-PredictionWihtoutVariance
This experiment makes predictions with a model predicting values and variance and other model predicting only values.
Hypothesis: Adding variance prediction may slow down predicting values, so accuracy me be penalized.
Result: Accuracy is almost the same for both values (a difference of 0.00002 in r2_score).

### 01-syntheticData-AddedDataFarAwayFromOriginal
This experiment add data with the same distribution far away from original data.
There is training data at (0,1) and (800,801).
Hypothesis: Variance should be low where there is training data and high far from known data.
Result: Model learn to predict low variance at any point, when the expected result is that variance increase far from known data.

### 01-syntheticData-addednongaussiannoise
This experiment add non gaussian noise at a low variance zone of original data.
Hypothesis: Noise should only affects to that low variance zone, increasing variance, but other low variance zones should not be affected.
Result: The expected result, variance increse and decrease gradually in that zone and others zones are almost not being affected.


### 01-syntheticData-predictedFarAwayFromData
This experiment train with original data for (0,1) region, but it predicts for several values to 1000.
Hypothesis: Model can learn the generative function and predicts values far away from data. Variance should increase as long as the value is far from known data.
Result: The expected result, values follows almost the generative function and the variance increase as long as prediction is far from known data.