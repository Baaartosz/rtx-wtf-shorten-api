resource "aws_apigatewayv2_api" "shorten_http_api" {
  name          = "shorten-http-api"
  protocol_type = "HTTP"
  body          = data.template_file.api_spec_body.rendered
}

data "template_file" "api_spec_body" {
  template = file("../api/shorten-api.tpl")
  vars     = {
    lambda_function_uri = aws_lambda_function.url_shorten_lambda.invoke_arn
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

resource "aws_apigatewayv2_api_mapping" "shorten_api_mapping" {
  api_id          = aws_apigatewayv2_api.shorten_http_api.id
  domain_name     = aws_apigatewayv2_domain_name.shorten_api_domain_name.id
  stage           = aws_apigatewayv2_stage.shorten_http_api_stage.name
  api_mapping_key = "api"
}