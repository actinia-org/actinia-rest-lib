# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest

ENV ACTINIA_CUSTOM_TEST_CFG=/etc/default/actinia-rest-lib-test
# TODO do not set DEFAULT_CONFIG_PATH if this is fixed
ENV DEFAULT_CONFIG_PATH=/etc/default/actinia-rest-lib-test

# hadolint ignore=DL3018
RUN pip3 install --no-cache-dir \
    iniconfig==2.0.0 pytest==8.3.5 pytest-cov==6.0.0

# copy needed files and configs for test
COPY docker/actinia-rest-lib-test/actinia-rest-lib-test.cfg /etc/default/actinia
COPY docker/actinia-rest-lib-test/actinia-rest-lib-test.cfg /etc/default/actinia-rest-lib-test
COPY . /src/actinia-rest-lib/

WORKDIR /src/actinia-rest-lib/
RUN pip3 install --no-cache-dir -e .

# RUN make test
