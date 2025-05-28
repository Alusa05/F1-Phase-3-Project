from lib.models.driver import Driver
from lib.models.team import Team
from lib.models.race import Race

def seed_data():
    # Create teams
    mercedes = Team(name="Mercedes", country="Germany")
    mercedes.save()

    ferrari = Team(name="Ferrari", country="Italy")
    ferrari.save()

    # Create drivers
    hamilton = Driver("Lewis Hamilton", "British")
    hamilton.save()

    leclerc = Driver("Charles Leclerc", "Monegasque")
    leclerc.save()

    # Create races 
    monaco_gp = Race("Monaco GP", "Monaco", "2024-05-26")
    monaco_gp.save()

    # Add race results
    hamilton.add_race_result(mercedes.id, monaco_gp.id, position=1, points=25)
    leclerc.add_race_result(ferrari.id, monaco_gp.id, position=2, points=18)