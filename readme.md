# Setup of azure ML environment

Structure of environment (horizontal modularization)
```
|_ modules
    |_ base 
        |_ main.tf
        |_ outputs.tf
        |_ variables.tf
    |_ machine_learning
        |_ main.tf
        |_ outputs.tf
        |_ variables.tf
|_ main.tf
|_ outputs.tf
|_ variables.tf
```

The ```base``` and the ```machine_learning``` module are examples of horizontal modularization. First all the dependencies are created in the ```base``` module. The ```machine_learning``` module contains all the specific azure ML code. 

### Azure ML

To work with Azure ML in the CLI. Download the ml extension for azure
```bash
az extension add -n ml
```

> After destroying an environment the workspace will be soft deleted. If you want to force permanent deletion you have to find a way in the CLI (does not seem straight forward), or do it through the portal. 

> Note that you can also manually restore the environment (can be handy if you had a lot of assets in there.)

