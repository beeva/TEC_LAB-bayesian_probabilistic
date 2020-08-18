# Experiment repeatability
In order to repeat, extend and collaborate on experiments, we have the `manage.py` console script.

The only requirement is to have a [Python](https://www.python.org/) (version >= 3.5) interpreter with the pip library installed.


## Available experiments
List all the available experiments.

``` bash
$ python3 manage.py list
./manage.py list
Available experiments:
	bayesian_deep_learning/uncertainty_estimation/on-the-fly/tf
...
```

## Create an environment
Different experiments have different library requirements. Create a virtual environment, the `venv` directory, under the experiment path so the experiment libraries do not interfere others.

```bash
$ python3 manage.py create bayesian_deep_learning/uncertainty_estimation/on-the-fly/tf
```

## Run an experiment
Most of our experiments are in the [Jupyter Notebook](https://jupyter.org/) fomat. To run them, just get into de experiment directory an run the notebook server from the virtual environment.

``` bash
$ cd bayesian_deep_learning/uncertainty_estimation/on-the-fly/tf
$ venv/bin/jupyter notebook
```


## Delete an environment
As the environments are self-contained, the easiest way to delete them is just to remove the `venv` directory inside the experiment.

``` bash
$ cd bayesian_deep_learning/uncertainty_estimation/on-the-fly/tf
$ rm -rf python3 manage.py list
```


## Frequent Answered Questions

### How do I set the python version?
Although our experiments do not use exotic Python features, sometimes a specific python version has to be set in the virtual environment.

In this example, if we have the versions 3.8 and 3.5, by default, typing just `$ python3` will take the newer one, 3.8. If we want, the 3.5 versions, we can specify it when calling the interpreter. This way, the created `venv` will have Python 3.5.
```
$ python3.5 manage.py create bayesian_deep_learning/uncertainty_estimation/on-the-fly/tf
```

### What makes a directory an experiment?
Our assumptions on what to consider an experiment directory are:
* It is a directory, not a file.
* It contains a `requirements.txt` file where needed libraries and versions are set.


### Why?
1. It is the easiest way we have found to automate tedious tasks!
2. We make most of our work in Python.
3. It works.


# References
* [Reproducibility](https://en.wikipedia.org/wiki/Reproducibility) - Wikipedia
* [Reproducibility](https://explorable.com/reproducibility) - Explorable (_See section: Reproducibility vs. Repeatability_)
