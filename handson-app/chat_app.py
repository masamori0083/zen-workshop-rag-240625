# こちらへの対応: https://github.com/microsoft/Oryx/issues/1774
try:
    import azure.functions as func
    from azure.cosmos import CosmosClient
    from openai import AzureOpenAI
    import os
    import json
except:
    pass

chat_app_bp = func.Blueprint()


@chat_app_bp.function_name(name="chat")
@chat_app_bp.route(route="chat", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def chat(req: func.HttpRequest) -> func.HttpResponse:

    # 質問の文章の取得: クエリ文字列 query の値
    # 質問の文章がない場合はエラーにする
    # ベクター検索の結果を取得
    # ベクター検索の結果をもとに回答を生成
    return func.HttpResponse("Hello from CHAT")
