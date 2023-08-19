resource "aws_acm_certificate" "shorten_api_certification" {
  domain_name       = "shorten.rtx.wtf"
  validation_method = "DNS"
}

resource "aws_route53_record" "cert-validations" {
  count = length(aws_acm_certificate.shorten_api_certification.domain_validation_options)

  zone_id = aws_route53_zone.rtx_wtf.zone_id
  name    = element(aws_acm_certificate.shorten_api_certification.domain_validation_options.*.resource_record_name, count.index)
  type    = element(aws_acm_certificate.shorten_api_certification.domain_validation_options.*.resource_record_type, count.index)
  records = [element(aws_acm_certificate.shorten_api_certification.domain_validation_options.*.resource_record_value, count.index)]
  ttl     = 60
}

resource "aws_acm_certificate_validation" "shorten_api_certificate_validation" {
  certificate_arn         = aws_acm_certificate.shorten_api_certification.arn
  validation_record_fqdns = aws_route53_record.cert-validations.*.fqdn
}