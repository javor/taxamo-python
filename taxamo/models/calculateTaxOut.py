#!/usr/bin/env python
"""
Copyright 2014-2020 by Taxamo

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
class CalculateTaxOut:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'transaction': 'transaction',
            'tax_required_fields': 'list[tax_required_fields]',
            'storage_required_fields': 'list[storage_required_fields]'

        }


        #Transaction data
        self.transaction = None # transaction
        #Fields required for tax calculation. Depends on the region/transaction type.
        self.tax_required_fields = None # list[tax_required_fields]
        #Fields required for transaction storage (can be added later - it's up to merchant software). Depends on the region/transaction type.
        self.storage_required_fields = None # list[storage_required_fields]
        
