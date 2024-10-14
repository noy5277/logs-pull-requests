data "aws_caller_identity" "current" {}

resource "aws_sqs_queue" "pr_trigger" {
  name = "pr-trigger"

  policy = jsonencode({
    "Version"   : "2012-10-17",
    "Statement" : [
      {
        "Effect"   : "Allow",
        "Principal": { "AWS": "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root" },
        "Action"   : "sqs:*",
        "Resource" : "arn:aws:sqs:us-west-2:${data.aws_caller_identity.current.account_id}:pr-trigger"
      }
    ]
  })
}