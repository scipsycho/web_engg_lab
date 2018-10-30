FROM python:3

RUN apt-get update && apt-get install -y apache2 apache2-dev vim

COPY mod_wsgi-4.6.5 mod_wsgi-4.6.5 

WORKDIR mod_wsgi-4.6.5

#configuring and installing the module
RUN ./configure && make && make install

#loading the module in apache
RUN echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" >> /etc/apache2/apache2.conf

WORKDIR /

#installing MySQL
RUN apt-get install -y mysql-server 

#installing django
RUN pip install --upgrade pip && pip install django

EXPOSE 80 8080 8000
CMD ["apachectl","-DFOREGROUND"] 

