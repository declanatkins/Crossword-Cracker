from __future__ import annotations

from enum import Enum
from typing import List


class CellType(Enum):
    EMPTY = 0
    BLOCK = 1
    LETTER = 2


class Cell:

    def __init__(self, celltype: CellType, letter: str | None = None):
        self.celltype = celltype
        self.letter = letter


class Grid:

    def __init__(self, cells: List[List[Cell]]):
        self.cells = cells
        self.clue_cells_across = self._get_clue_cells_across()
        self.clue_cells_down = self._get_clue_cells_down()

    def _get_clue_cells_across(self) -> List[List[Cell]]:
        clue_cells: List[List[Cell]] = []
        current_clue: List[Cell] = []
        for row in self.cells:
            for cell in row:
                if cell.celltype == CellType.BLOCK:
                    if current_clue:
                        clue_cells.append(current_clue)
                        current_clue = []
                else:
                    current_clue.append(cell)
            if current_clue:
                clue_cells.append(current_clue)
                current_clue = []
        return clue_cells

    def _get_clue_cells_down(self) -> List[List[Cell]]:

        clue_cells: List[List[Cell]] = []
        current_clue: List[Cell] = []
        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                cell = self.cells[j][i]
                if cell.celltype == CellType.BLOCK:
                    if current_clue:
                        clue_cells.append(current_clue)
                        current_clue = []
                else:
                    current_clue.append(cell)
            if current_clue:
                clue_cells.append(current_clue)
                current_clue = []
        return clue_cells
