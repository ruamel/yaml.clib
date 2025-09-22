FROM quay.io/pypa/manylinux2014_x86_64:latest
# FROM quay.io/pypa/manylinux2014_x86_64:latest
# FROM quay.io/pypa/manylinux2014_i686:latest
# FROM quay.io/pypa/musllinux_1_1_x86_64:latest
# FROM quay.io/pypa/musllinux_1_1_i686:latest

MAINTAINER Anthon van der Neut <a.van.der.neut@ruamel.eu>

RUN echo '[global]' > /etc/pip.conf
RUN echo 'disable-pip-version-check = true' >> /etc/pip.conf

RUN echo 'cd /src' > /usr/bin/makewheel
RUN echo 'rm -f /tmp/*.whl'                                                     >> /usr/bin/makewheel
RUN echo 'for PYVER in $*; do'                                                  >> /usr/bin/makewheel
RUN echo '  for PYBIN in /opt/python/cp$PYVER*/bin/; do'                        >> /usr/bin/makewheel
RUN echo '     echo "$PYBIN"'                                                   >> /usr/bin/makewheel
RUN echo '     ${PYBIN}/pip install -Uq pip'                                  >> /usr/bin/makewheel
RUN echo '     ${PYBIN}/pip wheel . -use-pep517 --no-deps -w /tmp'            >> /usr/bin/makewheel
RUN echo '  done'                                                               >> /usr/bin/makewheel
RUN echo 'done'                                                                 >> /usr/bin/makewheel
RUN echo ''                                                                     >> /usr/bin/makewheel
RUN echo 'for whl in /tmp/*.whl; do'                                            >> /usr/bin/makewheel
RUN echo '  echo processing "$whl"'                                             >> /usr/bin/makewheel
RUN echo '  auditwheel show "$whl"'                                             >> /usr/bin/makewheel
RUN echo '  auditwheel repair "$whl" -w /src/dist/'                             >> /usr/bin/makewheel
RUN echo 'done'                                                                 >> /usr/bin/makewheel
RUN chmod 755 /usr/bin/makewheel

CMD /usr/bin/makewheel 310
