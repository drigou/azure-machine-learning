output azure_storage_account_id {
    value       = azurerm_storage_account.ml_storage_account.id
    description = "Id of the azure storage account"
}

output azure_key_vault_id {
    value           = azurerm_key_vault.ml_key_vault.id
    description     = "The azure region for the resources"
}

output azure_application_insights_id {
    value       = azurerm_application_insights.ml_application_insight.id
    description = "Id of the azure storage account"
}

output azure_container_registry_id {
    value       = azurerm_container_registry.acr.id
    description = "Id of the azure container registry"
}