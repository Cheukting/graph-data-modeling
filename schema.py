####
# This is the script for storing the schema of your TerminusDB
# database for your project.
# Use 'terminusdb commit' to commit changes to the database and
# use 'terminusdb sync' to change this file according to
# the exsisting database schema
####

from typing import List, Optional, Set

from terminusdb_client.woqlschema import (
    DocumentTemplate,
    EnumTemplate,
    HashKey,
    TaggedUnion,
)


class Team(EnumTemplate):
    """Team within the company"""
    marketing = "Marketing"
    it = "Information Technology"


class Address(DocumentTemplate):
    """Address consist of street (with street number), town and postcode"""
    _subdocument = []
    street: str
    town: str
    postcode: str


class Employee(DocumentTemplate):
    """Employee of the Company"""
    name: str
    title: str
    manager: Optional['Employee']
    address: Address
    contact_number: str
