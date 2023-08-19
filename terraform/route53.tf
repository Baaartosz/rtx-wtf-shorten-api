resource "aws_route53_zone" "rtx_wtf" {
  name = "rtx.wtf"
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.rtx_wtf.zone_id
  name    = "shorten.rtx.wtf"
  type    = "A"

  alias {
    evaluate_target_health = true
    name                   = aws_apigatewayv2_domain_name.shorten_api_domain_name.domain_name_configuration[0].target_domain_name
    zone_id                = aws_apigatewayv2_domain_name.shorten_api_domain_name.domain_name_configuration[0].hosted_zone_id
  }
}