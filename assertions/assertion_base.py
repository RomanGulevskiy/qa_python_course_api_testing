def assert_schema(response, model):
    body = response.json()
    if isinstance(body, list):
        for item in body:
            model.model_validate(item)
    else:
        model.model_validate(body)
