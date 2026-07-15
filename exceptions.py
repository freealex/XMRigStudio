"""
core/exceptions.py

Custom exceptions for XMRig Manager.
"""


class XMRigManagerError(Exception):
    """
    Base application error.
    """
    pass



class APIConnectionError(XMRigManagerError):
    """
    Raised when XMRig API cannot be reached.
    """
    pass



class APIAuthenticationError(XMRigManagerError):
    """
    Raised when API token is invalid.
    """
    pass



class MinerProcessError(XMRigManagerError):
    """
    Raised when miner process operations fail.
    """
    pass



class ConfigurationError(XMRigManagerError):
    """
    Raised when settings/configuration is invalid.
    """
    pass
