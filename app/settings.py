class Settings:
    project_name: str = "Basketball Statistics API"
    version: str = "1.0.0"
    sqlalchemy_url: str = "sqlite://"
    csv_source_file: str = "res/L9HomeworkChallengePlayersInput.csv"


settings = Settings()
