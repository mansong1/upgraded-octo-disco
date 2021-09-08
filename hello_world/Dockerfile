FROM public.ecr.aws/lambda/python:3.8

WORKDIR /

COPY app.py requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt -t . --no-cache-dir

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]