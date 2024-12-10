import matplotlib.pyplot as plt
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
valence_diffs2, arousal_diffs2, literal_diffs2 = [], [], []
valence_diffs3, arousal_diffs3, literal_diffs3 = [], [], []
for i in range(len(ratings)):
    valence_diffs.append(llm_ratings[i][0] - ratings[i][0])
    arousal_diffs.append(llm_ratings[i][1] - ratings[i][1])
    literal_diffs.append(llm_ratings[i][2] - ratings[i][2])
avg_valence_diff = statistics.mean(valence_diffs)
avg_arousal_diff = statistics.mean(arousal_diffs)
avg_literal_diff = statistics.mean(literal_diffs)

for i in range(len(ratings)):
    valence_diffs2.append(response_ratings[i][0] - ratings[i][0])
    arousal_diffs2.append(response_ratings[i][1] - ratings[i][1])
    literal_diffs2.append(response_ratings[i][2] - ratings[i][2])
avg_valence_diff2 = statistics.mean(valence_diffs2)
avg_arousal_diff2 = statistics.mean(arousal_diffs2)
avg_literal_diff2 = statistics.mean(literal_diffs2)

for i in range(len(ratings)):
    valence_diffs3.append(response_ratings[i][0] - llm_ratings[i][0])
    arousal_diffs3.append(response_ratings[i][1] - llm_ratings[i][1])
    literal_diffs3.append(response_ratings[i][2] - llm_ratings[i][2])
avg_valence_diff3 = statistics.mean(valence_diffs3)
avg_arousal_diff3 = statistics.mean(arousal_diffs3)
avg_literal_diff3 = statistics.mean(literal_diffs3)

# plot the differences

categories = ["Valence", "Arousal", "Literality"]
diffs = [avg_valence_diff, avg_arousal_diff, avg_literal_diff]
diffs2 = [avg_valence_diff2, avg_arousal_diff2, avg_literal_diff2]
diffs3 = [avg_valence_diff3, avg_arousal_diff3, avg_literal_diff3]

barWidth = 0.25
r1 = range(len(categories))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, diffs, color='b', width=barWidth,
        edgecolor='grey', label='LLM - User')
plt.bar(r2, diffs2, color='r', width=barWidth,
        edgecolor='grey', label='Response - User')
plt.bar(r3, diffs3, color='g', width=barWidth,
        edgecolor='grey', label='Response - LLM')

plt.xlabel('Categories', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(categories))], categories)
plt.legend()

plt.savefig("diffs.png")

plt.clf()

valence, arousal = [], []
for i in range(len(llm_ratings)):
    valence.append(llm_ratings[i][0])
    arousal.append(llm_ratings[i][1])

valence_arousal = list(zip(valence, arousal))
valence_arousal_counts = {}
for pair in valence_arousal:
    if pair in valence_arousal_counts:
        valence_arousal_counts[pair] += 1
    else:
        valence_arousal_counts[pair] = 1

for i in range(len(valence)):
    plt.scatter(valence[i], arousal[i])
    plt.text(valence[i], arousal[i],
             valence_arousal_counts[valence_arousal[i]])

plt.xlabel("Valence")
plt.ylabel("Arousal")

plt.savefig("scatterplot_llm.png")

plt.clf()

valence, arousal = [], []
for i in range(len(ratings)):
    valence.append(ratings[i][0])
    arousal.append(ratings[i][1])

valence_arousal = list(zip(valence, arousal))
valence_arousal_counts = {}
for pair in valence_arousal:
    if pair in valence_arousal_counts:
        valence_arousal_counts[pair] += 1
    else:
        valence_arousal_counts[pair] = 1

for i in range(len(valence)):
    plt.scatter(valence[i], arousal[i])
    plt.text(valence[i], arousal[i],
             valence_arousal_counts[valence_arousal[i]])

plt.xlabel("Valence")
plt.ylabel("Arousal")

plt.savefig("scatterplot_user.png")
