def review(rows, origins, article_ids):
    verified = {origin['id']: origin for origin in origins if origin['verification'] == 'confirmed'}
    accepted = []
    unresolved = []
    for row in rows:
        if row['article'] not in article_ids or row['state'] != 'active':
            continue
        origin = verified.get(row['source'])
        if origin is None:
            unresolved.append(row['id'])
        else:
            accepted.append({**row, 'group': origin['group']})
    return {'accepted': accepted, 'unresolved': unresolved}
