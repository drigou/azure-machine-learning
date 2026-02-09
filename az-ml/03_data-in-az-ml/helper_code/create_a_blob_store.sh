
STORAGE_ACCOUNT_NAME='dg123'
STORAGE_ACCOUNT_CONTAINER_NAME='csvdata'

echo $(pwd)

# Check if container exists. If yes, delete. 
if az storage account show --name $STORAGE_ACCOUNT_NAME &>/dev/null; then
    echo "storage account with name ${STORAGE_ACCOUNT_NAME} already exists"
    echo '... start deleting'
    az storage account delete --name $STORAGE_ACCOUNT_NAME --yes
fi

# Create the azure storage account
echo "... Start creating storage account"
az storage account create --name $STORAGE_ACCOUNT_NAME --resource-group $AZURE_RESOURCE_GROUP \
    --kind BlobStorage \
    --location $AZURE_LOCATION \
    --access-tier Hot \
    --sku Standard_LRS &>/dev/null

# Get the account key
echo "... Get the account key"
ACCOUNT_KEY=$(az storage account keys list --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)

# Create the container
echo "... Create a container"
az storage container create --name csvdata \
    --account-key $ACCOUNT_KEY \
    --account-name $STORAGE_ACCOUNT_NAME &>/dev/null

# Upload a CSV
echo "... Upload a CSV"
az storage blob upload \
    --account-name $STORAGE_ACCOUNT_NAME \
    --account-key $ACCOUNT_KEY \
    --container-name $STORAGE_ACCOUNT_CONTAINER_NAME \
    --name "diabetes.csv" \
    --file "../../data/diabetes-data/diabetes.csv" &>/dev/null


# Create the SAS token
echo "... Create an SAS token"
SAS_TOKEN=$(az storage container generate-sas \
    --account-key=$ACCOUNT_KEY \
    --account-name dg123 \
    --name csvdata \
    --permissions rld \
    --expiry 2026-12-31T23:59:59Z \
    --output tsv)

# Create a new .env file
echo "... Create a new .env file"
CONTENT_DOTENV=$(cat ../../.env | grep -v AZURE_STORAGE_ACCOUNT | grep -v AZURE_SAS_TOKEN)
echo -e "${CONTENT_DOTENV}\nAZURE_STORAGE_ACCOUNT=${ACCOUNT_KEY}\nAZURE_SAS_TOKEN=${SAS_TOKEN}" > ../../.env

echo 'Done!'
