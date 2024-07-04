# Integrations

Project focused to implement a basic ETL workflow using microservices for each of the major steps.

# Steps

## Extraction

This project extracts relevant data from API: https://pokeapi.co/api/v2/pokemon/ needed for creation of cards

## Transform

This project receives information from Extraction step and converts it to a card that can be displayed in a html

## Load

This project saves the cards to a Blob Storage hosted in Azure public cloud.
