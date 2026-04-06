from setuptools import setup, find_packages, setup

setup(
    name='Fraud Detection',
    description='A Streamlit app for financial fraud detection using a machine learning model.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=["pandas","numpy","seaborn", "matplotlib", "joblib", "streamlit", "scikit-learn",]
)