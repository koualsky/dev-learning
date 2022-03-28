from datetime import datetime, date, time
from pydantic import BaseModel, Field  # from typing import Any, Dict, List
from typing import List



class StatusInformation(BaseModel):
    status_date: date = Field(alias='statusDate')
    status_time: time = Field(alias='statusTime')
    status_code: str = Field(alias='statusCode')
    description: str = Field(alias='description')
    result_code: str = Field(alias='resultCode')
    result_message: str = Field(alias='resultMessage')
    city: str = Field(alias='city')
    zip_code: str = Field(alias='zipCode')
    country_code: str = Field(alias='countryCode')


class ListOfCurrentShipmentStatus(BaseModel):
    shipment_id: str = Field(alias='shipmentID')
    status_information: StatusInformation = Field(alias='statusInformation')


class TrackingEvent(BaseModel):
    list_of_current_shipment_status: List[ListOfCurrentShipmentStatus] = Field(alias='listOfCurrentShipmentStatus')


response_json = {
    "listOfCurrentShipmentStatus": [
        {
            "shipmentID": "MCQ190200001334",
            "statusInformation": {
                "statusDate": "2020-11-21",
                "statusTime": "08:59:53",
                "statusCode": "50-1-2",
                "statusImageURL": "https://sisyr.hlg.de/SISY_Theme/img/Se_05.jpg",
                "statusImageID": 5,
                "description": "string",
                "resultCode": "string",
                "resultMessage": "string",
                "expectedDelivery": {
                    "expectedDate": "2020-06-06",
                    "expectedTimeEarliest": {
                        "hour": 0,
                        "minute": 0,
                        "second": 0,
                        "nano": 0
                    },
                    "expectedTimeLatest": {
                        "hour": 0,
                        "minute": 0,
                        "second": 0,
                        "nano": 0
                    },
                    "fixedDateOfDelivery": True
                },
                "city": "Hamburg",
                "zipCode": "22083",
                "countryCode": "DEU"
            }
        }
    ]
}


tracking = TrackingEvent(**response_json)
breakpoint()
# tracking.list_of_current_shipment_status[0].shipment_id
