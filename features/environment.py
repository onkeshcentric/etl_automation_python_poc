from allure_behave.hooks import allure_report

def before_all(context):
    print("inside before all")
    context.connection = {}
    context.count = {}
    context.column_data={}
    context.remote=False

def after_all(context):
    print("inside after all")
    allure_report('../reports')