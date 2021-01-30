#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Input::Initialization:: *)
i = Import["/home/pi/Documents/froggo.jpeg"]


Print["Image imported"]
ImageIdentify[i]
Print["Identified Image"]
Export["/home/pi/Documents/bigData.txt" ,ImageIdentify[i]]
Print["See bigData.txt for image"]



