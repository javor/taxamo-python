#!/usr/bin/env python
"""
Copyright 2014 Taxamo, Ltd.

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
class ValidateTaxNumberOut:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'tax_deducted': 'bool',
            'buyer_tax_number': 'str',
            'billing_country_code': 'str'

        }


        #True if the transaction deducted from tax and no tax is applied. Either set automatically when VAT number validates with VIES correctly, but can also be provided in manual mode.
        self.tax_deducted = None # bool
        # Buyer's tax number - EU VAT number for example.
        self.buyer_tax_number = None # str
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        
