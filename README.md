## Sample function to use as a wrapper for OCI Genai Chat (for Demo only)

### Setup 
- Set up necessary dynamic group with function reference and policy to allow function to use generative-ai-family or specific resource accordingly.

- Set up necessary dynamic group with ApiGateway reference and policy to allow to use function family.

- Do necessary context setup for Function/OCID (Refer OCI Function doc for more) and deploy 

```
fn config app <your-app-name> OCI_REGION <OCI Region> #Default is us-chicago-1
fn -v deploy --app <your-app-name>
```

- Associate it with API Gateway behind a deployment.

- Refer `request.py` for sample execution.

