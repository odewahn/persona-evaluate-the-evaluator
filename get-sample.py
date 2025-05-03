import requests
import json
import random


"""
# Sample data for testing.  This is a mockup of the data structure that would be returned by the API.
{
id: 5,
is_current: 1,
command: "transform clean-epub html-to-md token-split --n=100",
tag: "edz-845",
created_at: "2025-05-02 17:43:37",
blocks: [
{
id: 436,
tag: "ch01.html",
group_id: 5,
position: 0,
created_at: "2025-05-02 17:43:37",
content: "
# Chapter 1. What Makes a Software Engineering Team Effective?
Some teams seem to operate like well-oiled machines, churning out successes. Communication flows seamlessly, they meet deadlines with a smile, and they tackle challenges head-on. Conversely, other teams struggle to reach every milestone. Communication is chaotic, and meeting deadlines is a challenge. What makes the successful teams effective? It’s usually a mix of things: clear plans, honest talk, a healthy dose of trust, and a shared belief in what they’re doing. Some teams already have the rhythm and the steps down pat, while others are still figuring things out. But the",
token_count: 101
},
...
"""

URL = "http://localhost:8000/api/blocks"
N = 30
FN = "data/martin-kleppmann.json"

# Grab the data from the API
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()

# Select 20 random items from the blocks list
blocks = data["blocks"]
sample_blocks = random.sample(blocks, N)

# output the "content" field of each block into a list
sample_content = [block["content"] for block in sample_blocks]

# write the sample content to a file as a json array
with open(FN, "w") as f:
    json.dump(sample_content, f, indent=4)
