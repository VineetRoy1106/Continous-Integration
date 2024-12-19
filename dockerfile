# Step 1: Use an official Python runtime as a base image
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container
COPY . /app

# Step 4: Install the required Python dependencies
RUN pip install --no-cache-dir streamlit

# Step 5: Expose the port that Streamlit will run on
EXPOSE 5000

# Step 6: Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=5000"]
