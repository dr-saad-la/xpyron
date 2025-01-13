"""
Xpyron - An Educational Deep Learning Framework
"""

from importlib import metadata

try:
    __version__ = metadata.version("xpyron")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

# Add any imports or package initialization here

def version_info():
    """Return version information for Xpyron."""
    return {
        "xpyron": __version__,
        "python": metadata.version("python"),
        "numpy": metadata.version("numpy"),
        "matplotlib": metadata.version("matplotlib"),
        "scikit-learn": metadata.version("scikit-learn")
    }
