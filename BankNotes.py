# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:27:19 2023

@author: win10
"""


from pydantic import BaseModel

class BankNotes(BaseModel):
    variance: float
    skewnwss: float
    curtosis: float
    entropy: float
