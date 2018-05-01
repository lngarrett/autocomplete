FROM python:2.7.9

ADD loader.py /project/
ADD requirements.txt /project/
ADD products.json /project/
ADD run.sh /project/
RUN chmod a+x /project/run.sh
EXPOSE 8000
CMD ["/project/run.sh"]
