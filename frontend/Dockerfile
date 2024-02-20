FROM python:3.8

ARG SCENEX_API_KEY
ARG SHOPTIMIZER_BACKEND_URL
ARG WOOCOMMERCE_URL
ARG WOOCOMMERCE_KEY
ARG WOOCOMMERCE_SECRET

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV SHOPTIMIZER_BACKEND_URL=${SHOPTIMIZER_BACKEND_URL}
ENV SCENEX_API_KEY=${SCENEX_API_KEY}
ENV WOOCOMMERCE_URL=${WOOCOMMERCE_URL}}
ENV WOOCOMMERCE_KEY=${WOOCOMMERCE_KEY}
ENV WOOCOMMERCE_SECRET=${WOOCOMMERCE_KEY}

# Run script.py when the container launches
CMD ["streamlit", "run", "ui.py"]
