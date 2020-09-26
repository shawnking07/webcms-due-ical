FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

EXPOSE 80

COPY ./app /app
COPY environment.yml /app

COPY ./script/supervisord-debian.conf /etc/supervisor/conf.d/supervisord.conf

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
ENV PYTHONPATH="/root/miniconda3/envs/envs/webcms-due-ical/bin"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda env create -f environment.yml

RUN conda install -c conda-forge uwsgi -n webcms-due-ical

RUN echo "source activate webcms-due-ical" > ~/.bashrc
ENV PATH /root/miniconda3/envs/envs/webcms-due-ical/bin:$PATH
