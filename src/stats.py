import statistics
import json

ratings, llm_ratings, response, response_ratings = [], [], [], []

with open("llm_annotated.json", "r") as f:
    data = json.load(f)
    for conversation in data:
        ratings.append(conversation["ratings"])
        llm_ratings.append(conversation["llm_ratings"])
        response.append(conversation["response"])
        response_ratings.append(conversation["response_ratings"])


# get the differences in ratings

valence_diffs, arousal_diffs, literal_diffs = [], [], []
for i in range(len(ratings)):
    valence_diffs.append(llm_ratings[i][0] - ratings[i][0])
    arousal_diffs.append(llm_ratings[i][1] - ratings[i][1])
    literal_diffs.append(llm_ratings[i][2] - ratings[i][2])

valence_avg = sum(valence_diffs) / len(valence_diffs)
arousal_avg = sum(arousal_diffs) / len(arousal_diffs)
literal_avg = sum(literal_diffs) / len(literal_diffs)
print(f"Average Valence Difference: {valence_avg}")
print(f"Average Arousal Difference: {arousal_avg}")
print(f"Average Literal Difference: {literal_avg}")
print(
    f"Standard Deviations: {statistics.stdev(valence_diffs)}, {statistics.stdev(arousal_diffs)}, {statistics.stdev(literal_diffs)}")

for i in range(len(ratings)):
    valence_diffs.append(response_ratings[i][0] - ratings[i][0])
    arousal_diffs.append(response_ratings[i][1] - ratings[i][1])
    literal_diffs.append(response_ratings[i][2] - ratings[i][2])

valence_avg = sum(valence_diffs) / len(valence_diffs)
arousal_avg = sum(arousal_diffs) / len(arousal_diffs)
literal_avg = sum(literal_diffs) / len(literal_diffs)
print(f"Average Valence Difference: {valence_avg}")
print(f"Average Arousal Difference: {arousal_avg}")
print(f"Average Literal Difference: {literal_avg}")
print(
    f"Standard Deviations: {statistics.stdev(valence_diffs)}, {statistics.stdev(arousal_diffs)}, {statistics.stdev(literal_diffs)}")

for i in range(len(ratings)):
    valence_diffs.append(response_ratings[i][0] - llm_ratings[i][0])
    arousal_diffs.append(response_ratings[i][1] - llm_ratings[i][1])
    literal_diffs.append(response_ratings[i][2] - llm_ratings[i][2])

valence_avg = sum(valence_diffs) / len(valence_diffs)
arousal_avg = sum(arousal_diffs) / len(arousal_diffs)
literal_avg = sum(literal_diffs) / len(literal_diffs)
print(f"Average Valence Difference: {valence_avg}")
print(f"Average Arousal Difference: {arousal_avg}")
print(f"Average Literal Difference: {literal_avg}")
print(
    f"Standard Deviations: {statistics.stdev(valence_diffs)}, {statistics.stdev(arousal_diffs)}, {statistics.stdev(literal_diffs)}")
