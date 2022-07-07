from main import Vamstar_challenge



def test_random_values():
    assert Vamstar_challenge.random_values


def test_data_gen_and_filtering():
    assert Vamstar_challenge.data_gen_and_filtering


def test_bmi_category_count():
    assert Vamstar_challenge.bmi_category_count


def test_bmi_category():
    assert Vamstar_challenge.bmi_category


def test_health_risk():
    assert Vamstar_challenge.health_risk


def test_file_creation():
    assert Vamstar_challenge.file_creation
