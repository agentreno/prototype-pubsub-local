# Provider setup
provider "google" {
  credentials = "${var.service_account_key_file}"
  project = "${var.project}"
  region = "${var.region}"
}

resource "google_pubsub_topic" "example" {
  name = "snyk-example-topic"
}

resource "google_pubsub_subscription" "example" {
  name = "snyk-example-subscription"
  topic = "${google_pubsub_topic.example.name}"

  message_retention_duration = "1200s"
  retain_acked_messages = true
  ack_deadline_seconds = 20
}

resource "local_file" "config" {
  filename = ".env"
  content = <<CONFIG
PROJECT_ID=${var.project}
TOPIC_NAME=${google_pubsub_topic.example.name}
SUB_NAME=${google_pubsub_subscription.example.name}
PUBSUB_EMULATOR_HOST=localhost:8085
CONFIG
}
