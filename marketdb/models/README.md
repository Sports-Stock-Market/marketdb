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

## NBAPlayer

The `NBAPlayer` model has the following fields:
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