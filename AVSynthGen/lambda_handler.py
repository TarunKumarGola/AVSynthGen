import GPTApis

def lambda_handler(event, context):
    print("Asking to ChatGPT")
    print(event)
    return GPTApis.CheckGPTConnection()
     