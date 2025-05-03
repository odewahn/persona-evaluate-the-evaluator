import requests
import json

FN = ["herman-melville", "martin-kleppmann", "camille-fournier", "addy-osmani"]


# replicate this call with requests library
# curl -s -X POST -H "Content-Type: application/json" \
#   -d '{ "content":"<INSERT YOUR CONTENT HERE>" }' \
#     https://llm-proxy-service.platform.gcp.oreilly.review/api/v1/llm-proxy/TEMPORARY/calculate_metrics


def evaluate(content):
    # raise an error if the content is not a string
    if not isinstance(content, str):
        raise ValueError("Content must be a string")

    # Make the API request
    response = requests.post(
        "https://llm-proxy-service.platform.gcp.oreilly.com/api/v1/llm-proxy/TEMPORARY/calculate_metrics",
        headers={"Content-Type": "application/json"},
        json={"content": content},
    )

    # Check if the request was successful
    if response.status_code == 200:
        out = response.json()
        if out["success"] is False:
            raise Exception(f"Error: {out['error']}")
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")


# the strucrture of the evaluation function is likely to change
# so I'm isolating how it's computed here
def get_scores(evalution):
    burrows_delta = evalution["burrows_delta"]["score"]
    classifier = evalution["andreww_model"]["predict_proba"]["osmani"]
    return burrows_delta, classifier


def evaluate_sample(content):
    burrows_deltas = []
    classifiers = []
    # Call the evaluate function with the sample content
    for idx, sample in enumerate(content):
        print(f"Evaluating sample {idx + 1}/{len(content)}")
        # Call the evaluate function with each sample content
        result = evaluate(sample)
        burrows_delta, classifier = get_scores(result)
        burrows_deltas.append(burrows_delta)
        classifiers.append(classifier)
    return burrows_deltas, classifiers


out = {}
for fn in FN:
    # Load the sample content from the file
    with open(f"data/{fn}.json", "r") as f:
        sample_content = json.load(f)

    burrows_deltas, classifiers = evaluate_sample(sample_content)
    out[fn] = {
        "burrows_deltas": burrows_deltas,
        "classifiers": classifiers,
    }

# Save the results to a JSON file
with open("evaluations.json", "w") as f:
    json.dump(out, f, indent=4)
