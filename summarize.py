# load the json data from the file
import json

with open("evaluations.json", "r") as f:
    sample_content = json.load(f)


summary = {}
for k in sample_content.keys():
    for evaluation in ["burrows_deltas", "classifiers"]:
        summary.setdefault(evaluation, {})
        summary[evaluation].setdefault(k, {})
        # compute average and standard deviation
        avg = sum(sample_content[k][evaluation]) / len(sample_content[k][evaluation])
        std = (
            sum((x - avg) ** 2 for x in sample_content[k][evaluation])
            / len(sample_content[k][evaluation])
        ) ** 0.5
        summary[evaluation][k]["avg"] = avg
        summary[evaluation][k]["std"] = std

print(json.dumps(summary, indent=4))


for author in [
    "herman-melville",
    "martin-kleppmann",
    "camille-fournier",
    "addy-osmani",
]:
    print(
        f"{author} | {summary['burrows_deltas'][author]['avg']} | {summary['classifiers'][author]['avg']}"
    )
