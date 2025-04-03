from flask import Request
from abc import ABC, abstractmethod

class collectionHandler(ABC):
    @abstractmethod
    def items(self, params):
        pass

class refundOptionsHandler(collectionHandler):
    def items(self, params):
        return { 
                "type": "RefundOptionCollection",
                "options": [
                    { "id": "07bfca3c-4f96-4920-b145-5f203ce0807f"
                    , "properties": 
                        { "type": "refund-option"
                        , "id": "07bfca3c-4f96-4920-b145-5f203ce0807f"
                        , "packageState": "cancelled"
                        , "refundType": "package_refund"
                        , "consequences": [ { "category": "voucher"
                                            , "amount": 1000
                                            , "currencyCode": "NOK" } ]
                        }
                    , "links": [ 
                        {   "rel": "claim-refund-options",
                            "method": "POST",
                            "url": "/processes/claim-refund-option/execute",
                            "body": { "refundOptionId": "07bfca3c-4f96-4920-b145-5f203ce0807f" } }
                    ] 
                } ]
            }

class collectionRetriever:
    request : Request = None
    collectionId = None
    def __init__(self, req, collectionId):
        self.request = req
        self.collectionId = collectionId
    
    def items(self):
        handler = self.get_handler()
        return handler.items(self.request.args)
    
    def get_handler(self) -> collectionHandler:
        if self.collectionId == 'refund-options':
            return refundOptionsHandler()
