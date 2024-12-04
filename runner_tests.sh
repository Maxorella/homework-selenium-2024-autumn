pytest hw/code/test_LK_audiences.py hw/code/test_LK_companies.py hw/code/test_LK_education.py hw/code/test_main_page_no_login.py hw/code/test_settings.py hw/code/test_sites.py --url https://ads.vk.com/ --debug_log
pytest hw/code/test_cases_page.py --url https://ads.vk.com/cases --debug_log
pytest hw/code/test_events_page.py --url https://ads.vk.com/events --debug_log
pytest hw/code/test_materials_page.py --url https://ads.vk.com/insights --debug_log
pytest hw/code/test_news_page.py --url https://ads.vk.com/news --debug_log
pytest hw/code/test_news_page.py --url https://ads.vk.com/news --debug_log



# правильный порядок
# pytest hw/code/test_cases_page.py --url https://ads.vk.com/cases --debug_log
  #pytest hw/code/test_events_page.py --url https://ads.vk.com/events --debug_log
  #pytest hw/code/test_LK_audiences.py --url https://ads.vk.com/ --debug_log
  #pytest hw/code/test_LK_companies.py --url https://ads.vk.com/ --debug_log
  #pytest hw/code/test_LK_education.py --url https://ads.vk.com/ --debug_log
  #pytest hw/code/test_main_page_no_login.py --url https://ads.vk.com/ --debug_log
  #pytest hw/code/test_materials_page.py --url https://ads.vk.com/insights --debug_log
  #pytest hw/code/test_news_page.py --url https://ads.vk.com/news --debug_log
  #pytest hw/code/test_settings.py --url https://ads.vk.com/ --debug_log
  #pytest hw/code/test_sites.py --url https://ads.vk.com/ --debug_log