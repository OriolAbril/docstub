from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray


def func_object_with_numpy_objects(
    a1: np.np.int8, a2: np.np.int16, a3: np.typing.DTypeLike, a4: np.typing.DTypeLike
) -> None: ...


def func_ndarray(
    a1: NDArray, a2: np.NDArray, a3: NDArray[float], a4: NDArray[np.uint8] = ...
) -> NDArray[np.uint8] | NDArray[complex]: ...


def func_array_like(
    a1: ArrayLike, a2: ArrayLike, a3: ArrayLike[float], a4: ArrayLike[np.uint8]
) -> ArrayLike[np.uint8] | ArrayLike[complex]: ...
