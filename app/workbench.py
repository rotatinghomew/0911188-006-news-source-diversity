import json
from .citations import review
from .coverage import groups
from .desk import schedule
from .journal import packet


def run_workbench(action, directory, key, ledger):
    if action == 'brief' and key:
        return packet(ledger, 'desk', key)
    source = json.loads((directory / 'workbench.json').read_text())
    articles = {row['id']: row for row in source['articles'] if row['month'] == source['month']}
    citations = review(source['citations'], source['origins'], articles)
    if action == 'citations':
        return citations
    counts = groups(articles, citations['accepted'])
    if action == 'coverage':
        return counts
    tasks = schedule(counts, source['coverage_targets'], source['assignments'])
    return packet(ledger, 'desk', source['month'], {'coverage': counts, **tasks}) if action == 'brief' else tasks
