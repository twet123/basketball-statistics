from fastapi.testclient import TestClient
from parameterized import parameterized

from .main import app


@parameterized.expand(
    [
        (
            "Sifiso Abdalla",
            {
                "playerName": "Sifiso Abdalla",
                "gamesPlayed": 3,
                "traditional": {
                    "freeThrows": {
                        "attempts": 4.7,
                        "made": 3.3,
                        "shootingPercentage": 71.4,
                    },
                    "twoPoints": {
                        "attempts": 4.7,
                        "made": 3.0,
                        "shootingPercentage": 64.3,
                    },
                    "threePoints": {
                        "attempts": 6.3,
                        "made": 1.0,
                        "shootingPercentage": 15.8,
                    },
                    "points": 12.3,
                    "rebounds": 5.7,
                    "blocks": 1.7,
                    "assists": 0.7,
                    "steals": 1.0,
                    "turnovers": 1.3,
                },
                "advanced": {
                    "valorization": 11.7,
                    "effectiveFieldGoalPercentage": 40.9,
                    "trueShootingPercentage": 46.7,
                    "hollingerAssistRatio": 4.4,
                },
            },
        ),
        (
            "Luyanda Yohance",
            {
                "playerName": "Luyanda Yohance",
                "gamesPlayed": 1,
                "traditional": {
                    "freeThrows": {
                        "attempts": 6.0,
                        "made": 6.0,
                        "shootingPercentage": 100.0,
                    },
                    "twoPoints": {
                        "attempts": 4.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "threePoints": {
                        "attempts": 4.0,
                        "made": 4.0,
                        "shootingPercentage": 100.0,
                    },
                    "points": 18.0,
                    "rebounds": 1.0,
                    "blocks": 1.0,
                    "assists": 4.0,
                    "steals": 2.0,
                    "turnovers": 2.0,
                },
                "advanced": {
                    "valorization": 20.0,
                    "effectiveFieldGoalPercentage": 75.0,
                    "trueShootingPercentage": 82.9,
                    "hollingerAssistRatio": 23.7,
                },
            },
        ),
    ]
)
def test_get_player_statistics(player_name: str, json_response):
    with TestClient(app) as client:
        response = client.get(f"/stats/player/{player_name}")
        assert response.status_code == 200
        assert response.json() == json_response


def test_non_existing_player():
    with TestClient(app) as client:
        response = client.get(f"/stats/player/Vladimir Popov")
        assert response.status_code == 404
