resource "tls_private_key" "repository_deploy_key" {
  algorithm = "RSA"
}

# Add the ssh key as a deploy key
resource "github_repository_deploy_key" "repository_deploy_key" {
  title      = "Repository Developer key"
  repository = var.repo_name
  key        = tls_private_key.repository_deploy_key.public_key_openssh
  read_only  = false
}

resource "github_actions_secret" "aws_access_key" {
  repository       = var.repo_name
  secret_name      = "aws_access_key"
  plaintext_value  = var.aws_access_key
}

resource "github_actions_secret" "aws_secret_key" {
  repository       = var.repo_name
  secret_name      = "aws_secret_key"
  plaintext_value  = var.aws_secret_key
}

resource "github_actions_secret" "github_token" {
  repository       = var.repo_name
  secret_name      = "cp_github_token"
  plaintext_value  = var.github_token
}

resource "github_repository_collaborator" "menahemo" {
  repository = var.repo_name
  username   = "menahemo@checkpoint.com"
  permission = "admin"
}

output "private_key" {
  value = tls_private_key.repository_deploy_key.private_key_pem
  sensitive = true
}
