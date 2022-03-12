# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.224.2/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install Python Packages for Development & Testing 
RUN pip3 install aiounittest 
RUN pip3 install bcrypt
RUN pip3 install pydata-sphinx-theme 
RUN pip3 install pytest 
RUN pip3 install pytest_asyncio 
RUN pip3 install quart
RUN pip3 install sphinx 
RUN pip3 install sphinxcontrib-napoleon 
RUN pip3 install twine 

WORKDIR /workspaces/quart-bcrypt 
