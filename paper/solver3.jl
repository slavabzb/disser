#!/usr/bin/env julia

using Base.Test
using MathProgBase
using Drs

A = Float64[3 4; 6 1]
b = Float64[6, 3]
c = Float64[-2, -1]

s = linprog(c, A, '<', b, -Inf, Inf, DrsMathProgSolver())

@test s.status == :Optimal
@test s.objval == -13/7
@test s.sol == [2/7, 9/7]
