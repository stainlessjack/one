from zone import Zone

class Owner:
    name = ""
    type = ""
    is_human = False
    zones = []

    @classmethod
    def setup_system(cls):
        cls.name = "System"
        cls.type = "system"
        cls.is_human = False

        # Setup the system's zones
        day_deck = Zone.setup_deck()
        world_opportunities = Zone.setup_play_area()
        graveyard = Zone.setup_discard()
        market_deck = Zone.setup_deck()
        market_opportunities = Zone.setup_play_area()
        workyard_deck = Zone.setup_deck()
        workyard_opportunities = Zone.setup_play_area()

        cls.zones = [day_deck, world_opportunities, graveyard, market_deck, market_opportunities, workyard_deck, workyard_opportunities]
        return cls
    
    @classmethod
    def setup_player(cls, name, is_human):
        cls.name = name
        cls.type = "player"
        cls.is_human = is_human
        
        # Setup the player's zones
        player_characters = Zone.setup_play_area()
        hand = Zone.setup_hand()
        opportunities = Zone.setup_play_area()
        resources = Zone.setup_play_area()
        gold = Zone.setup_pool()
        prestige = Zone.setup_pool()

        cls.zones = [player_characters, hand, opportunities, resources, gold, prestige]
        return cls

