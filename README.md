Ths repo is an evaluation of our evaluator function, which you can call with the `requests` library like this:

```python
response = requests.post(
    "https://llm-proxy-service.platform.gcp.oreilly.com/api/v1/llm-proxy/TEMPORARY/calculate_metrics",
    headers={"Content-Type": "application/json"},
    json={"content": content},
)
```

I generated 30 writing samples from Addy Osmani, Camille Fournier, Martin Kleppmann, and Herman Melville (as kind of the anti-Addy). The samples are in the `data` directory. I then used the `calculate_metrics` endpoint to evaluate each writing sample, and then computed averages for the Burrow's Delta and the classifier score.

```
| Author           | Burrow's Delta        | Classifier          |
| ---------------- | --------------------- | ------------------- |
| herman-melville  | -0.023990434904893238 | 0.15332259798131764 |
| martin-kleppmann | 0.028999585409959158  | 0.23019579744897467 |
| camille-fournier | 0.11857400969602168   | 0.4156682573901136  |
| addy-osmani      | 0.31612503503759704   | 0.6587510983411453  |
```
