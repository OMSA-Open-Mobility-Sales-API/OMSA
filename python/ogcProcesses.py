from flask import Request
from abc import ABC, abstractmethod

class processHandler(ABC):
    @abstractmethod
    def execute(self, defaultInput):
        pass

class searchOfferHandler(processHandler):
    def __init__(self):
        pass

    def execute(self, defaultInput):
        return { 
                "type": "OfferCollection",
                "offers": [ 
                    { "type": "offer"
                    , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b"
                    , "properties": 
                        {
                            "legs": [ 
                                { "type": "leg"
                                , "id": "ff6c6c75-8cf0-4d5c-9e54-962e06a12e86"
                                , "startTime": "2025-04-02T21:03:00Z"
                                , "endTime": "2025-04-03T04:27:00Z"
                                , "from": { "id": "NSR:StopPlace:337", "name": "Oslo S" }
                                , "to": { "id": "NSR:StopPlace:548", "name": "Bergen stasjon" }
                                , "traveller": "c2ed41f5-2fd2-4f38-afb1-edbd479d30a8"
                                , "products": [ "VYG:Product:NightRail" ] 
                                } 
                            ]
                            , "products": [ 
                                { "type": "product", 
                                    "id": "VYG:Product:NightRail" } ]
                            , "price": { "amount": 1193, "currencyCode": "NOK" }
                            , "mode": "TRAIN"
                            , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b" 
                        }
                    , "links": [
                        { 
                            "rel": "purchase-package",
                            "method": "POST",
                            "url": "/processes/purchase-package/execute",
                            "body": { "offerId": "96217fe2-c7ac-4f49-9561-4f6245c5e28b" } }
                        ] 
                    } 
                ],
                "numberMatched" : 1,
                "numberReturned": 1
            }

class selectOffersHandler(processHandler):
    def __init__(self):
        pass

    def execute(self, defaultInput):
        return { 
                "type": "package",
                "id": "5f75913f-a8bc-4e2d-b060-bd431744bc7f",
                "status": "selected",
                "price": { "amount": 1193, "currencyCode": "NOK" },
                "offers": [
                    { "type": "offer"
                    , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b"
                    , "properties": 
                        {
                            "legs": [ 
                                { "type": "leg"
                                , "id": "ff6c6c75-8cf0-4d5c-9e54-962e06a12e86"
                                , "startTime": "2025-04-02T21:03:00Z"
                                , "endTime": "2025-04-03T04:27:00Z"
                                , "from": { "id": "NSR:StopPlace:337", "name": "Oslo S" }
                                , "to": { "id": "NSR:StopPlace:548", "name": "Bergen stasjon" }
                                , "traveller": "c2ed41f5-2fd2-4f38-afb1-edbd479d30a8"
                                , "products": [ "VYG:Product:NightRail" ] 
                                } 
                            ]
                            , "products": [ 
                                { "type": "product", 
                                    "id": "VYG:Product:NightRail" } ]
                            , "price": { "amount": 1193, "currencyCode": "NOK" }
                            , "mode": "TRAIN"
                            , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b" 
                        }
                    , "links": [
                        ] 
                    } 
                ],
                "guarantees": [],
                "travellers": [{ "type": "user_profile", 
                                    "id": "c2ed41f5-2fd2-4f38-afb1-edbd479d30a8", 
                                    "ageGroup": "adult" }],
                "links": [
                        {   "rel": "purchase-package",
                            "method": "POST",
                            "url": "/processes/purchase-package/execute",
                            "body": { "packageId": "5f75913f-a8bc-4e2d-b060-bd431744bc7f" } },
                        {   "rel": "assign-asset",
                            "description": "Assign a seat Oslo S - Bergen stasjon",
                            "method": "POST",
                            "url": "/processes/assign-asset/execute",
                            "body": { 
                                "packageId": "5f75913f-a8bc-4e2d-b060-bd431744bc7f"
                                , "offerId": "96217fe2-c7ac-4f49-9561-4f6245c5e28b"
                                , "legId": "ff6c6c75-8cf0-4d5c-9e54-962e06a12e86" } }
                        ]
            }

class purchasePackageHandler(processHandler):
    def __init__(self):
        pass

    def execute(self, defaultInput):
        return { 
                "type": "package",
                "id": "5f75913f-a8bc-4e2d-b060-bd431744bc7f",
                "status": "confirmed",
                "price": { "amount": 1193, "currencyCode": "NOK" },
                "offers": [
                    { "type": "offer"
                    , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b"
                    , "properties": 
                        {
                            "legs": [ 
                                { "type": "leg"
                                , "id": "ff6c6c75-8cf0-4d5c-9e54-962e06a12e86"
                                , "startTime": "2025-04-02T21:03:00Z"
                                , "endTime": "2025-04-03T04:27:00Z"
                                , "from": { "id": "NSR:StopPlace:337", "name": "Oslo S" }
                                , "to": { "id": "NSR:StopPlace:548", "name": "Bergen stasjon" }
                                , "traveller": "c2ed41f5-2fd2-4f38-afb1-edbd479d30a8"
                                , "products": [ "VYG:Product:NightRail" ] 
                                } 
                            ]
                            , "products": [ 
                                { "type": "product", 
                                    "id": "VYG:Product:NightRail" } ]
                            , "price": { "amount": 1193, "currencyCode": "NOK" }
                            , "mode": "TRAIN"
                            , "id": "96217fe2-c7ac-4f49-9561-4f6245c5e28b" 
                        }
                    } 
                ],
                "guarantees": [],
                "travellers": [{ "type": "user_profile", 
                                    "id": "c2ed41f5-2fd2-4f38-afb1-edbd479d30a8", 
                                    "ageGroup": "adult" }],
                "links": [
                        {   "rel": "refund-options",
                            "method": "GET",
                            "url": "/collections/refund-options/items",
                            "body": { "packageId": "5f75913f-a8bc-4e2d-b060-bd431744bc7f" } }
                        ]
            }

class processExecutor:
    request : Request = None
    processId = None
    def __init__(self, req, processId):
        self.request = req
        self.processId = processId
    
    def execute(self):
        handler = self.get_handler()
        defaultInput = self.request.get_json()['inputs']
        return handler.execute(defaultInput)
    
    def get_handler(self) -> processHandler:
        if self.processId == 'search-offers':
            return searchOfferHandler()
        elif self.processId == 'select-offers':
            return selectOffersHandler()
        elif self.processId == 'purchase-package':
            return purchasePackageHandler()
        elif self.processId == 'claim-refund-option':
            return purchasePackageHandler()
    
