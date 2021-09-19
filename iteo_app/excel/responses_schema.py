from drf_yasg import openapi

response_schema_dict = {
    "200": openapi.Response(
        description="Response body",
        examples={
            "application/json":  {
                    "file": "us trade price changes2011_nofc (1).xlsx",
                    "summary": [
                        {
                            "column": "CURRENT USD",
                            "sum": 18306.05,
                            "avg": 27.28
                        },
                        {
                            "column": "USD",
                            "sum": 2047.8,
                            "avg": 32.5
                        },
                        {
                            "column": "USD",
                            "sum": 2200.8,
                            "avg": 34.93
                        }
                    ]
            }
        }
    ),
    "400": openapi.Response(
        description="Error: Bad Request",
        examples={
            "application/json": [
                [
                    "Error info"
                ]
            ]
        }
    ),
}
