import time
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
    # xpath.select_li(0)
    #
    # xpath.fill_form('userName', 'Gogy', 1)
    # xpath.fill_form('userEmail', 'gogy@gmail.com', 2)
    # xpath.fill_form('currentAddress', '213456gfdsaasd', 3)
    # xpath.fill_form('permanentAddress', 'dsada', 4)
    # xpath.submit_form()
    #
    # xpath.select_li(1)
    # xpath.select_checkboxes()
    #
    # xpath.select_li(2)
    # xpath.select_radiobuttons('yesRadio')
    # xpath.select_radiobuttons('impressiveRadio')
    #
    # xpath.select_li(3)
    #
    # xpath.add_record()
    # [xpath.fill_modal_form(k, v[0]) for k, v in data.items()]
    # xpath.submit_form()
    #
    # xpath.add_record()
    # [xpath.fill_modal_form(k, v[1]) for k, v in data.items()]
    # xpath.submit_form()
    #
    # xpath.add_record()
    # [xpath.fill_modal_form(k, v[2]) for k, v in data.items()]
    # xpath.submit_form()
    #
    # xpath.select_count_records(5)
    # xpath.next()
    # xpath.delete_record_from_table(6)
    #
    # xpath.edit_record_from_table(3)
    # xpath.clear_modal_form('salary')
    # xpath.fill_modal_form('salary', '5000')
    # xpath.submit_form()
    #
    # xpath.search_record('Alden')
    # xpath.select_li(4)
    # xpath.click_button()

    # xpath.select_li(5)
    # xpath.go_to_link('created')
    # xpath.go_to_link('no-content')
    # xpath.go_to_link('moved')
    # xpath.go_to_link('bad-request')
    # xpath.go_to_link('unauthorized')
    # xpath.go_to_link('forbidden')
    # xpath.go_to_link('invalid-url')

    # xpath.select_li(6)
    # xpath.click_on_link_by_text('Click Here for Valid Link')
    # xpath.go_to_elements()
    xpath.select_li(6)
    xpath.click_on_link_by_text('Click Here for Broken Link')
    xpath.click_on_link_by_text('here')

    xpath.select_li_codes('200')
    xpath.click_on_link_by_text('here')

<<<<<<< HEAD
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

    xpath.select_li(5)
    xpath.go_to_link('created')
    xpath.go_to_link('no-content')
    xpath.go_to_link('moved')
    xpath.go_to_link('bad-request')
    xpath.go_to_link('unauthorized')
    xpath.go_to_link('forbidden')
    xpath.go_to_link('invalid-url')

    xpath.select_li(6)
    xpath.click_on_link_by_text('Click Here for Valid Link')
    xpath.go_to_elements()
    xpath.select_li(6)
    xpath.click_on_link_by_text('Click Here for Broken Link')
    xpath.click_on_link_by_text('here')

    xpath.select_li_codes('200')
    xpath.click_on_link_by_text('here')

    xpath.select_li_codes('301')
    xpath.click_on_link_by_text('here')

    xpath.select_li_codes('404')
    xpath.click_on_link_by_text('here')

    xpath.select_li_codes('500')
    xpath.click_on_link_by_text('here')

    xpath.site()
    xpath.go_to_elements()
    xpath.select_li(7)
    xpath.upload_file('./media/main.jpg')
    xpath.download_file()

    xpath.select_li(8)
    time.sleep(8)
=======
    # xpath.select_li_codes('301')
    # xpath.click_on_link_by_text('here')
    #
    # xpath.select_li_codes('404')
    # xpath.click_on_link_by_text('here')
    #
    # xpath.select_li_codes('500')
    # xpath.click_on_link_by_text('here')
>>>>>>> 99892094bd5b1e40cbfb5d47684642dc8ecaa05b
