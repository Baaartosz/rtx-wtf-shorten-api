resource "aws_dynamodb_table" "rtx_wtf_shorten_urls" {
  name = "rtx-wtf-shorten-urls"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"

  point_in_time_recovery {
    enabled = true
  }

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "owner"
    type = "S"
  }

  global_secondary_index {
    name               = "OwnerIndex"
    hash_key           = "owner"
    projection_type    = "ALL"
  }
}