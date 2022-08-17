# Build app
FROM registry.access.redhat.com/ubi8/python-39
ARG USER_ID=1001

WORKDIR $HOME
USER 0
COPY main.py $WORKDIR
RUN pip install aiohttp && chown -R $USER_ID ./

USER $USER_ID

CMD ["python","main.py"]
