# Data Science and Machine Learning Vault

The required *Python* version for this project is *3.12.x.*

## About me

My name is *Rolando* and I've been writing software for over 20 years, always driven by my passion for research and education. I helped start the research program at Jala Foundation that grew into what's now *Jala R&D*, where I currently *lead the Generative AI team*.

Throughout my career, I've worked on everything from traditional software development to *Machine Learning* and *Blockchain* projects, always trying to create technology that makes a positive impact.

Starting this year, I am also a professor at *Jala University* teaching machine learning.

## Setup environment

As usual setup your virtual environment:

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip setuptools
$ pip install -r requirements-dev.txt
$ pip install -e .
```

## Basic code compliance

```
$ black .
All done! ✨ 🍰 ✨
X files left unchanged.
$ mypy .
Success: no issues found in X source files
```

## About the CI/CD pipeline

This `monorepo` comes with a pre-configured CI/CD pipeline that is triggered every time a push is made to a **merge request** or when a **merge request** is integrated into the **main** branch.

The pipeline is configured to:

- Execute **code compliance** checks.
- Generate documentation.

> You may add more stages or jobs to the pipeline, but make sure you **do not remove the existing ones**. In addition, make sure you do your best to **keep the pipeline green** at all times.
