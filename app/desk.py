def schedule(counts, targets, assignments):
    outstanding = []
    for topic, groups in targets.items():
        for group, target in groups.items():
            sent = sum(1 for row in assignments if (row['topic'], row['group'], row['state']) == (topic, group, 'sent'))
            gap = target - counts.get(topic, {}).get(group, 0) - sent
            if gap > 0:
                outstanding.append({'topic': topic, 'group': group, 'gap': gap})
    return {'sent': [row['id'] for row in assignments if row['state'] == 'sent'], 'outstanding': outstanding}
