



import boto3
import csv

def write_account_types_to_csv():
    # Create a Boto3 client for AWS Organizations
    client = boto3.client('organizations')

    # Set the input parameters
    params = {
        'MaxResults': 10  # Update the MaxResults value to a lower value within the range
    }

    # Retrieve the list of accounts
    response = client.list_accounts(**params)

    # Create a CSV file and write the header
    with open('account_types.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Account ID', 'Account Name', 'Account Email', 'Account Type'])

        # Iterate over the accounts and write the details to the CSV file
        for account in response['Accounts']:
            account_id = account['Id']
            account_name = account['Name']
            account_email = account['Email']
            account_status = account['Status']
            account_joined_method = account['JoinedMethod']

            # Determine the account type
            account_type = ''
            if account_joined_method == 'INVITED':
                account_type = 'Invited'
            elif account_joined_method == 'CREATED':
                account_type = 'Created'
            else:
                account_type = 'Unknown'

            # Write the account details to the CSV file
            writer.writerow([account_id, account_name, account_email, account_type])

    
def list_enabled_services():
    org_client = boto3.client('organizations')

    # Call the ListAWSServiceAccessForOrganization API to retrieve the enabled services
    list_services_output = org_client.list_aws_service_access_for_organization()

    # Extract the enabled services from the response
    enabled_services = list_services_output['EnabledServicePrincipals']

    # Write the enabled services to a CSV file
    with open('enabled_services.csv', mode='w', newline='\r\n') as file:
        writer = csv.writer(file)
        writer.writerow(['Enabled Service in the Organization :'])

        for service in enabled_services:
            service_principal = service['ServicePrincipal']
            writer.writerow([service_principal])

   
    print("CSV file generated successfully.")






