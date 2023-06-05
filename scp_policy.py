

import boto3
import json

def list_scp_policies():
    # Create a Boto3 client for AWS Organizations
    client = boto3.client('organizations')

    # Retrieve the list of SCPs
    response = client.list_policies(Filter='SERVICE_CONTROL_POLICY')

    # Extract the list of policies
    scp_policies = response['Policies']

    # Get the details of each SCP
    for scp_policy in scp_policies:
        policy_id = scp_policy['Id']
        policy_name = scp_policy['Name']
        
        # Retrieve the policy content
        policy_response = client.describe_policy(PolicyId=policy_id)
        policy_content_str = policy_response['Policy']['Content']
        policy_content = json.loads(policy_content_str)

        # Parse the policy content to identify denied resources and actions
        denied_resources = []
        denied_actions = []
        for statement in policy_content['Statement']:
            if statement['Effect'] == 'Deny':
                denied_resources.extend(statement.get('Resource', []))
                denied_actions.extend(statement.get('Action', []))

        # Add denied resources and actions to the policy details
        scp_policy['DeniedResources'] = denied_resources
        scp_policy['DeniedActions'] = denied_actions

    # Write the SCP policy details to a JSON file
    with open('scp_policies.json', 'w') as file:
        json.dump(scp_policies, file, indent=4)

    print("JSON file generated successfully.")

# Call the function to list SCP policies and store the output in a JSON file
list_scp_policies()
