"""
    REST API Documentation for TheOrgBook

    TheOrgBook is a repository for Verifiable Claims made about Organizations related to a known foundational Verifiable Claim. See https://github.com/bcgov/VON

    OpenAPI spec version: v1
        

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import datetime

from django.db import models
from django.utils import timezone
from .VerifiableOrg import VerifiableOrg
from .DoingBusinessAs import DoingBusinessAs
from .LocationType import LocationType

from auditable.models import Auditable

class Location(Auditable):	    
    verifiableOrgId = models.ForeignKey('VerifiableOrg', related_name='locations', default=0)
    doingBusinessAsId = models.ForeignKey('DoingBusinessAs', related_name='locations', blank=True, null=True)   
    locationTypeId = models.ForeignKey('LocationType', related_name='locationTypes')   
    addressee = models.CharField(max_length=255, blank=True, null=True)   
    addlDeliveryInfo = models.CharField(max_length=255, blank=True, null=True)   
    unitNumber = models.CharField(max_length=255, blank=True, null=True)   
    streetAddress = models.CharField(max_length=255, blank=True, null=True)   
    municipality = models.CharField(max_length=255, blank=True, null=True)   
    province = models.CharField(max_length=255, blank=True, null=True)   
    postalCode = models.CharField(max_length=255, blank=True, null=True)   
    latLong = models.CharField(max_length=255, blank=True, null=True)   
    effectiveDate = models.DateField(default=timezone.now)   
    endDate = models.DateField(blank=True, null=True)   
    class Meta:
        db_table = 'LOCATION'
