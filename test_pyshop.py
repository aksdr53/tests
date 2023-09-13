from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 100

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):
    if (
        not game_stamps or not isinstance(game_stamps, list)
        or offset > game_stamps[-1]['offset'] or offset < 0
    ):
        raise ValueError('Offset вне диапозона')
    offset = math.floor(offset)
    for i in range(offset // OFFSET_MAX_STEP, offset):
        if game_stamps[i]['offset'] <= offset:
            offset_stamp = game_stamps[i]
        else:
            break
    home = offset_stamp['score']['home']
    away = offset_stamp['score']['away']
    return home, away


if __name__ == "__main__":
    game_stamps = generate_game()

    pprint(game_stamps)