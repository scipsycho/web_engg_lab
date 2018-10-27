FROM python:3

RUN apt-get update && apt-get install -y apache2 apache2-dev vim

COPY . .

WORKDIR mod_wsgi-4.6.5

#configuring and installing the module
RUN ./configure && make && make install

#loading the module in apache
RUN echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" >> /etc/apache2/apache2.conf

EXPOSE 80
CMD ["apachectl","-DFOREGROUND"] 

