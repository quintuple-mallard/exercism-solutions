"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    edible_ghost = power_pellet_active and touching_ghost
    
    return edible_ghost
    


    


def score(touching_power_pellet, touching_dot):
    
    get_score = touching_power_pellet or touching_dot
    
    return get_score



def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    game_over = not power_pellet_active and touching_ghost
    return game_over


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    win_game = has_eaten_all_dots and ((power_pellet_active and touching_ghost) or (not touching_ghost)) #parantheses just for clarification
    return win_game
