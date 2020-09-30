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
class C:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'day_raw': 'str',
            'value': 'number',
            'status': 'str',
            'day': 'str'

        }


        #Date for stats in yyyy-MM-dd'T'hh:mm:ss'Z' format.
        self.day_raw = None # str
        #Transaction count.
        self.value = None # number
        #Transaction status (C or N).
        self.status = None # str
        #Date for stats in yyyy-MM-dd format.
        self.day = None # str
        
