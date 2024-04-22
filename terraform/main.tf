module "vertex_ai" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric/blueprints/data-solutions/vertex-mlops"

  # Configure the project
  project_config = {
    billing_account_id = "01351B-EF61D3-967E55"
    parent             = "organizations/642164415054"
    project_id         = "analytics-project-373621"
  }

  # Configure the Vertex AI notebooks
  notebooks = {
    "myworkbench" = {
      type = "USER_MANAGED"
    }
  }

  # Configure other optional variables
  prefix       = "hdd"
  region       = "us-east1"
  bucket_name  = "rimac_hdd"
  dataset_name = "rimac_hdd"

  # Configure labels
  labels = {
    "env"  = "dev"
    "team" = "ml"
  }
}