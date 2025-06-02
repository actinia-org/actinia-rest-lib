# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest

# pwgen is needed for the tests
RUN pip3 install --no-cache-dir pwgen==0.8.2.post0

COPY docker/actinia.cfg /etc/default/actinia
COPY src /src/actinia-rest-lib/src/
COPY setup.cfg /src/actinia-rest-lib/
COPY setup.py /src/actinia-rest-lib/
COPY requirements.txt /src/actinia-rest-lib/

RUN pip3 install --no-cache-dir -r /src/actinia-rest-lib/requirements.txt && \
    pip3 uninstall actinia-rest-lib.wsgi -y
# SETUPTOOLS_SCM_PRETEND_VERSION is only needed if in the plugin folder is no
# .git folder
ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.0

WORKDIR /src/actinia-rest-lib
RUN pip3 install --no-cache-dir -e .

WORKDIR /src/actinia_core
