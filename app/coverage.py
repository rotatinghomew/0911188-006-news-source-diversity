from collections import defaultdict


def groups(articles, accepted):
    counts = defaultdict(set)
    for citation in accepted:
        counts[(articles[citation['article']]['topic'], citation['group'])].add(citation['source'])
    result = {}
    for (topic, group), sources in sorted(counts.items()):
        result.setdefault(topic, {})[group] = len(sources)
    return result
