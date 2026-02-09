output azure_machine_learning_workspace_name {
    value       = azurerm_machine_learning_workspace.aml.name
    description = "Name of the azure machine learning workspace"
}

output azure_machine_learning_workspace_id {
    value       = azurerm_machine_learning_workspace.aml.id
    description = "ID of the azure machine learning workspace"
}