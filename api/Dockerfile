FROM python:2.7.9

ADD run.sh /project/
ADD requirements.txt /project/
ADD api.py /project/
RUN chmod a+x /project/run.sh
EXPOSE 8000
CMD ["/project/run.sh"]
