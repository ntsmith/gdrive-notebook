FROM jupyter/minimal-notebook

# Install google cloud
RUN curl -fsSL https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz -o google-cloud-sdk.tar.gz \
  && tar -xvzf google-cloud-sdk.tar.gz \
  && ~/google-cloud-sdk/install.sh \
  && rm google-cloud-sdk.tar.gz
ENV PATH $PATH:~/google-cloud-sdk/bin
# Install python dependencies
RUN pip install --no-cache-dir google-api-python-client google-auth-oauthlib ipykernel psutil

