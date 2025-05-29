import pytest
from lib.models.driver import Driver 

def test_create_and_save_driver():
    driver = driver(name="Lewis Hamilton", nationality="British")
    driver.save()
    
    assert driver.id is not None

def test_find_by_id():
    driver = driver(name="Max Verstappen", nationality="Dutch")
    driver.save()

    found = driver.find_by_id(driver.id)
    assert found is not None
    assert found.name == "Max Verstappen"

def test_get_races_for_driver():
    # Create team and race
    from lib.models.team import Team
    from lib.models.race import Race

    mercedes = Team("Mercedes", "Germany")
    mercedes.save()

    monaco_gp = Race("Monaco GP", "Monaco", "2024-05-26")
    monaco_gp.save()

    # Add result
    driver = driver("George Russell", "British")
    driver.save()
    driver.add_race_result(mercedes.id, monaco_gp.id, position=3, points=15)

    races = driver.races()
    assert len(races) == 1
    assert races[0]['name'] == "Monaco GP"