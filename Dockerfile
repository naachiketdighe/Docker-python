# Use Alpine Linux as base image
FROM alpine:latest

# Install Python
RUN apk add --no-cache python3

# Copy the Python script into the container
COPY script.py /home/script.py
# Copy text files into the container
COPY home/data/IF.txt home/data/Limerick-1.txt /home/data/
COPY home/output/result.txt /home/output/

# Run the Python script
CMD ["python3", "/home/script.py"]