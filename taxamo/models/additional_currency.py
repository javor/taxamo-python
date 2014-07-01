#!/usr/bin/env python
"""
Copyright 2014 Wordnik, Inc.

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
class Additional_currency:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'currency_code': 'str',
            'amount': 'number',
            'tax_amount': 'number',
            'fx_rate': 'number',
            'total_amount': 'number'

        }


        #3-letter ISO currency code.
        self.currency_code = None # str
        #Amount (w/o TAX) in designated currency.
        self.amount = None # number
        #Tax amount in designated currency.
        self.tax_amount = None # number
        #Foreign exchange rate used in calculation
        self.fx_rate = None # number
        #Total amount in designated currency.
        self.total_amount = None # number
        
