def scoreboard(scores):
    results = []

    for score in scores:
        total_score = ((score['wings'] * 5) + (score['burgers'] * 3) + (score['hotdogs'] * 2))
        name = score['name']

        outcome = {"name": name, "score":total_score}
        
        results.append(outcome)

    sorted_results = sorted(results, key=lambda results: results['score'], reverse=True)
    return sorted_results



participants = [
  {"name" : "Habanero Hillary", "wings" : 5 , "burgers": 17, "hotdogs": 11},
  {"name": "Big Bob" , "wings": 20, "burgers": 4, "hotdogs": 11},
  {"name": "Brian Kiprono" , "wings": 25, "burgers": 15, "hotdogs": 11}
]

print(scoreboard(participants))
