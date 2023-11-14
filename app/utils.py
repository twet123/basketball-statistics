def calculate_shooting_percentage(shots_made: int, shots_attempted: int) -> float:
    return shots_made / shots_attempted * 100


def calculate_points(
    free_throw_made: int, two_points_made: int, three_points_made: int
):
    return free_throw_made + 2 * two_points_made + 3 * three_points_made


def calculate_valorization(
    free_throw_made: int,
    two_points_made: int,
    three_points_made: int,
    rebounds: int,
    blocks: int,
    assists: int,
    steals: int,
    free_throw_attempted: int,
    two_points_attempted: int,
    three_points_attempted: int,
    turnovers: int,
):
    return (
        free_throw_made
        + 2 * two_points_made
        + 3 * three_points_made
        + rebounds
        + blocks
        + assists
        + steals
    ) - (
        free_throw_attempted
        - free_throw_made
        + two_points_attempted
        - two_points_made
        + three_points_attempted
        - three_points_made
        + turnovers
    )


def calculate_effective_fg_percentage(
    two_points_made: int,
    three_points_made: int,
    two_points_attempted: int,
    three_points_attempted: int,
):
    return (
        (two_points_made + three_points_made + 0.5 * three_points_made)
        / (two_points_attempted + three_points_attempted)
        * 100
    )


def calculate_true_shooting_percentage(
    points: int,
    two_points_attempted: int,
    three_points_attempted: int,
    free_throw_attempted,
):
    return (
        points
        / (
            2
            * (
                two_points_attempted
                + three_points_attempted
                + 0.475 * free_throw_attempted
            )
        )
        * 100
    )


def calculate_hollinger_assist_ratio(
    assists: int,
    two_points_attempted: int,
    three_points_attempted: int,
    free_throw_attempted: int,
    turnovers: int,
):
    return (
        assists
        / (
            two_points_attempted
            + three_points_attempted
            + 0.475 * free_throw_attempted
            + assists
            + turnovers
        )
        * 100
    )
