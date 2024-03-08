output "lambda_invoke_arn" {
  value = aws_lambda_function.url_shorten_lambda.invoke_arn
}