# こちらへの対応: https://github.com/microsoft/Oryx/issues/1774
try:
    import azure.functions as func
    from chat_app import chat_app_bp
    from indexer import indexer_bp
except:
    pass

app = func.FunctionApp()

app.register_functions(indexer_bp)
app.register_functions(chat_app_bp)
