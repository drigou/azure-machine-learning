# Intro to terraform.

Collecting some information on terraform. 
https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build

You need a service principle in Azure/AWS/...
Put the environment variables in a variables.tf file somewhere. 

## BUILD


Initialise terraform within the directory.
```bash
terraform init
```

To format terraform files. Recommended to use consistent formatting. This command will automatically do that. 
```bash
terraform init
```

Use these commands to make terraform think about what it will do and to validate that the code is consistent. 
```bash
terraform plan
terraform validate
```

Apply the configuration. You need to answer yes to tell terraform you agree with what it will do. 
terraform will write the resulting to a terraform.tfstate file. This will show the resources and id's. 
This should be stored remotely to enable colaboration. You can also check the state with the ```show``` command. 
Also the ```state list``` command will do that. 
```bash
terraform apply
terraform show
terraform state list
```



## CHANGE

When changing resources you can just do ```terraform apply```.


## DESTROY

You can do ```terraform destroy``` to delete all the resources. 

## VARIABLES

You can add variables in a ```variables.tf``` file. You can use the variables in the ```main.tf``` file. 
You can also override variables as follows:
```bash
terraform apply -var "resource_group_name=NewNameForTFResourceGroup"
```

When you already had an active resource_group. This command will be destructive. It will destroy the current resource and dependencies and recreate. 

## OUTPUTS

When building complex infrastructure, Terraform stores hundreds or thousands of attribute values for all your resources. As a user of Terraform, you may only be interested in a few values of importance. Outputs designate which data to display. This data is outputted when apply is called, and can be queried using the ```terraform output``` command.

## REMOTE STATE

In production environments you will need a remote server to execute these commands. This way you avoid two people at the same time trying to run ```terraform apply```.
Also the ```terraform.tfstate``` is stored remotely. Hence, there can be no confusion between states. HCP terraform bundles these two aspects. 

Another way of setting it up would be:
- Use S3/Azure blob storage or any cloud storage for the state file. 
- Use DynamoDB just as a service to check out the log.
- Use git to store all the ```.tf``` files. 