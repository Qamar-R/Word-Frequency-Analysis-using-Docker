# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY word_frequency.py /app/

# Copy the text file into the container
COPY random_paragraphs.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir nltk

# Download NLTK data (required for stop word removal)
RUN python -m nltk.downloader stopwords

# Run the Python script
CMD ["python", "word_frequency.py"]