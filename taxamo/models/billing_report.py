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
class Billing_report:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'billing_lines': 'list[billing_lines]',
            'count': 'number',
            'total_amount': 'number',
            'amount': '',
            'deducted': 'number'

        }


        #Billing statement lines
        self.billing_lines = None # list[billing_lines]
        #Line item count for this group of lines
        self.count = None # number
        #Total transaction amount, including VAT, which is used for line total amount calculation.
        self.total_amount = None # number
        #Transactions amount, without VAT, which is used for line 
        self.amount = None # 
        #Tax deducted transaction count.
        self.deducted = None # number
        
