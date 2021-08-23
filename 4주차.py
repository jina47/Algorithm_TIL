def solution(table, languages, preference):
    job = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    table = [list(reversed(t.split()[1:])) for t in table]

    scores = {}
    n = 0
    while n != len(table):
        score = 0
        for i in range(5):
            for j, l in enumerate(languages):
                if l == table[n][i]:
                    score += (i+1)*preference[j]
        scores[job[n]] = score
        n += 1

    scores = sorted(sorted(scores.items()), key=lambda x :x[1], reverse=True)
    return scores[0][0]