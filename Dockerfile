FROM pytorch/pytorch
WORKDIR /ml
COPY . .
RUN pip3 install -r requirements.txt
WORKDIR /ml/code
#Expose the required port
EXPOSE 5000

CMD [ "python", "app.py", "--port", "5000", "--host", "0.0.0.0" ]
