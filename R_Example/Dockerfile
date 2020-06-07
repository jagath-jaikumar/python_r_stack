FROM rocker/r-base:latest

RUN mkdir /app

COPY basic_script.r api_runner.r app/

EXPOSE 8000

RUN R -e "install.packages('plumber', dependencies=TRUE, repos='http://cran.rstudio.com/')"

CMD R -e "source('/app/api_runner.r')"
