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
        (
            "Jaysee Nkrumah",
            {
                "playerName": "Jaysee Nkrumah",
                "gamesPlayed": 3,
                "traditional": {
                    "freeThrows": {
                        "attempts": 4.3,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "twoPoints": {
                        "attempts": 3.7,
                        "made": 3.7,
                        "shootingPercentage": 100.0,
                    },
                    "threePoints": {
                        "attempts": 4.0,
                        "made": 2.0,
                        "shootingPercentage": 50.0,
                    },
                    "points": 13.3,
                    "rebounds": 1.7,
                    "blocks": 0.7,
                    "assists": 0.7,
                    "steals": 1.7,
                    "turnovers": 1.3,
                },
                "advanced": {
                    "valorization": 10.3,
                    "effectiveFieldGoalPercentage": 87.0,
                    "trueShootingPercentage": 68.6,
                    "hollingerAssistRatio": 5.7,
                },
            },
        ),
        (
            "Nkosinathi Cyprian",
            {
                "playerName": "Nkosinathi Cyprian",
                "gamesPlayed": 2,
                "traditional": {
                    "freeThrows": {
                        "attempts": 4.5,
                        "made": 1.5,
                        "shootingPercentage": 33.3,
                    },
                    "twoPoints": {
                        "attempts": 7.5,
                        "made": 2.5,
                        "shootingPercentage": 33.3,
                    },
                    "threePoints": {
                        "attempts": 3.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "points": 6.5,
                    "rebounds": 5.5,
                    "blocks": 1.5,
                    "assists": 1.0,
                    "steals": 0.0,
                    "turnovers": 1.5,
                },
                "advanced": {
                    "valorization": 2.0,
                    "effectiveFieldGoalPercentage": 23.8,
                    "trueShootingPercentage": 25.7,
                    "hollingerAssistRatio": 6.6,
                },
            },
        ),
        (
            "Haji Nabulung",
            {
                "playerName": "Haji Nabulung",
                "gamesPlayed": 2,
                "traditional": {
                    "freeThrows": {
                        "attempts": 2.5,
                        "made": 1.5,
                        "shootingPercentage": 60.0,
                    },
                    "twoPoints": {
                        "attempts": 4.0,
                        "made": 2.0,
                        "shootingPercentage": 50.0,
                    },
                    "threePoints": {
                        "attempts": 2.0,
                        "made": 1.5,
                        "shootingPercentage": 75.0,
                    },
                    "points": 10.0,
                    "rebounds": 4.0,
                    "blocks": 0.5,
                    "assists": 3.5,
                    "steals": 1.5,
                    "turnovers": 2.0,
                },
                "advanced": {
                    "valorization": 14.0,
                    "effectiveFieldGoalPercentage": 70.8,
                    "trueShootingPercentage": 69.6,
                    "hollingerAssistRatio": 27.6,
                },
            },
        ),
        (
            "Pili Nkruma",
            {
                "playerName": "Pili Nkruma",
                "gamesPlayed": 2,
                "traditional": {
                    "freeThrows": {
                        "attempts": 8.5,
                        "made": 1.5,
                        "shootingPercentage": 17.6,
                    },
                    "twoPoints": {
                        "attempts": 13.5,
                        "made": 3.0,
                        "shootingPercentage": 22.2,
                    },
                    "threePoints": {
                        "attempts": 10.5,
                        "made": 1.5,
                        "shootingPercentage": 14.3,
                    },
                    "points": 12.0,
                    "rebounds": 0.5,
                    "blocks": 1.0,
                    "assists": 1.5,
                    "steals": 0.5,
                    "turnovers": 3.5,
                },
                "advanced": {
                    "valorization": -14.5,
                    "effectiveFieldGoalPercentage": 21.9,
                    "trueShootingPercentage": 21.4,
                    "hollingerAssistRatio": 4.5,
                },
            },
        ),
        (
            "Jawara Mekonnen",
            {
                "playerName": "Jawara Mekonnen",
                "gamesPlayed": 2,
                "traditional": {
                    "freeThrows": {
                        "attempts": 1.5,
                        "made": 1.5,
                        "shootingPercentage": 100.0,
                    },
                    "twoPoints": {
                        "attempts": 4.0,
                        "made": 3.5,
                        "shootingPercentage": 87.5,
                    },
                    "threePoints": {
                        "attempts": 1.5,
                        "made": 1.5,
                        "shootingPercentage": 100.0,
                    },
                    "points": 13.0,
                    "rebounds": 0.0,
                    "blocks": 0.5,
                    "assists": 2.5,
                    "steals": 1.0,
                    "turnovers": 0.5,
                },
                "advanced": {
                    "valorization": 16.0,
                    "effectiveFieldGoalPercentage": 104.5,
                    "trueShootingPercentage": 104.6,
                    "hollingerAssistRatio": 27.1,
                },
            },
        ),
        (
            "Sithembiso Komla",
            {
                "playerName": "Sithembiso Komla",
                "gamesPlayed": 2,
                "traditional": {
                    "freeThrows": {
                        "attempts": 2.0,
                        "made": 0.5,
                        "shootingPercentage": 25.0,
                    },
                    "twoPoints": {
                        "attempts": 3.0,
                        "made": 2.5,
                        "shootingPercentage": 83.3,
                    },
                    "threePoints": {
                        "attempts": 1.5,
                        "made": 0.5,
                        "shootingPercentage": 33.3,
                    },
                    "points": 7.0,
                    "rebounds": 1.5,
                    "blocks": 0.0,
                    "assists": 0.0,
                    "steals": 0.5,
                    "turnovers": 2.0,
                },
                "advanced": {
                    "valorization": 4.0,
                    "effectiveFieldGoalPercentage": 72.2,
                    "trueShootingPercentage": 64.2,
                    "hollingerAssistRatio": 0.0,
                },
            },
        ),
        (
            "Kodzo Danso",
            {
                "playerName": "Kodzo Danso",
                "gamesPlayed": 1,
                "traditional": {
                    "freeThrows": {
                        "attempts": 1.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "twoPoints": {
                        "attempts": 2.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "threePoints": {
                        "attempts": 1.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "points": 0.0,
                    "rebounds": 2.0,
                    "blocks": 3.0,
                    "assists": 3.0,
                    "steals": 1.0,
                    "turnovers": 1.0,
                },
                "advanced": {
                    "valorization": 4.0,
                    "effectiveFieldGoalPercentage": 0.0,
                    "trueShootingPercentage": 0.0,
                    "hollingerAssistRatio": 40.1,
                },
            },
        ),
        (
            "Aboki Siyabonga",
            {
                "playerName": "Aboki Siyabonga",
                "gamesPlayed": 1,
                "traditional": {
                    "freeThrows": {
                        "attempts": 0.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "twoPoints": {
                        "attempts": 0.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "threePoints": {
                        "attempts": 0.0,
                        "made": 0.0,
                        "shootingPercentage": 0.0,
                    },
                    "points": 0.0,
                    "rebounds": 0.0,
                    "blocks": 0.0,
                    "assists": 0.0,
                    "steals": 0.0,
                    "turnovers": 0.0,
                },
                "advanced": {
                    "valorization": 0.0,
                    "effectiveFieldGoalPercentage": 0.0,
                    "trueShootingPercentage": 0.0,
                    "hollingerAssistRatio": 0.0,
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
