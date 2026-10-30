"""
Rongorongo Engine — Imscribing Grammar structural analysis of the
undeciphered glyphic script of Easter Island (Rapa Nui).

Architecture follows the four-engine pattern:
  compiler.py  — parse glyph sequences to IMASM opcodes
  runtime.py   — execute the compiled stream
  callgraph.py — construct and analyze the call graph
  sectional.py — sectional/topological analysis of text structure
  primitives.py — Barthel → IG categorical opcode mapping
"""

__version__ = "0.1.0"
