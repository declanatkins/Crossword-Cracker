from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ..components.clue import Clue
from ..components.grid import Grid


class ClueParser(ABC):

    @abstractmethod
    def parse(self) -> List[Clue]:
        pass


class GridParser(ABC):

    @abstractmethod
    def parse(self) -> Grid:
        pass
