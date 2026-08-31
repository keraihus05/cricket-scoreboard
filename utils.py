def find_player(query, players):
    """
    Match typed input against a list of Player objects.

    Accepts either the player's full name or a single part of it
    (e.g. just the surname, or just the first name).

    Returns the matching Player, or None if there's no match or
    the query is ambiguous (matches more than one player).
    """
    query = query.lower().strip()
    if not query:
        return None

    # Exact full-name match wins first
    for player in players:
        if player.name.lower() == query:
            return player

    # Otherwise match on any single word in the name (surname, first name...)
    matches = [
        player for player in players
        if query in [part.lower() for part in player.name.split()]
    ]

    if len(matches) == 1:
        return matches[0]

    if len(matches) > 1:
        names = ", ".join(p.name for p in matches)
        print(f"'{query}' matches more than one player ({names}) - be more specific.")
        return None

    return None
