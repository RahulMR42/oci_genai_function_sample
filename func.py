# Copyright (c) 2025 Oracle and/or its affiliates.
## All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl

import io
import os
import json
import logging
import oci
from oci.util import to_dict
from fdk import response

class Ocigenai:
    def __init__(self):
        """
        Init the class 
        """
        OCI_CONFIG = {}
        signer = oci.auth.signers.get_resource_principals_signer()
        self.region = os.getenv('OCI_REGION',default="us-chicago-1")
        self.CLIENT_KWARGS = {
            "retry_strategy": oci.retry.DEFAULT_RETRY_STRATEGY,
            "timeout": (10, 240),  # default timeout config for OCI Gen AI service
            }
        self.CLIENT_KWARGS.update({'config': OCI_CONFIG})
        self.CLIENT_KWARGS.update({'signer': signer})
        try:
            self.generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(**self.CLIENT_KWARGS)
        except Exception as error:
            logging.getLogger().error(f"Error in Generative AI Controller: {str(error)}")
            return json.dumps({"error": str(error)})
    def chat(self,data):
        """
        Function to run chat router against OCI Genai,
        Input : Json body
        Output : 
        """
        try:
            chat_response = self.generative_ai_inference_client.chat(data)
            return chat_response
        except Exception as error:
            logging.getLogger().error(f"Error in Generative AI Chat: {str(error)}")
            return json.dumps({"error": str(error)})

    
def handler(ctx, data: io.BytesIO = None):
    """
    Function handler code.
    """
    try:
        body = json.loads(data.getvalue())
        handler = Ocigenai()
        result = handler.chat(data=body)
        logging.getLogger().info(str(result))
    
        return response.Response(
            ctx, 
            response_data=result.data,
            headers={"Content-Type": "application/json"})

    except Exception as error:
        logging.getLogger().error(f"Error in Generative AI function: {str(error)}")
        return json.dumps({"error": f"Error in Generative AI function - {str(error)}","details":str(result)})
    
