output "azure_tenant_id" {
  value = data.azurerm_client_config.current.tenant_id
  description = "The tenant ID being used of the current Azure active directory"
}

output "azure_resource_group_name" {
    value = azurerm_resource_group.rg.name
    description = "Name of the created resource group in Azure"
}

output "azure_resource_group_id" {
    value = azurerm_resource_group.rg.id
    description = "Id of the created resource group in Azure"
}

/*
output "azure_storage_account_id" {
    value = module.base_infrastructure.azure_storage_account_id
    description = "Id of the azure storage account"
}
*/

output azure_machine_learning_workspace_name {
    value       = module.machine_learning.azure_machine_learning_workspace_name
    description = "Name of the azure machine learning workspace"
}

output azure_machine_learning_workspace_id {
    value       = module.machine_learning.azure_machine_learning_workspace_id
    description = "ID of the azure machine learning workspace"
}
