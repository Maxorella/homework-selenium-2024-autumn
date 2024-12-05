#pytest hw/code/test_LK_audiences.py hw/code/test_LK_companies.py hw/code/test_LK_education.py hw/code/test_main_page_no_login.py hw/code/test_settings.py hw/code/test_sites.py --url https://ads.vk.com/ --debug_log
#pytest hw/code/test_cases_page.py --url https://ads.vk.com/cases --debug_log
#pytest hw/code/test_events_page.py --url https://ads.vk.com/events --debug_log
#pytest hw/code/test_materials_page.py --url https://ads.vk.com/insights --debug_log
#pytest hw/code/test_news_page.py --url https://ads.vk.com/news --debug_log



pytest hw/code/test_cases_page.py --url https://ads.vk.com/cases --debug_log
pytest hw/code/test_companies.py hw/code/test_companies_advertise_group.py hw/code/test_companies_site.py hw/code/test_companies_target_actions.py hw/code/test_LK_audiences.py hw/code/test_LK_education.py hw/code/test_login.py hw/code/test_main_page_carousel.py hw/code/test_main_page_cases.py hw/code/test_main_page_cookie.py hw/code/test_main_page_educate.py hw/code/test_main_page_footer.py hw/code/test_main_page_navigation.py hw/code/test_settings.py hw/code/test_sites.py  --url https://ads.vk.com/ --debug_log
pytest hw/code/test_main_page_news.py --url https://ads.vk.com/news --debug_log
pytest hw/code/test_materials_page.py --url https://ads.vk.com/insights --debug_log
pytest hw/code/test_news_page.py --url https://ads.vk.com/news --debug_log
pytest hw/code/test_events_page.py --url https://ads.vk.com/events --debug_log


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