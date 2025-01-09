class LeaderboardPlugin:
    def __init__(self, contribution_handler):
        self.contribution_handler = contribution_handler

    def generate_leaderboard(self, top_n=10):
        """Generates a leaderboard of top contributors."""
        contributions = self.contribution_handler.get_all_contributions()
        leaderboard = {}
        for user_id, contribution_type, amount, _ in contributions:
            leaderboard[user_id] = leaderboard.get(user_id, 0) + amount
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        return sorted_leaderboard[:top_n]