# import boto3

# def get_aws_accounts():
#     org_client = boto3.client('organizations')
#     response = org_client.list_accounts()

#     accounts = response['Accounts']

#     for account in accounts:
#         account_id = account['Id']
#         account_name = account['Name']
#         email = account['Email']
#         status = account['Status']

#         # Determine account type
#         account_type = 'Joined' if status == 'ACTIVE' else 'Created'

#         print(f"Account Name: {account_name}")
#         print(f"Account ID: {account_id}")
#         print(f"Email: {email}")
#         print(f"Account Type: {account_type}")
#         print("------------------------------")

# get_aws_accounts()
# import boto3
# output1=[]

# def get_aws_accounts():
   
#     org_client = boto3.client('organizations')
#     response = org_client.list_accounts()

#     accounts = response['Accounts']

#     for account in accounts:
#         account_id = account['Id']
#         account_name = account['Name']
#         email = account['Email']
#         service_principal = account.get('ServicePrincipal')

#         # Determine account type
#         account_type = 'Created' if not service_principal or service_principal == '*' or service_principal == 'organizations.amazonaws.com' else 'Joined'

#         print(f"Account Name: {account_name}")
#         print(f"Account ID: {account_id}")
#         print(f"Email: {email}")
#         print(f"Account Type: {account_type}")
#         print("------------------------------")


# import boto3

# def get_aws_accounts():
#     org_client = boto3.client('organizations')
#     response = org_client.list_accounts()

#     accounts = response['Accounts']

#     for account in accounts:
#         account_id = account['Id']
#         account_name = account['Name']
#         email = account['Email']
#         service_principal = account.get('ServicePrincipal')

#         # Determine account type
#         account_type = 'Created' if not service_principal else 'Joined'

#         print(f"Account Name: {account_name}")
#         print(f"Account ID: {account_id}")
#         print(f"Email: {email}")
#         print(f"Account Type: {account_type}")
#         print("------------------------------")
# import boto3

# def get_aws_accounts():
#     org_client = boto3.client('organizations')
#     response = org_client.list_accounts()

#     accounts = response['Accounts']

#     for account in accounts:
#         account_id = account['Id']
#         account_name = account['Name']
#         email = account['Email']
#         joined_method = account.get('JoinedMethod')

#         # Determine account type
#         account_type = 'Created' if joined_method is None else 'Joined'

#         print(f"Account Name: {account_name}")
#         print(f"Account ID: {account_id}")
#         print(f"Email: {email}")
#         print(f"Account Type: {account_type}")
#         print("------------------------------")
# import boto3
# import csv

# def get_aws_accounts():
#     org_client = boto3.client('organizations')
#     response = org_client.list_accounts()

#     accounts = response['Accounts']

#     with open('aws_accounts.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Account Name', 'Account ID', 'Email', 'Account Type'])

#         for account in accounts:
#             account_id = account['Id']
#             account_name = account['Name']
#             email = account['Email']
#             joined_method = account.get('JoinedMethod')

#             # Determine account type
#             account_type = 'Created' if joined_method is None else 'Joined'

#             writer.writerow([account_name, account_id, email, account_type])

#     print("CSV file generated successfully.")






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






