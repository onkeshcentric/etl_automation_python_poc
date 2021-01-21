from allure_behave.hooks import allure_report

def before_all(context):
    print("inside before all")
    context.connection = {}
    context.count = {}

def after_all(context):
    print("inside after all")
    allure_report('../reports')