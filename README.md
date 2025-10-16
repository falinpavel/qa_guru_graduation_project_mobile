![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24&height=200&section=header&text=QA%20GURU&fontAlignY=35&fontSize=60&desc=PROJECT%20MOBILE%20AUTO&descAlignY=60&descSize=50&animation=twinkling&fontColor=E9E9E9F3&descAlign=60&fontAlign=25
)

# <p  align="center"> Этот проект является дипломной работой по курсу QA.GURU в части построения фреймворка по MOBILE (Appium) автоматизации на примере приложения "Кинопоиск"

# <p  align="center"> В реализации использованы инструменты и библиотеки:

<p  align="center">
  <code><img width="6%" title="Pycharm" src="resources/github_readme/images/logo/pycharm.png" alt="pycharm"></code>
  <code><img width="6%" title="Python" src="resources/github_readme/images/logo/python.png" alt="python"></code>
  <code><img width="6%" title="Pytest" src="resources/github_readme/images/logo/pytest.png" alt="pytest"></code>
  <code><img width="6%" title="Selene" src="resources/github_readme/images/logo/selene.png" alt="selene"></code>
  <code><img width="6%" title="Selenium" src="resources/github_readme/images/logo/selenium.png" alt="selenium"></code>
  <code><img width="6%" title="GitHub" src="resources/github_readme/images/logo/github.png" alt="github"></code>
  <code><img width="6%" title="Allure Report" src="resources/github_readme/images/logo/allure_report.png" alt="allure"></code>
</p>

## <img width="3%" title="pycharm" src="resources/images/logo/pycharm.png"> Запуск тестов локально:

1) Клонировать репозиторий: git clone git@github.com:falinpavel/qa_guru_graduation_project_mobile.git
2) Установить зависимости (в проекте используется poetry): poetry init -> poetry install -> poetry env activate
3) На своей локальной машине запустить Appium сервер, выполнив команду "appium" в терминале
4) Запустить Android эмулятор
5) Запуск тестов с генерацией отчетов Allure: pytest (все параметры запуска зашиты в pyproject.toml)
6) Просмотр отчета Allure (если установлен Allure CLI): allure serve reports/allure-results

## <img width="3%" title="allure" src="resources/images/logo/allure_report.png"> Визуализация результатов в Allure Reports

## Allure отчет с результатами тестирования можно посмотреть выполнив команду: 

```bash
allure serve reports/allure-results
```