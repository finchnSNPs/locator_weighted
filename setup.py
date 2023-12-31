from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='locator',
      version='1.1',
      description='supervised machine learning of geographic location from genetic variation',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/kern-lab/locator',
      license='NPOSL-3.0',
      packages=find_packages(exclude=[]),
      install_requires=["numpy<1.19.0",
                        "tensorflow",
                        "h5py==2.10.0",
                        "scikit-allel",
                        "scikit-learn",
                        "matplotlib",
                        "scipy==1.4.1",
                        "tqdm",
                        "pandas",
                        "zarr",
                        "seaborn",
                        "gnuplotlib"],
      scripts=["scripts/locator.py"],
      zip_safe=False,
      setup_requires=["numpy"]
)
