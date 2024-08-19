from zones import Zone

def create_zone(zone_data):
    zone = Zone(zone_data['name'])
    if 'cards' in zone_data:
        zone.resources = zone_data['cards']
    elif 'opportunities' in zone_data:
        zone.resources = zone_data['opportunities']
    elif 'game_elements' in zone_data:
        zone.resources = zone_data['game_elements']
    elif 'gold' in zone_data and 'prestige' in zone_data:
        zone.resources = {'gold': zone_data['gold'], 'prestige': zone_data['prestige']}
    return zone
