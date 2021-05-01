from database_connection import get_database_connection


class GameRepository():
    def __init__(self, connection) -> None:
        self.connection = connection

    def list_past_games(self):
        cursor = self.connection.cursor()
        # past_games =

    def get_win_amound(self):
        cursor = self.connection.cursor()
        wins = cursor.execute(
            "SELECT count(*) FROM games WHERE win_loss= ?", ["Win"]).fetchone()[0]
        return wins

    def get_lost_amound(self):
        cursor = self.connection.cursor()
        losses = cursor.execute(
            "SELECT count(*) FROM games WHERE win_loss= ?", ["Loss"]).fetchone()[0]
        return losses

    def add_game(self, timestamp, win_or_loss):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO games (timestamp, win_loss) VALUES (?, ?)", [timestamp, win_or_loss])


game_repo = GameRepository(get_database_connection())
