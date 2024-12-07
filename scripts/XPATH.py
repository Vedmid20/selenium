from functions.XPATH import XPATH


def go():
    data = {
        'firstName': ['Gogy', 'Gogy2', 'Gogy3'],
        'lastName': ['Zhowzhowsh', 'Zhowzhowsh2', 'Zhowzhowsh3'],
        'userEmail': ['gogy@gmail.com', 'gogy2@gmail.com', 'gogy3@gmail.com'],
        'age': ['21', '22', '23'],
        'salary': ['1234', '1235', '1236'],
        'department': ['Selenium', 'Selenium2', 'Selenium3']
    }
    xpath = XPATH()
    xpath.go_to_elements()
    xpath.select_li(0)

    xpath.fill_form('userName', 'Gogy', 1)
    xpath.fill_form('userEmail', 'gogy@gmail.com', 2)
    xpath.fill_form('currentAddress', '213456gfdsaasd', 3)
    xpath.fill_form('permanentAddress', 'dsada', 4)
    xpath.submit_form()

    xpath.select_li(1)
    xpath.select_checkboxes()

    xpath.select_li(2)
    xpath.select_radiobuttons('yesRadio')
    xpath.select_radiobuttons('impressiveRadio')

    xpath.select_li(3)

    xpath.add_record()
    [xpath.fill_modal_form(k, v[0]) for k, v in data.items()]
    xpath.submit_form()

    xpath.add_record()
    [xpath.fill_modal_form(k, v[1]) for k, v in data.items()]
    xpath.submit_form()

    xpath.add_record()
    [xpath.fill_modal_form(k, v[2]) for k, v in data.items()]
    xpath.submit_form()

    xpath.select_count_records(5)
    xpath.next()
    xpath.delete_record_from_table(6)

    xpath.edit_record_from_table(3)
    xpath.clear_modal_form('salary')
    xpath.fill_modal_form('salary', '5000')
    xpath.submit_form()

    xpath.search_record('Alden')
    xpath.select_li(4)
    xpath.click_button()
