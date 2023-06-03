FROM python:3

ENV PATH /usr/local/bin:$PATH

WORKDIR /USR/SRC/APP


RUN apt-get update
#&& apt-get install -y --no-install-recommends

# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# COPY geos-3.11.2 ./
# RUN mkdir .build
# RUN cmake --build . --target install

# COPY proj-9.2.0 ./
# RUN mkdir .build
# RUN cmake --build . --target install


#RUN mkdir ./gdal

# COPY gdal-3.7.0 ./
# RUN ./configure
# RUN make install
#RUN pip install numpy

# RUN apt-get install -y software-properties-common && apt-get update
# RUN apt-get install -y gdal-bin libgdal-dev
# ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
# ARG C_INCLUDE_PATH=/usr/include/gdal
# RUN pip install GDAL



RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

#WORKDIR /places

#RUN mkdir ./static && mkdir ./templates

COPY --chown=places:places . .

#RUN pip install --upgrade

RUN pip install -r requirements.txt
WORKDIR ./Places_Remember
#USER place
EXPOSE 8000
CMD ["python",'manage.py','runserver','0.0.0.0:8000' ]