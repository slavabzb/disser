#!/usr/bin/env julia

using Base.Test
using MathProgBase
using Drs

A = Float64[2 1; 2 3; 3 1]
b = Float64[18, 42, 24]
c = Float64[-3, -2]

s = linprog(c, A, '<', b, -Inf, Inf, DrsMathProgSolver())

@test s.status == :Optimal
@test s.objval == -33
@test s.sol == [3, 12]
