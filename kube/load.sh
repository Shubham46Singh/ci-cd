#!/bin/bash

# URL to be tested
URL="http://127.0.0.1:55396/k8s"

# Number of concurrent requests
CONCURRENT_REQUESTS=500

# Number of total requests
TOTAL_REQUESTS=1000000

# Function to perform curl request
perform_request() {
  curl -s -o /dev/null -w "%{http_code}" "$URL"
}

# Loop to create background processes
for ((i=1; i<=TOTAL_REQUESTS; i++))
do
  # Run the curl command in the background
  perform_request &
  
  # Control the number of concurrent requests
  if (( i % CONCURRENT_REQUESTS == 0 )); then
    wait
  fi
done

# Wait for all background processes to finish
wait

echo "Load testing completed."
