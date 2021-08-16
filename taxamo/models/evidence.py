#!/usr/bin/env python
"""
Copyright 2014-2021 by Taxamo

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
class Evidence:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'by_token': 'evidence_schema',
            'by_cc': 'evidence_schema',
            'by_2003_rules': 'evidence_schema',
            'forced': 'evidence_schema',
            'by_payment_method': 'evidence_schema',
            'by_ip': 'evidence_schema',
            'guessed_from_ip': 'evidence_schema',
            'other_commercially_relevant_info': 'evidence_schema',
            'by_billing': 'evidence_schema',
            'by_tax_number': 'evidence_schema',
            'self_declaration': 'evidence_schema'

        }


        #Country detected from SMS token
        self.by_token = None # evidence_schema
        #Country detected by credit card number prefix
        self.by_cc = None # evidence_schema
        #Used when merchant uses 2003 EU VAT rules.
        self.by_2003_rules = None # evidence_schema
        #Country forced by paramters
        self.forced = None # evidence_schema
        #Country detected by payment method.
        self.by_payment_method = None # evidence_schema
        #Country detected by IP
        self.by_ip = None # evidence_schema
        #Country guessed from IP due to lack of other evidence
        self.guessed_from_ip = None # evidence_schema
        #Additional evidence held by the merchant. Can be used only with a private token.
        self.other_commercially_relevant_info = None # evidence_schema
        #Country detected by billing country code
        self.by_billing = None # evidence_schema
        #Country detected from EU TAX number
        self.by_tax_number = None # evidence_schema
        #Self declared country as evidence. Requires merchant setting to be active.
        self.self_declaration = None # evidence_schema
        
