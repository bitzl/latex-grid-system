latex-grid-system
=================

latex-grid-system is a package for the LaTeX typesetting system implementing a grid system as known from CSS grid systems. This is useful for creating box layouts as used in brochures.

Usage:

```latex
\begin{row}{<Columns>}{<Cells in row>}
    \begin{cell}{<Columns for this cell>}
    Some text using 2/3 of the width.
    \end{cell}
    \begin{cell}{<Columns for this cell>}
    Some text using 1/3 of the width.
    \end{cell}
\end{row}
```


Example:

```latex
\begin{row}{3}{2}
    \begin{cell}{2}
    Some text using 2/3 of the width.
    \end{cell}
    \begin{cell}{1}
    Some text using 1/3 of the width.
    \end{cell}
\end{row}
````

Contribute
==========

This package is developed a GitHub:

	https://github.com/bitzl/latex-grid-system

Please feel free to fork and contribute.