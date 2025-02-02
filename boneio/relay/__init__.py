"""Relay module."""
from boneio.relay.gpio import GpioRelay
from boneio.relay.mcp import MCPRelay
from boneio.relay.pca import PWMPCA

__all__ = ["MCPRelay", "GpioRelay", "PWMPCA"]
