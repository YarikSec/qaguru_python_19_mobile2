import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@allure.title('Android Wiki Search Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Поиск с главной страницы')
@allure.story('Поиск по слову Appium')
def test_search(android_management):

    with step('Type search'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.title('Android Wiki Article Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Поиск и открытие статьи в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Поиск с главной страницы')
@allure.story('Поиск по слову Appium и клик на первый результат')
def test_open_article(android_management):

    with step('Type search'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step('Open article'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.first.click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/closeButton')).click()
        browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Appium"]')
        )

@allure.title('Android Wiki Onboarding Test')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('Тестирование страницы "Getting Started" в приложении Wikipedia на Android')
@allure.label('owner', 'Yaroslav')
@allure.epic('Википедия мобильное приложение Android')
@allure.feature('Тестирование страницы "Getting Started"')
@allure.story('Тестирование страницы "Getting Started"')
def test_getting_started(android_management):

    with ((step('Open second page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))

    with ((step('Open third page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))

    with ((step('Open fourth page'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Data & Privacy'))

    with ((step('Click get started'))):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')
                        ).should(have.text('Wikipedia games'))
