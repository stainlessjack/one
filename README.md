# Pain Rules
Welcome to our digital card game! Below you'll find the complete ruleset, including descriptions of the game flow, elements, and areas.

## Table of Contents
- [Introduction](#introduction)
- [Game Flow](#game-flow)
- [Game Elements](#game-elements)
- [Game Areas](#game-areas)
- [Victory Condition](#victory-condition)

## Introduction
In this strategic card game, players compete to gain **Prestige** by engaging in various **Opportunities** within a dynamic world. Manage your **Resources** wisely, outmaneuver your opponents, and be the first to reach the pinnacle of success!

## Game Flow
The game is structured around a repeating **Day** cycle, with each **Day** consisting of several key phases. Players must strategically engage with **Opportunities** and manage their **Resources** to progress toward victory.

### Day Cycle
1. **Start of Day**:
    - **Day Deck Check**: At the beginning of each **Day**, an **Opportunity** is drawn from the **Day Deck**, which is shuffled at the start of play. The **Opportunity** will specify a location, and it is placed in that location's **Opportunities Zone**.
    - **Maintenance**: Resolve any ongoing effects or temporary conditions from the previous **Day**. For example, a **Player Resource** might read: "At the Start of each Day: Gain 1 **Gold**." Update any **Tokens** or **Resources** as needed.
2. **Character Engagement**:
    - **Player Decision**: Each **Player** selects an **Opportunity** for their **Character** to engage with. **Players** can choose from any available **Opportunity** in the **player_area**, **market_area**, **workyard_area**, or **world_area** locations.
    - **Confirm Engagement**: **Players** make their selections simultaneously, confirming their choices without knowledge of the other **Player’s** decision.
    - **Reveal Choices**: Once confirmed, the engagements are revealed, showing where each **Player’s Character** has chosen to engage. There is no overlapping of **Opportunities**; each occupies a distinct place in its location's **Opportunities Zone**.
3. **Tick Clocks**:
    - **Clock Advancement**: All **Opportunities** with active **Clocks** tick down. **Opportunities** with **Clocks** that reach zero are resolved.
    - **Opportunity Resolution**:
        - **Contest Opportunities**: The **Player** who has **Dominance** over a majority of the **Obstacles** in the **Opportunity** Claims the **Consequences**. **Dominance** is determined by having more **Power** present at an **Obstacle**. If there is a tie in **Dominance**, total **Power** at the **Opportunity** is used to break the tie. If the tie persists, no **Player** is considered to have Claimed the **Opportunity**.
        - **Challenge Opportunities**: If the **Power Threshold** is met, the **Opportunity** is Claimed.
        - **Open Opportunities**: The **Player** who meets the **Resource** cost Claims the **Consequences**.
        - **Unclaimed Consequences**: If an **Opportunity** is not Claimed, any **Unclaimed Consequences** are applied as explicitly stated on the **Opportunity**. If there is no **Unclaimed Consequence**, the **Opportunity** is moved to the **world's graveyard**.
4. **End of Day**:
    - **Wrap-Up**: Trigger any end-of-day effects, such as resetting **Energy** or processing lingering effects.
    - **Cleanup**: Move Resolved **Opportunities** and Destroyed **Resources** to the **graveyard_zone**, removing them from play.
    - **Check for Victory**: After the **Cleanup** step, check if any **Player** has 10 or more **Prestige**. If multiple **Players** meet this condition, the **Player** with the most **Prestige** wins. If there's still a tie, the **Player** with the most **Gold** wins. If there's still a tie, the game continues. If the **Day Deck** is empty and there's still a tie, the game is considered a Tie.
    - **Prepare for Next Day**: Update the game state and prepare for the next **Day** cycle.

## Game Elements
The game revolves around managing various elements, including **Tokens**, **Characters**, and **Resources**, to engage with **Opportunities** and progress toward victory.

### Tokens
- **Energy**: A **Resource** used to perform actions by playing **Move Resources**.
- **Gold**: A currency used to engage with certain **Opportunities** or acquire new **Resources**.
- **Prestige**: The primary victory condition; **Players** aim to accumulate 10 **Prestige** to win the game.

### Characters
- **Trait Values**: Limit the amount of **Power** of each Type (Physical, Mental, Social) that can be played at a **Character’s** Engaged **Opportunity** in a single **Day**.
- **Energy Pool**: Most **Characters** have an **Energy Pool** with a maximum value of 6, used to play **Move Resources**.
- **Engagement**: **Characters** engage with **Opportunities** by allocating their available **Energy** and **Resources** to overcome **Obstacles** or fulfill requirements.

### Resources (Cards)
- **Moves**: Actions taken by **Characters**, played facedown to **Opportunities** and revealed upon resolution. After resolution, they return to the **Player's** hand.
- **Allies**: Individuals or entities that assist the **Character**. **Allies** are typically played to a **Player's Resource Zone** or directly to an **Opportunity**.
- **Objects**: Items or tools that provide benefits. **Objects** are also played to a **Player's Resource Zone** or to an **Opportunity**.
- **Acquisition**: **Moves** originate in each **Player’s** starting hand, while **Allies** and **Objects** are generally acquired as **Consequences** from **Opportunities**.
- **Transfer**: If a **Resource** changes **Zones**, it is referred to as a **Transfer**.

## Game Areas
The game board is divided into distinct areas, each consisting of various **Zones** where game elements are placed and managed.

### player_area(s)
- **hand_zone**: Where a **Player's** hand of **Resources** (cards) is kept.
- **token_zone**: Where **Tokens** such as **Energy**, **Gold**, and **Prestige** are stored.
- **unengaged_character_zone**: Where **Characters** wait when not engaged with an **Opportunity**.
- **opportunities_zone**: Where active **Opportunities** specific to the **Player** are located.
- **resource_zone**: Where **Allies** and **Objects** controlled by the **Player** are placed.

### market_area
- **market_deck_zone**: Holds the **Market Deck** from which **Opportunities** related to purchasing or trading are drawn.
- **market_opportunities_zone**: Where Market-related **Opportunities** are displayed.

### workyard_area
- **workyard_deck_zone**: Holds the **Workyard Deck**, where **Opportunities** related to labor and production are drawn.
- **workyard_opportunities_zone**: Where Workyard-related **Opportunities** are displayed.

### world_area
- **day_deck_zone**: Holds the **Day Deck**, from which global **Opportunities** or events are drawn each **Day**.
- **graveyard_zone**: The discard pile for Resolved **Opportunities** and Destroyed **Resources**, indicating that these elements are no longer in play.
- **world_opportunities_zone**: Where **Opportunities** from the **Day Deck** or global events are displayed.

## Victory Condition
The first **Player** to accumulate 10 **Prestige** wins the game. If no **Player** has 10 **Prestige** by the end of the tenth turn when the **Day Deck** is empty, the **Player** with the most **Prestige** wins. If there is still a tie, the **Player** with the most **Gold** wins. If there is still a tie, the game continues. If the **Day Deck** is empty and there's still a tie, the game is considered a Tie.
