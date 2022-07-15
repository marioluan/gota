FROM public.ecr.aws/lambda/python:3.8

# this arg is already exposed by the base image
# but I'm defining it here for clarity.
ARG LAMBDA_TASK_ROOT="/var/task"

# install dependencies
COPY "requirements.txt"  .
RUN pip3 install -r "requirements.txt" --target "${LAMBDA_TASK_ROOT}"

# application code is copied into the lambda filesystem
COPY "src" "${LAMBDA_TASK_ROOT}"

# lambda handler
CMD ["gota.core.api.handler"]

# TODO: split this image into: gota-core and gota-core-lambda