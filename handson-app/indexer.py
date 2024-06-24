try:
    import azure.functions as func
    from azure.cosmos import CosmosClient
    from openai import AzureOpenAI
    import logging
    import os
except:
    pass

indexer_bp = func.Blueprint()


@indexer_bp.function_name(name="upsert-data")
@indexer_bp.route(route="upsert", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def upsert(req: func.HttpRequest) -> func.HttpResponse:

    # Request body からデータを取得
    # content の内容をベクター化
    # Cosmos DB へ登録するスキーマへ変換
    # Cosmos DB へデータを登録
    return func.HttpResponse("Hello from indexer")
