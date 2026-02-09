variable resource_group_name {
    type            = string
    description     = "The name of the existing resource type"
}

variable location {
    type            = string
    description     = "The location of the project"
}

variable storage_account {
    type            = string
    description     = "The id of the storage account needed to setup the AzureML env"
}

variable key_vault {
    type            = string
    description     = "The id of the key vault needed to setup the AzureML env"
}

variable application_insights {
    type            = string 
    description     = "The id of the application insights needed to setup the AzureML env"
}

variable container_registry {
    type            = string 
    description     = "The id of the container registry needed to setup the AzureML env"
}
