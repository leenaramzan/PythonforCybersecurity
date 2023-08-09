#!/usr/bin/env python3
# example workign with Functions
#By Leena on 07/27

def send_message():
    daily_weather = input("Is today a sunny day? (Y/N) ")

    if daily_weather in {"Y", "y"}:
        for _ in range(10):
            print("Yeah is is!")

send_message()