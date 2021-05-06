from setuptools import setup, find_packages

setup(
    name="my_app",
    version="0.0.0-dev1",
    description='Test Holoviews with Tox',
    author='Bruno C. Quint',
    author_email='b1quint@gmail.com',
    install_requires=["bokeh>=2.3.1",
                      "holoviews", ],
    packages=find_packages(),
    python_requires='>=3.7',
)
