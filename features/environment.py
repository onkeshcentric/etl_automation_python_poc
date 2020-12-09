def before_all(context):
    print("inside before all")
    context.connection = {}
    context.count = {}
