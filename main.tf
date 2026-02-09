# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"

}

provider "azurerm" {
  features {}
}

# Get the tennant id information
data "azurerm_client_config" "current" {}

# Define the azure resource group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.azure_location
}

module "base_infrastructure" {
    source                  = "./modules/base"
    resource_group_name     = azurerm_resource_group.rg.name
    location                = azurerm_resource_group.rg.location
    tenant_id               = data.azurerm_client_config.current.tenant_id
}

module "machine_learning" {
    source                  = "./modules/machine_learning"
    resource_group_name     = azurerm_resource_group.rg.name
    location                = azurerm_resource_group.rg.location
    storage_account         = module.base_infrastructure.azure_storage_account_id
    key_vault               = module.base_infrastructure.azure_key_vault_id
    application_insights    = module.base_infrastructure.azure_application_insights_id
    container_registry      = module.base_infrastructure.azure_container_registry_id
}

