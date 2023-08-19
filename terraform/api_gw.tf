resource "aws_apigatewayv2_api" "shorten_http_api" {
  name          = "shorten-http-api"
  protocol_type = "HTTP"
  body          = file("../api/shorten-api.json")
}

resource "aws_apigatewayv2_domain_name" "shorten_api_domain_name" {
  domain_name = "shorten.rtx.wtf"

  domain_name_configuration {
    certificate_arn = aws_acm_certificate.shorten_api_certification.arn
    endpoint_type   = "REGIONAL"
    security_policy = "TLS_1_2"
  }
}

resource "aws_apigatewayv2_api_mapping" "shorten_api_mapping" {
  api_id          = aws_apigatewayv2_api.shorten_http_api.id
  domain_name     = aws_apigatewayv2_domain_name.shorten_api_domain_name.id
  stage           = "$default"
  api_mapping_key = "api"
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = "rtx-wtf-test-shorten-handler" ## TODO change to reference lambda function from internal terraform
  principal     = "apigateway.amazonaws.com"

  # The /*/* portion grants access from any method on any resource
  # within the API Gateway "REST API".
  source_arn = "${aws_apigatewayv2_api.shorten_http_api.execution_arn}/*/*"
}