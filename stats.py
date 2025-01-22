def make_stats_dict():
    with open("stats", 'r') as file:
        content = file.read()
    learning = content.split(',')
    for i in range(len(learning)):
        learning[i] = learning[i].split('=')
        learning[i][1] = learning[i][1].split('/')
    stats_dict = dict()
    for ele in learning:
        stats_dict[ele[0]] = [int(ele[1][0]), int(ele[1][1])]
    return stats_dict


def write_stats(stats_dict):
    file_content = ""
    for word, stats in stats_dict.items():
        file_content += f"{word}={stats[0]}/{stats[1]},"
    with open("stats", 'w') as file:
        file.write(file_content[:-1])