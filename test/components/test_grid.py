import pytest

from crossword.components.grid import Cell, CellType, Grid


@pytest.mark.parametrize(
    "grid, clue_cells_across, clue_cells_down",
    [
        (
            Grid(
                [
                    [
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                    ],
                    [
                        Cell(CellType.BLOCK),
                        Cell(CellType.LETTER, "A"),
                        Cell(CellType.LETTER, "B"),
                        Cell(CellType.BLOCK),
                    ],
                    [
                        Cell(CellType.BLOCK),
                        Cell(CellType.LETTER, "C"),
                        Cell(CellType.LETTER, "D"),
                        Cell(CellType.BLOCK),
                    ],
                    [
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                        Cell(CellType.BLOCK),
                    ],
                ]
            ),
            [
                [Cell(CellType.LETTER, "A"), Cell(CellType.LETTER, "B")],
                [Cell(CellType.LETTER, "C"), Cell(CellType.LETTER, "D")],
            ],
            [
                [Cell(CellType.LETTER, "A"), Cell(CellType.LETTER, "C")],
                [Cell(CellType.LETTER, "B"), Cell(CellType.LETTER, "D")],
            ],
        )
    ],
)
def test_create_grid_parses_correct_clue_cells(
    grid, clue_cells_across, clue_cells_down
):

    assert len(grid.clue_cells_across) == len(clue_cells_across)
    assert len(grid.clue_cells_down) == len(clue_cells_down)

    for i in range(len(clue_cells_across)):
        assert len(grid.clue_cells_across[i]) == len(clue_cells_across[i])
        for j in range(len(clue_cells_across[i])):
            assert (
                grid.clue_cells_across[i][j].celltype
                == clue_cells_across[i][j].celltype
            )
            assert grid.clue_cells_across[i][j].letter == clue_cells_across[i][j].letter

    for i in range(len(clue_cells_down)):
        assert len(grid.clue_cells_down[i]) == len(clue_cells_down[i])
        for j in range(len(clue_cells_down[i])):
            assert grid.clue_cells_down[i][j].celltype == clue_cells_down[i][j].celltype
            assert grid.clue_cells_down[i][j].letter == clue_cells_down[i][j].letter
