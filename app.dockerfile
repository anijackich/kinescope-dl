FROM debian:12.4-slim
RUN apt update && apt install -y \
    ffmpeg \
    tar \
    python3-venv \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ADD https://www.bok.net/Bento4/binaries/Bento4-SDK-1-6-0-641.x86_64-unknown-linux.zip /tmp/bento4.zip
ADD ./requirements.txt /tmp/requirements.txt
RUN cd /tmp && unzip bento4.zip && mv /tmp/Bento4-SDK-1-6-0-641.x86_64-unknown-linux /opt/bento4
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH=${VIRTUAL_ENV}/bin:${PATH}
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
ENV FFMPEG_PATH=/usr/bin/ffmpeg
ENV MP4DECRYPT_PATH=/opt/bento4/bin/mp4decrypt
ADD . /opt/kinescope-dl/

ENTRYPOINT ["/opt/kinescope-dl/kinescope-dl.py"]

