resource "azurerm_machine_learning_workspace" "aml" {
  name                    = "aml-dg-associate-data-science"
  location                = var.location
  resource_group_name     = var.resource_group_name

  # Add all the prerequisite resources here with ID's
  application_insights_id = var.application_insights
  key_vault_id            = var.key_vault
  storage_account_id      = var.storage_account
  container_registry_id   = var.container_registry

  identity {
    type = "SystemAssigned"
  }
}


/*
resource "azurerm_machine_learning_compute_instance" "ci_01" {
  name                          = "dgml_compute_small"
  machine_learning_workspace_id = azurerm_machine_learning_workspace.aml.id
  location                      = var.location
  virtual_machine_size          = "STANDARD_DS2_V2"
} */
