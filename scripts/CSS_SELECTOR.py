import time
from functions.CSS_SELECTOR import CSSSelector


def go():
    data = {
        'firstName': ['Gogy', 'Gogy2', 'Gogy3'],
        'lastName': ['Zhowzhowsh', 'Zhowzhowsh2', 'Zhowzhowsh3'],
        'userEmail': ['gogy@gmail.com', 'gogy2@gmail.com', 'gogy3@gmail.com'],
        'age': ['21', '22', '23'],
        'salary': ['1234', '1235', '1236'],
        'department': ['Selenium', 'Selenium2', 'Selenium3']
    }
    css = CSSSelector()
    css.go_to_elements()
    css.select_li(0)

    css.fill_form('userName', 'Gogy', 1)
    css.fill_form('userEmail', 'gogy@gmail.com', 2)
    css.fill_form('currentAddress', '213456gfdsaasd', 3)
    css.fill_form('permanentAddress', 'dsada', 4)
    css.submit_form()

    css.select_li(1)
    css.select_checkboxes()

    css.select_li(2)
    css.select_radiobuttons('yesRadio')
    css.select_radiobuttons('impressiveRadio')

    css.select_li(3)

    css.add_record()
    [css.fill_modal_form(k, v[0]) for k, v in data.items()]
    css.submit_form()

    css.add_record()
    [css.fill_modal_form(k, v[1]) for k, v in data.items()]
    css.submit_form()

    css.add_record()
    [css.fill_modal_form(k, v[2]) for k, v in data.items()]
    css.submit_form()

    css.select_count_records(5)
    css.next()
    css.delete_record_from_table(6)

    css.edit_record_from_table(3)
    css.clear_modal_form('salary')
    css.fill_modal_form('salary', '5000')
    css.submit_form()

    css.search_record('Alden')
    css.select_li(4)
    css.click_button()

    css.select_li(5)
    css.go_to_link('created')
    css.go_to_link('no-content')
    css.go_to_link('moved')
    css.go_to_link('bad-request')
    css.go_to_link('unauthorized')
    css.go_to_link('forbidden')
    css.go_to_link('invalid-url')

    css.select_li(6)
    css.click_on_link_by_text('Click Here for Valid Link')
    css.go_to_elements()
    css.select_li(6)
    css.click_on_link_by_text('Click Here for Broken Link')
    css.click_on_link_by_text('here')

    css.select_li_codes('200')
    css.click_on_link_by_text('here')

    css.select_li_codes('301')
    css.click_on_link_by_text('here')

    css.select_li_codes('404')
    css.click_on_link_by_text('here')

    css.select_li_codes('500')
    css.click_on_link_by_text('here')

    css.site()
    css.go_to_elements()
    css.select_li(7)
    css.upload_file('./media/main.jpg')
    css.download_file()

    css.select_li(8)
    time.sleep(8)