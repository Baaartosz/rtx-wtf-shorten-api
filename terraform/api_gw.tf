resource "aws_apigatewayv2_api" "shorten_http_api" {
  name          = "rtx-wtf-shorten-http-api"
  description   = "API for shortening URLs to user customizable short urls to be redirected via rtx.wtf"
  protocol_type = "HTTP"
  body          = data.template_file.api_spec_body.rendered
}

data "template_file" "api_spec_body" {
  template = file("../api/shorten-api.tpl")
  vars     = {
    shorten_service_lambda = aws_lambda_function.url_shorten_lambda.invoke_arn
    client_id = "7re6c9kmrbdbjmj3v33pnnls8s"
    user_pool_id = "eu-west-2_Wurx6FIUd"
    region = local.region
  }
}

resource "aws_apigatewayv2_stage" "shorten_http_api_stage" {
  api_id      = aws_apigatewayv2_api.shorten_http_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_apigatewayv2_domain_name" "shorten_api_domain_name" {
  domain_name = "shorten.rtx.wtf"

  domain_name_configuration {
    certificate_arn = aws_acm_certificate.shorten_api_certification.arn
    endpoint_type   = "REGIONAL"
    security_policy = "TLS_1_2"
  }
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.shorten_http_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.url_shorten_lambda.invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_api_mapping" "shorten_api_mapping" {
  api_id          = aws_apigatewayv2_api.shorten_http_api.id
  domain_name     = aws_apigatewayv2_domain_name.shorten_api_domain_name.id
  stage           = aws_apigatewayv2_stage.shorten_http_api_stage.name
  api_mapping_key = "api"
}