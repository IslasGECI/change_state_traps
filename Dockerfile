FROM python:3.7
COPY . /workdir
WORKDIR /workdir
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pandas \
    pylint \
    pytest-cov \
    pytest==6.0.1 \
    rope
CMD make
