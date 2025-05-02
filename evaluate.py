import requests
import json

FN = "data/herman-melville.json"


# replicate this call with requests library
# curl -s -X POST -H "Content-Type: application/json" \
#   -d '{ "content":"<INSERT YOUR CONTENT HERE>" }' \
#     https://llm-proxy-service.platform.gcp.oreilly.review/api/v1/llm-proxy/TEMPORARY/calculate_metrics


def evaluate(sample_content):

    # Prepare the data for the API request
    data = {"content": sample_content}

    # Make the API request
    response = requests.post(
        "https://llm-proxy-service.platform.gcp.oreilly.review/api/v1/llm-proxy/TEMPORARY/calculate_metrics",
        headers={"Content-Type": "application/json"},
        json=data,
    )

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")


# Load the sample content from the file
with open(FN, "r") as f:
    sample_content = json.load(f)

# Call the evaluate function with the sample content
try:
    result = evaluate(sample_content[:1])
    # Print the result
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f"An error occurred: {e}")
