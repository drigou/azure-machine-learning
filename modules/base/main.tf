# Define the azurerm storage account
resource "azurerm_storage_account" "ml_storage_account" {
  name                     = "storageaccountmldg"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS" # => Locally redundant storage: three copies in one datacenter 
}

# Define the azure key vault
resource "azurerm_key_vault" "ml_key_vault" {
  name                      = "keyvaultmldg"
  location                  = var.location
  resource_group_name       = var.resource_group_name
  tenant_id                 = var.tenant_id
  sku_name                  = "standard"
  purge_protection_enabled  = true
}

# Create application insights resource
resource "azurerm_application_insights" "ml_application_insight" {
  name                = "appinsightsmldg"
  location            = var.location
  resource_group_name = var.resource_group_name
  application_type    = "web"   # Different options available which don't show up necessarily in the portal wizard. 
                                # Other options are java/other for java web applications or background services.
                                # When changing this a recreation will be forced. Any data in the current app will
                                # be deleted.  
}


# Create container registry
resource "azurerm_container_registry" "acr" {
  name                = "acrmldg"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Standard"
  admin_enabled       = true # Required for AML to authenticate
}
