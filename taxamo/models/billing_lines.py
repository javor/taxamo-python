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
class Billing_lines:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'rate': 'number',
            'deducted': 'number',
            'quantity': 'str',
            'count': 'number',
            'currency': 'number',
            'value': 'number',
            'total_amount': 'number',
            'amount': '',
            'type': 'str'

        }


        #Line rate
        self.rate = None # number
        #Tax deducted transaction count.
        self.deducted = None # number
        #Item quantity
        self.quantity = None # str
        #Line item count
        self.count = None # number
        #Line currency
        self.currency = None # number
        #Line total
        self.value = None # number
        #Total transaction amount, including VAT, which is used for line total amount calculation.
        self.total_amount = None # number
        #Transactions amount, without VAT, which is used for line 
        self.amount = None # 
        #Line type
        self.type = None # str
        
