resource "aws_lambda_function" "url_shorten_lambda" {
  function_name = "rtx-wtf-url-shorten-handler"

  filename = "../url-shorten-handler/url-shorten-handler.zip"
  source_code_hash = filebase64sha256("../url-shorten-handler/url-shorten-handler.zip")

  memory_size = "1536"
  # "main" is the filename within the zip file (main.js) and "handler"
  # is the name of the property under which the handler function was
  # exported in that file.
  handler = "url_shorten_handler/handler.lambda_handler"
  runtime = "python3.11"

  role = aws_iam_role.function_role.arn

  environment {
    variables = {
      SHORTEN_URLS_TABLE = aws_dynamodb_table.rtx_wtf_shorten_urls.name
    }
  }
}

resource "aws_cloudwatch_log_group" "function_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.url_shorten_lambda.function_name}"
  retention_in_days = 7
  lifecycle {
    prevent_destroy = false
  }
}

resource "aws_iam_role_policy_attachment" "function_logging_policy_attachment" {
  role = aws_iam_role.function_role.id
  policy_arn = aws_iam_policy.function_logging_policy.arn
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.url_shorten_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  # The /*/* portion grants access from any method on any resource
  # within the API Gateway "REST API".
  source_arn = "${aws_apigatewayv2_api.shorten_http_api.execution_arn}/*/*"
}