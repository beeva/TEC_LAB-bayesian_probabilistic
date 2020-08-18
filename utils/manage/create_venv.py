import os
import subprocess
import venv

from .experiment import is_experiment


"""TODO

from .experiment import is_experiment
"""

def create_venv(path_experiment, path_utils):
    """Create a virtual environment
    Paramenters:
    ------------
    path_experiment: string
      Absolute path to the experiment directory.
    path_utils: string
      Absolute path to the utils directory.
    """

    # Paths
    path_venv = os.path.join(path_experiment, "venv")
    path_requirements = os.path.join(path_experiment, "requirements.txt")
    path_python = os.path.join(path_venv, "bin", "python")
    is_experiment(path_experiment)
    # Do not create a venv if found one
    if os.path.exists(path_venv):
        raise Exception("ERROR: You already have an enviroment in: {}".format(path_venv))
    # Create virtual environment
    print("\t- Creating virtual environment on: {}".format(path_venv))
    venv.create(
        env_dir=path_venv,
        system_site_packages=False,
        clear=True,
        symlinks=True,
        with_pip=True
    )
    # Update pip to the last version
    print("\t- Upgrading local 'pip' package")
    subprocess.run([path_python, "-m", "pip", "install", "--upgrade", "pip"])
    # Install packages
    print("\t- Installing packages")
    subprocess.run([path_python, "-m", "pip", "install", "--requirement", path_requirements])
    # Link utils folder (venv have to exist)
    path_dest_utils =  os.path.join(path_venv, 'lib', os.listdir(os.path.join(path_venv,'lib'))[0], 'site-packages', 'utils')
    print("\t- Linking local utilities")
    os.symlink(path_utils, path_dest_utils, path_dest_utils) 

