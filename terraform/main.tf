terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = "./keys/terraform-demo-411110-8ef6da51b509.json"
  project     = "terraform-demo-411110"
  region      = "EUROPE-WEST2"
}

resource "google_storage_bucket" "demo-bucket" {
  name     = "homework-w2-411110-bucket"
  location = "EU"
  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}