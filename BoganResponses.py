import os
import math
import time
import tweepy
import random


class boganResponses:
    @staticmethod
    def randomizer(self):
        randomizer = random.randint(1, 9)
        if randomizer == 1:
            a = boganResponses.bogan_response_1(boganResponses)
        elif randomizer == 2:
            a = boganResponses.bogan_response_2(boganResponses)
        elif randomizer == 3:
            a = boganResponses.bogan_response_3(boganResponses)
        elif randomizer == 4:
            a = boganResponses.bogan_response_4(boganResponses)
        elif randomizer == 5:
            a = boganResponses.bogan_response_5(boganResponses)
        elif randomizer == 6:
            a = boganResponses.bogan_response_6(boganResponses)
        elif randomizer == 7:
            a = boganResponses.bogan_response_7(boganResponses)
        elif randomizer == 8:
            a = boganResponses.bogan_response_8(boganResponses)
        elif randomizer == 9:
            new_random = random.randint(1, 5)
            if new_random == 1:
                a = boganResponses.bogan_response_9(boganResponses)
            else:
                boganResponses.randomizer(boganResponses)
        return a

    @staticmethod
    def bogan_response_1(self):
        percentage = random.randint(100, 1000)
        response = f"Just got my dna results back. {percentage} % jew. :("
        return response

    @staticmethod
    def bogan_response_2(self):
        percentage = random.randint(1, 9)
        response = f"sorry man, going to see my great-grandpa in orem and he lives {percentage} hours away. Maybe next month :("
        return response

    @staticmethod
    def bogan_response_3(self):
        percentage = random.randint(1, 4)
        response = f"just got stage {percentage} panky cancer"
        return response

    @staticmethod
    def bogan_response_4(self):
        percentage = random.randint(100, 1000)
        response = f"gf {percentage}% cheated on me again lol"
        return response

    @staticmethod
    def bogan_response_5(self):
        percentage = random.randint(100, 1000)
        response = (
            f"someone pass the narcan™ I'm {percentage}% sure i'm about to overdose lol"
        )
        return response

    @staticmethod
    def bogan_response_6(self):
        percentage = random.randint(7, 10)
        response = (
            f"I hope my wifes boyfriend lets me stay up past  {percentage} pm tonight 😊"
        )
        return response

    @staticmethod
    def bogan_response_7(self):
        percentage = random.randint(7, 10)
        if percentage == 1:
            suffix = "st"
        if percentage == 2:
            suffix = "nd"
        if percentage == 3:
            suffix = "rd"
        else:
            suffix = "th"
        response = f"just got {percentage}{suffix} chair sax. Thanks Dayne, I won't let you down"
        return response

    @staticmethod
    def bogan_response_8(self):
        percentage = random.randint(1, 99)
        response = f"just got a new shipment of {percentage} hair growth creams"
        return response

    @staticmethod
    def bogan_response_9(self):
        percentage = random.randint(1, 99)
        response = f"alright im {percentage}% sure im living in a simulation lmao"
        return response

    @staticmethod
    def bogan_response_10(self):
        # Post an image
        pass
