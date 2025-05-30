
from lib.models.driver import Driver
from lib.models.team import Team
from lib.models.race import Race

def test_create_and_save_driver():
    driver = Driver(name="Lewis Hamilton", nationality="British")
    driver.save()
    
    assert driver.id is not None

def test_find_by_id():
    driver = Driver(name="Max Verstappen", nationality="Dutch")
    driver.save()

    found = Driver.find_by_id(driver.id)
    assert found is not None
    assert found.name == "Max Verstappen"

def test_get_races_for_driver():
    # Create team and race
    mercedes = Team(name="Mercedes", country="Germany")
    mercedes.save()

    monaco_gp = Race(name="Monaco GP", location="Monaco", date="2024-05-26")
    monaco_gp.save()

    # Add result
    driver = Driver(name="George Russell", nationality="British")
    driver.save()
    driver.add_race_result(mercedes.id, monaco_gp.id, position=3, points=15)
    races = driver.races()
    assert len(races) == 1
    assert races[0]['name'] == "Monaco GP"