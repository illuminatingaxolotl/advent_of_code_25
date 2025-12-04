#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 18:25:33 2025

@author: svenja

get the neighbours of a number in a matrix or the indices of those neighbours
i: outer lists or the rows of the matrix
j: inner lists colums of the matrix
"""
def to(i,j,matrix): #top      
    if i!=0:
         return matrix[i-1][j]
    return None


def bo(i,j,matrix): #bottom              
    if i!=len(matrix)-1:
         return matrix[i+1][j]
    return None


def tl(i,j,matrix): #top left
    if i!=0 and j!=0:
        return matrix[i-1][j-1]
    return None


def tr(i,j,matrix): #top right
    if i!=0 and j!=len(matrix[i])-1:
        return matrix[i-1][j+1]
    return None


def bl(i,j,matrix): #bottom left
    if i!=len(matrix)-1 and  j!=0:
        return matrix[i+1][j-1]
    return None


def br(i,j,matrix): #bottom right
    if i!=len(matrix)-1 and  j!=len(matrix[i])-1:
        return matrix[i+1][j+1]
    return None
    

def le(i,j,matrix): #left             
    if j!=0:
         return matrix[i][j-1]
    return None
     
     
def ri(i,j,matrix): #right             
    if j!=len(matrix[i])-1:
         return matrix[i][j+1]
    return None


#indices

def in_to(i,j,matrix): #top      
    if i!=0:
         return i-1,j
    return None


def in_bo(i,j,matrix): #bottom              
    if i!=len(matrix)-1:
         return i+1,j
    return None


def in_tl(i,j,matrix): #top left
    if i!=0 and j!=0:
        return i-1,j-1
    return None


def in_tr(i,j,matrix): #top right
    if i!=0 and j!=len(matrix[i])-1:
        return i-1,j+1
    return None


def in_bl(i,j,matrix): #bottom left
    if i!=len(matrix)-1 and  j!=0:
        return i+1,j-1
    return None


def in_br(i,j,matrix): #bottom right
    if i!=len(matrix)-1 and  j!=len(matrix[i])-1:
        return i+1,j+1
    return None
    

def in_le(i,j,matrix): #left             
    if j!=0:
         return i,j-1
    return None
     
     
def in_ri(i,j,matrix): #right             
    if j!=len(matrix[i])-1:
         return i,j+1
    return None

#return all neighbours

def al(i,j,matrix):
    return[to(i,j,matrix),bo(i,j,matrix),tl(i,j,matrix),tr(i,j,matrix),bl(i,j,matrix),br(i,j,matrix),le(i,j,matrix),ri(i,j,matrix)]

def in_al(i,j,matrix):
    return[in_to(i,j,matrix),in_bo(i,j,matrix),in_tl(i,j,matrix),in_tr(i,j,matrix),in_bl(i,j,matrix),in_br(i,j,matrix),in_le(i,j,matrix),in_ri(i,j,matrix)]


    