import os


def is_experiment(path_experiment):
    """Say if a directory contains a replayable experiment.
    Conditions:
    - The directory exists
    - It is a directory, not a file.
    - It contains a "requirements.txt" file.

    Return
    ------
    retval: True or Exception.
      Wether the path is an experiment directory.
    """
    path_requirements = os.path.join(path_experiment, "requirements.txt")
    # Experiment path exists
    if not os.path.exists(path_experiment):
        raise Exception("ERROR: Experiment path \"{}\" does NOT exist".format(path_experiment))
    # Experiment path is a directory
    if not os.path.isdir(path_experiment):
        raise Exception("ERROR: Experiment path \"{}\" is NOT a directory".format(path_experiment))
    # There is a "requierements.txt"
    if not os.path.exists(path_requirements):
        raise Exception("ERROR: Experiment does NOT have a \"requirements.txt\"".format(path_requirements))
    return True


def list_experiments(path_project):
    """Return a list of experiments paths to create venv.
    
    Parameters
    ----------
    path_project: string
      Absolute path for the poject.
    """
    paths_explore = [path_project]
    paths_visied = {}  # Avoid circular references
    paths_experiments = []
    while paths_explore:
        path_candidate = paths_explore.pop()
        try:
            if is_experiment(path_candidate):
                paths_experiments.append(path_candidate)
        except Exception as e:
            paths_explore.extend(filter(
                os.path.isdir,
                [ # Get subdirectories
                    os.path.join(path_candidate, x)
                    for x in os.listdir(path_candidate)
                ]
            ))
    paths_experiments.sort()
    return paths_experiments
