# selenium_course_final_project
Final project of the course at Stepik platform: [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/syllabus)


Autotests implemented in frame of the project (using [Training site](http://selenium1py.pythonanywhere.com/)) are based on Page Object pattern. 



### Requirements
```
pytest==5.1.1
selenium==3.14.0
```

### Getting started
```
git clone https://github.com/hemerocallis/selenium_course_final_project.git
cd selenium_course_final_project
pip install -r requirements.txt 
```

## Running the tests

Command to run tests for review:
```
pytest -v --tb=line --language=en -m need_review
```

### More tests

Additionally the project includes autotests of two different pages for guests and registered users:

```
pytest -v --tb=line --language=en test_main_page.py
pytest -v --tb=line --language=en test_product_page.py
pytest -v --tb=line -m login_guest --language=en test_product_page.py
pytest -v --tb=line -m user_adds_to_basket --language=en test_product_page.py
```
