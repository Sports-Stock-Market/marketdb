# models

There are 4 models: `NBATeam`, `NBAPlayer`, `NFLTeam`, and `NFLPlayer`.

## Creating a model Instance

Feel free to use the actual constructor, but it is recommended to use the `new...` methods written in `marketdb.wrappers`, since they don't enforce order of parameters.

## Editing a model Instance

simply run the following code:
```
instance_name.field_name = new_value
Session.commit()
```

## Model Definitions:

### NBATeam

The `NBATeam` model has the following fields:
- `team_name :: String`
- `city :: String`
- `wins :: Int`
- `losses :: Int`
- `wins_lastYear :: Int`
- `losses_lastYear :: Int`
- `conference_standings :: Int`
- `playoff_odds :: Int`
- `starters_rating :: Float`
- `bench_rating :: Float`
- `points_for :: Int`
- `field_goal :: Int`
- `threePt_made :: Int`
- `free_throw :: Int`
- `offensive_rebounds :: Int`
- `defensive_rebounds :: Int`
- `assists :: Int`
- `turnovers :: Int`
- `plus_minus :: Float`
- `steals :: Int`
- `blocks :: Int`

### NBAPlayer

The `NBAPlayer` model has the following fields:
- `team :: NBATeam`
- `first_name :: String`
- `last_name :: String`
- `games_played :: Int`
- `games_started :: Int`
- `points :: Int`
- `field_goals_attemped :: Int`
- `field_goals_made :: Int`
- `threePt_attempted :: Int`
- `threePt_made :: Int`
- `freeThrows_attempted :: Int`
- `freeThrows_made :: Int`
- `assists :: Int`
- `turnovers :: Int`
- `def _rebounds :: Int`
- `off_rebounds :: Int`
- `plus_minus :: Float`
- `min_per_game :: Float`
- `win_share :: Int`
- `true_shooting_pct :: Float`
- `fouls :: Int`
- `blocks :: Int`

### NFLTeam

The `NFLTeam` model has the following fields:
- `city :: String`
- `team_name :: String`
- `wins :: Int`
- `losses :: Int`
- `wins_lastYear :: Int`
- `losses_lastYear :: Int`
- `ties_lastYear :: Int`
- `playoff_odds :: Float`
- `team_rating :: Float`
- `offense_rating :: Float`
- `qb_rating :: Float`
- `offensive_pointsFor :: Int`
- `yards_for :: Int`
- `touchdowns_for :: Int`
- `offensive_redzone_eff :: Float`
- `defense_rating :: Float`
- `yards_against :: Int`
- `points_against :: Int`
- `touchdowns_against :: Int`
- `sacks :: Int`
- `interceptions :: Int`
- `defensive_redzone_eff :: Float`
- `defensive_pointsFor :: Int`
- `defensive_eff :: Float`

### NFLPlayer

The `NFLPlayer` model has the following fields:
- `team :: NFLTeam`
- `position :: Int`
- `first_name :: String`
- `last_name :: String`
- `games_played :: Int`
- `games_started :: Int`
- `passing_completions :: Int`
- `pass_attempts :: Int`
- `passing_yards :: Int`
- `passing_touchdowns :: Int`
- `interceptions_against :: Int`
- `sacks_against :: Int`
- `fumbles_against :: Int`
- `qbr :: Float`
- `rushing_attempts :: Int`
- `rushing_yards :: Int`
- `rushing_touchdowns :: Int`
- `receiving_targets :: Int`
- `receptions :: Int`
- `receiving_yards :: Int`
- `receiving_touchdowns :: Int`
- `interceptions_for :: Int`
- `pick_sixes :: Int`
- `forces_fumbles_for :: Int`
- `fumble_recovery_for :: Int`
- `fumble_sixes :: Int`
- `passes_defended :: Int`
- `sacks_for :: Int`
- `total_tackles :: Int`
- `solo_tackles :: Int`
- `tackles_for_loss :: Int`
- `qb_hits :: Int`
- `fg_attempted :: Int`
- `fg_made :: Int`
- `longfg_attempted :: Int`
- `longfg_made :: Int`
- `xp_attemped :: Int`
- `xp_made :: Int`
- `punt_attempts :: Int`
- `punt_yards :: Int`
- `punt_returns :: Int`
- `punt_return_yards :: Int`
- `punt_return_touchdowns :: Int`
- `kick_returns :: Int`
- `kick_return_yards :: Int`
- `kick_return_touchdowns :: Int`
