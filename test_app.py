from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element('#header')

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element('#sales-linechart')

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element("#region-selector")

    radio_buttons = dash_duo.find_elements("input[type='radio']")
    assert len(radio_buttons) == 5

    labels = dash_duo.find_elements("label")
    selected = [b for b in radio_buttons if b.is_selected()][0]
    index = radio_buttons.index(selected)
    selected_label = labels[index].text
    assert selected_label == "All regions"
